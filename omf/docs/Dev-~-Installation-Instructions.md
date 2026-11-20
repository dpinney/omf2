# Installation Instructions

Install OMF from GitHub in a Python environment with Git available. CI uses Python 3.11 and installs the revision under test with `python -m pip install .`.

```bash
python -m pip install 'git+https://github.com/nreca-bts/omf'
```

Check the installed model and OpenDSS on Linux, macOS, or Windows.

```bash
python -m omf.runAllTests --smoke
```

On Ubuntu 24.04 x86-64, use the same solver check as Linux CI. On first import, OMF attempts to install missing GridLAB-D and SPLAT commands using `sudo`. The check requires those commands and runs a bundled GridLAB-D feeder.

```bash
python -m omf.runAllTests --smoke solvers
```

Run the full integration suite or a single module with the same test runner.

```bash
python -m omf.runAllTests
python -m omf.runAllTests omf.models.modelSkeleton
```

The repository also provides an [OMF Dockerfile](https://github.com/nreca-bts/omf/blob/master/omf.dockerfile). The hosted version is available at [omf.coop](https://omf.coop/).
