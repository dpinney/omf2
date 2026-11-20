# Open Modeling Framework

OMF helps electric utilities model their grids and evaluate changes such as adding solar, installing batteries, and improving reliability. [Open OMF in your browser](https://omf.coop/) or [read the full documentation](./omf/docs/README.md).

<!-- omf-catalog:start -->
## What you can do with OMF

- **Run grid and energy simulations.** OMF provides Python interfaces to solvers such as GridLAB-D, OpenDSS, MATPOWER, PySAM, and REopt. [Architecture notes](./omf/docs/Dev-~-Architecture-Notes.md)
- **Edit a feeder on a map.** Draw circuit components, inspect and edit equipment, and work with feeder files in the browser. [GIS editor guide](./omf/docs/Other-~-gridEdit.md)
- **Convert circuit data.** Import Milsoft WindMil data and work with GridLAB-D, OpenDSS, and OMF feeder files. [WindMil import](./omf/docs/Other-~-Windmil-Data-Import.md) · [OpenDSS import requirements](./omf/docs/Other-~-OpenDSS-Syntax-Requirements.md)

### Screenshots

Select a screenshot to open it at full size.

#### GIS feeder editor

Inspect a feeder layout and edit circuit components in the browser. [GIS editor guide](./omf/docs/Other-~-gridEdit.md)

[![OMF feeder editor with a network diagram and editing menus](./omf/docs/images/gridEdit_fullPage.png)](./omf/docs/images/gridEdit_fullPage.png)

#### DER interconnection

Compare feeder voltages for scenarios with and without the proposed generator. [DER Interconnection guide](./omf/docs/Models-~-derInterconnection.md)

[![DER Interconnection load-flow results with scenario controls and a color-coded voltage map](./omf/docs/images/derInterconnection_loadFlowPlots.png)](./omf/docs/images/derInterconnection_loadFlowPlots.png)

#### Solar hosting capacity

See how much additional solar the example feeder can host by location. [Hosting Capacity guide](./omf/docs/Models-~-hostingCapacity.md)

[![Hosting capacity results mapped across an example feeder](./omf/docs/images/hostingCapacity_resultsMap.png)](./omf/docs/images/hostingCapacity_resultsMap.png)

#### Microgrid resilience

See how outage start time and duration affect the modeled microgrid’s ability to serve load. [Microgrid Design guide](./omf/docs/Models-~-microgridDesign.md)

[![Microgrid resilience results showing hours of load served and outage survival probability](./omf/docs/images/multiSiteMicrogridDesign_resilience.png)](./omf/docs/images/multiSiteMicrogridDesign_resilience.png)

### Grid studies and interconnection

| Model | Question it answers | Inputs | Outputs |
| --- | --- | --- | --- |
| [circuitRealTime](./omf/docs/Models-~-circuitRealTime.md) | How does a circuit respond as I change it? | Circuit components and parameters | Interactive voltages, currents, and waveforms |
| [cvrDynamic](./omf/docs/Models-~-cvrDynamic.md) | How does conservation voltage reduction affect a feeder over time? | Feeder, simulation period, and energy costs | With/without CVR load, losses, voltages, tap changes, and savings |
| [cvrStatic](./omf/docs/Models-~-cvrStatic.md) | What could a feeder save through conservation voltage reduction? | Feeder, historical demand, and program costs | Estimated energy, loss, and peak reductions and their dollar value |
| [derInterconnection](./omf/docs/Models-~-derInterconnection.md) | How would a proposed generator affect the feeder? | Feeder, DER location and equipment, operating scenarios, and screening thresholds | Voltage and thermal maps, flicker and tap checks, and fault-current tables |
| [evInterconnection](./omf/docs/Models-~-evInterconnection.md) | Can a feeder serve a proposed EV charging load? | Feeder and charging location, vehicle and charger assumptions, and rates | Charging demand, feeder voltages, protective device response, and energy costs |
| [faultAnalysis](./omf/docs/Models-~-faultAnalysis.md) | How will a feeder and its protection respond to a fault? | Feeder, fault type, location, and time | Voltage map and protective device response |
| [gridlabMulti](./omf/docs/Models-~-gridlabMulti.md) | How does a proposed change affect feeder operation? | GridLAB-D feeder cases, simulation period, and cost assumptions | Side-by-side power, voltage, and cost-benefit results |
| [hostingCapacity](./omf/docs/Models-~-hostingCapacity.md) | How much additional solar can the grid host? | AMI data or a feeder model, depending on the method | Hosting capacity estimates, tables, and maps where supported |
| [hostingExpansion](./omf/docs/Models-~-hostingExpansion.md) | How does proposed solar generation line up with system load? | AMI or direct load data, site and year, and solar system size | Plots comparing estimated solar output with system demand |
| [phaseBalance](./omf/docs/Models-~-phaseBalance.md) | Could inverter controls reduce phase imbalance on this feeder? | Feeder, inverter and control settings, and cost assumptions | Voltage and imbalance comparisons and estimated financial effects |
| [solarEngineering](./omf/docs/Models-~-solarEngineering.md) | What changes on a feeder when solar is added? | Feeder with solar, location or weather, and simulation period | Generation, meter voltages, regulator taps, and capacitor operations |
| [transmission](./omf/docs/Models-~-transmission.md) | What voltages result from a transmission power-flow study? | MATPOWER case with buses, branches, and generators | Bus voltage table and circuit visualization |
| [voltageDrop](./omf/docs/Models-~-voltageDrop.md) | Where are voltages high or low on a feeder? | Feeder and display options | Color-coded voltage map across the feeder |

### Reliability, resilience, and communications

| Model | Question it answers | Inputs | Outputs |
| --- | --- | --- | --- |
| [commsBandwidth](./omf/docs/Models-~-commsBandwidth.md) | Can the communications network carry simultaneous meter traffic? | Feeder, meter packet size, and radio and fiber capacities | Network layout, overloaded collectors or links, and equipment costs |
| [newResDist](./omf/docs/Models-~-newResDist.md) | Which mitigations could address a specific outage? | Feeder, outage records, and critical loads | Prototype outage simulation and candidate mitigation screening |
| [outageCost](./omf/docs/Models-~-outageCost.md) | What do outage records show about feeder reliability? | Feeder, outage CSV, and customer counts | Outage maps and timelines, SAIDI, SAIFI, and MAIFI |
| [resilientDist](./omf/docs/Models-~-resilientDist.md) | Which investments could keep more loads served during severe weather? | Feeder, hazard scenarios, critical loads, and investment costs | Recommended hardening and generator investments and feeder diagrams |
| [rfCoverage](./omf/docs/Models-~-rfCoverage.md) | Where might a radio tower provide coverage? | Tower coordinates, height, power, frequency, and terrain | Map of estimated signal coverage |
| [smartSwitching](./omf/docs/Models-~-smartSwitching.md) | How much reliability benefit could an added recloser provide? | Feeder, proposed recloser location, and historical or simulated faults | Before/after reliability metrics, outage costs, and feeder graphic |

### Solar, microgrids, and storage

| Model | Question it answers | Inputs | Outputs |
| --- | --- | --- | --- |
| [microgridDesign](./omf/docs/Models-~-microgridDesign.md) | Which mix of generation and storage is economical for a site? | A year of load, site details, tariffs, technology costs, and outage assumptions | REopt equipment sizing, financial results, dispatch, and outage resilience |
| [pvWatts](./omf/docs/Models-~-pvWatts.md) | How much electricity would a PV system generate? | Site, array size and orientation, losses, and simulation period | Estimated AC generation over time |
| [solarCashflow](./omf/docs/Models-~-solarCashflow.md) | How might member-owned solar change utility finances and customer bills? | Utility costs and rates, member counts, and solar adoption and size | Monthly generation, revenue, and bills for solar and non-solar members |
| [solarConsumer](./omf/docs/Models-~-solarConsumer.md) | How do rooftop purchase, community solar, and a solar PPA compare for a household? | Site and PV specifications plus prices and financing assumptions | Estimated generation and costs under each option |
| [solarFinancial](./omf/docs/Models-~-solarFinancial.md) | What is the financial return of a PV project? | Site, PV specs, installation and operating costs, and energy value | Generation estimates, annual and cumulative cash flow, and project returns |
| [solarSunda](./omf/docs/Models-~-solarSunda.md) | How does financing affect a co-op solar project's cost? | Project site and size, construction costs, and financing assumptions | Cost breakdown and levelized cost by financing structure |
| [storageArbitrage](./omf/docs/Models-~-storageArbitrage.md) | What could a battery earn by charging at low prices and discharging at high prices? | Hourly prices, load, and battery specifications and costs | Charge and discharge schedule and estimated arbitrage value |
| [storageDeferral](./omf/docs/Models-~-storageDeferral.md) | How much storage would keep a transformer or line below its limit? | Load profile, equipment loading limit, and battery and upgrade costs | Required batteries, adjusted load, dispatch, and deferral economics |
| [storagePeakShave](./omf/docs/Models-~-storagePeakShave.md) | How much could a battery save in demand charges? | Load profile, demand charges, battery specs, and dispatch strategy | Monthly peak reductions, battery dispatch, and cash flow |

### Load flexibility, forecasting, and meter data

| Model | Question it answers | Inputs | Outputs |
| --- | --- | --- | --- |
| [anomalyDetector](./omf/docs/Models-~-anomalyDetector.md) | Which load readings look unusually high or low? | Time-stamped demand history and, for some methods, weather | Demand plots with flagged observations |
| [demandResponse](./omf/docs/Models-~-demandResponse.md) | How might customers respond to a new rate or direct load control program? | A year of hourly demand and program or rate assumptions | Changed load profile, peak reduction, and costs and benefits |
| [disaggregation](./omf/docs/Models-~-disaggregation.md) | Which appliances account for a site's measured demand? | Whole-site power data and appliance-level training data | Estimated appliance demand curves and energy shares |
| [forecastLoad](./omf/docs/Models-~-forecastLoad.md) | What will hourly demand look like tomorrow? | Historical demand and forecast temperature data | Hourly forecasts, actuals, and error metrics by method |
| [forecastTool](./omf/docs/Models-~-forecastTool.md) | How likely is tomorrow to set the month's demand peak? | Historical load, temperature, and optional saved forecast models | Day-ahead demand and likelihood of setting the monthly peak |
| [phaseId](./omf/docs/Models-~-phaseId.md) | Which phase is each meter likely connected to? | AMI voltage time series, meter IDs, and recorded phases | Inferred phases, confidence, and flagged discrepancies |
| [transformerPairing](./omf/docs/Models-~-transformerPairing.md) | Which meters may be mapped to the wrong transformer? | Customer IDs and AMI voltage, real power, and reactive power | Suspected mapping corrections and correlation results |
| [vbatDispatch](./omf/docs/Models-~-vbatDispatch.md) | How much peak demand could flexible thermal loads avoid? | Device counts and settings, temperature and demand profiles, and tariffs | Virtual battery capacity, dispatch, adjusted peaks, and bill savings |
| [vbatStacked](./omf/docs/Models-~-vbatStacked.md) | What could a fleet of flexible loads earn across multiple services? | Device fleet, load and weather data, and service and payment assumptions | Dispatch, stacked revenue, cash flow, and payback |
| [weatherPull](./omf/docs/Models-~-weatherPull.md) | What historical weather data can I use for a model? | Data source, location or station, year, and parameter | Weather time series and downloadable CSV |
<!-- omf-catalog:end -->

## Installation

Run OMF locally with Git and a Python environment.

~~~bash
python -m pip install 'git+https://github.com/nreca-bts/omf'
~~~

See the [installation and test guide](./omf/docs/Dev-~-Installation-Instructions.md) for solver setup, smoke tests, and Docker.
