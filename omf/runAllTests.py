"""
Discover OMF modules with test entrypoints and run their module-level smoke tests in a
repeatable order.
"""

import os, subprocess, sys, platform, pkgutil, importlib, omf, traceback, shutil
from concurrent.futures import ThreadPoolExecutor
from tempfile import TemporaryDirectory
from time import perf_counter

PY_BIN_NAME = 'python3'

# GitHub-hosted runners do not have the system solvers, GUI support, or stable external API access needed by these older integration-style tests.
IGNORE_FILES = ['omf.models.forecastTool', 'omf.models.solarDisagg', 'omf.cymeToGridlab', 'omf.milToGridlab', 'omf.models.transmission', 'omf.loadModelingAmi']

if platform.system()=='Windows':
	NO_WINDOWS_SUPPORT = ['omf.cymeToGridlab', 'omf.models.rfCoverage', 'omf.models.solarEngineering', 'omf.models.phaseBalance', 'omf.models.forecastTool', 'omf.distNetViz', 'omf.models.derInterconnection', 'omf.models.networkStructure', 'omf.models.smartSwitching'] # some tests are very finicky on windows
	PY_BIN_NAME = 'python' # also annoying binary naming on Windows
	IGNORE_FILES.extend(NO_WINDOWS_SUPPORT)

def get_all_testable_modules():
	''' Find all modules in the OMF with ._tests() functions defined, minus the ignored modules. '''
	# get all module names recursively
	mod_names = []
	for _, modname, _ in pkgutil.walk_packages(path=omf.__path__, prefix=omf.__name__+'.'):
		mod_names.append(modname)
	# filter out broken tests.
	good_mod_names = set(mod_names) - set(IGNORE_FILES)
	# get all test funcs
	test_funcs = []
	for mod_name in good_mod_names:
		try:
			this_mod = importlib.import_module(mod_name)
			sub_names = dir(this_mod)
			if '_tests' in sub_names:
				test_funcs.append(mod_name)
		except ImportError:
			pass
	return test_funcs

def run_tests_on_module(mod_name):
	''' e.g. run_tests_on_module('omf.models.pvWatts')'''
	import importlib
	my_mod = importlib.import_module(mod_name)
	test_func = getattr(my_mod, '_tests')
	test_func()

def run_smoke_tests(system_solvers=False):
	'''Check an installed OMF package with small model and solver cases.'''
	from omf.models import modelSkeleton
	from omf.solvers import gridlabd, opendss

	result = modelSkeleton.work(None, {'input1': '2', 'input2': '3'})
	if result['output'] != '5':
		raise RuntimeError(f'OMF model smoke test returned an unexpected result: {result}')

	opendss.runDssCommand('clear', strict=True)
	opendss.runDssCommand('new circuit.smoke basekv=12.47 bus1=source', strict=True)
	opendss.runDssCommand('new load.smoke bus1=source phases=3 kv=12.47 kw=30', strict=True)
	opendss.runDssCommand('solve', strict=True)
	if not opendss.dss.Solution.Converged() or opendss.dss.Circuit.NumBuses() != 1:
		raise RuntimeError('OpenDSS smoke circuit did not converge with one bus.')
	print('OMF model and OpenDSS smoke tests passed.')

	if system_solvers:
		missing = [name for name in ('gridlabd', 'splat', 'srtm2sdf') if not shutil.which(name)]
		if missing:
			raise RuntimeError('Required solver commands are missing from PATH: ' + ', '.join(missing))
		gridlabd._tests()
		print('GridLAB-D feeder simulation passed and SPLAT commands are available.')

def _print_header(header):
	"""
	Internal helper for run all tests print header processing.
	"""
	print('\n+------------------------+', flush=True)
	print(f'{header.upper()}', flush=True)
	print('+------------------------+\n', flush=True)

def _run_test_subprocess(module):
	'''Run a selected test with its own working directory and solver process state.'''
	env = os.environ.copy()
	package_root = os.path.dirname(os.path.dirname(os.path.abspath(omf.__file__)))
	env['PYTHONPATH'] = os.pathsep.join(filter(None, (package_root, env.get('PYTHONPATH'))))
	started_at = perf_counter()
	with TemporaryDirectory(prefix='omf-test-') as work_dir:
		result = subprocess.run(
			[sys.executable, '-m', 'omf.runAllTests', module],
			cwd=work_dir, env=env, stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT, text=True, errors='replace')
	return result, perf_counter() - started_at


def run_all_tests(parallel_modules=()):
	'''Run every discovered test, optionally isolating selected modules in subprocesses.'''
	all_testable_mods = get_all_testable_modules()
	selected = list(dict.fromkeys(parallel_modules))
	unknown = set(selected).difference(all_testable_mods)
	if unknown:
		raise ValueError('Parallel modules must be discovered tests: ' + ', '.join(sorted(unknown)))

	misfires = []
	with ThreadPoolExecutor(max_workers=2) as pool:
		background = {
			mod: pool.submit(_run_test_subprocess, mod)
			for mod in selected
		}
		for mod in all_testable_mods:
			if mod in background:
				continue
			print(f'!!!!! NOW TESTING {mod} !!!!!', flush=True)
			started_at = perf_counter()
			try:
				run_tests_on_module(mod)
			except:
				misfires.append(mod)
				traceback.print_exc()
			finally:
				print(f'{mod} took {perf_counter() - started_at:.2f}s', flush=True)

		for mod, future in background.items():
			print(f'!!!!! NOW TESTING {mod} !!!!!', flush=True)
			try:
				result, elapsed = future.result()
				print(result.stdout, end='', flush=True)
				print(f'{mod} took {elapsed:.2f}s (including subprocess startup)', flush=True)
				if result.returncode:
					misfires.append(mod)
			except Exception:
				misfires.append(mod)
				traceback.print_exc()
	_print_header('regular tests report')
	print(f'Number of modules tested: {len(all_testable_mods)}', flush=True)
	print(all_testable_mods, flush=True)
	_print_header('failed tests report')
	print(f'Number of tests failed: {len(misfires)}', flush=True)
	print(misfires, flush=True)
	_print_header('untested modules report')
	print(f'Number of untested modules: {len(IGNORE_FILES)}', flush=True)
	print(IGNORE_FILES, flush=True)
	if len(misfires) > 0:
		sys.exit(1) # trigger build failure.

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='Check an OMF installation, test one module, or run the full suite.')
	parser.add_argument('module', nargs='?', help='Dotted OMF module name, such as omf.models.modelSkeleton')
	parser.add_argument('--smoke', nargs='?', const='basic', choices=('basic', 'solvers'),
		help='Check a model and OpenDSS. Use --smoke solvers to also require GridLAB-D and SPLAT on Ubuntu.')
	parser.add_argument('--parallel-module', action='append', default=[],
		help='Queue this discovered module for an isolated worker (repeat in priority order).')
	args = parser.parse_args()
	if args.smoke:
		if args.module or args.parallel_module:
			parser.error('--smoke runs separately from module and full-suite tests.')
		run_smoke_tests(system_solvers=args.smoke == 'solvers')
	elif args.module is None:
		run_all_tests(args.parallel_module)
	elif args.parallel_module:
		parser.error('--parallel-module applies only when running the full suite.')
	elif args.module.startswith('omf.'):
		run_tests_on_module(args.module)
	else:
		parser.error('module must be a dotted name beginning with omf.')
