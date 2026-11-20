# Outage and mitigation modeling

`newResDist` is a prototype for studying an outage on a distribution feeder and screening possible mitigations.

## Inputs

- An OMF feeder that can be converted to an OpenDSS circuit. The model includes an Iowa 240-bus example.
- An outage CSV that identifies the affected component and outage cause. The prototype uses the first row of the CSV and expects the component name to match a line in the feeder.
- A comma-separated list of critical load names.

## Workflow and results

The prototype opens the affected line in a copy of the circuit and runs an OpenDSS power flow. It checks the outage cause and component against candidate mitigations such as undergrounding, vegetation clearance, reclosers, and backup generation.

Mitigation insertion and cost calculations are unfinished, so treat this workflow as a prototype. For an investment analysis across weather scenarios, see [resilientDist](./Models-~-resilientDist.md).
