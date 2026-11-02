# Reproducible SOC Scenario

This folder contains deterministic, fabricated telemetry for a controlled Splunk demonstration. The generator does not execute attack techniques or interact with any host.

## Generate

```bash
python3 simulation/generate_scenario.py --output simulation/sample-scenario.jsonl
```

The dataset includes:
- 30 synthetic connection-attempt records across distinct destination ports
- 12 SSH authentication failures followed by one success
- One synthetic web-service-to-shell process execution indicator
- One synthetic cron-file modification indicator
- Four benign SSH failures from an operations host

All records include `simulation=true` and `source=synthetic-training-data`. These are test fixtures, not proof of a real intrusion or a completed live lab.

## Import into Splunk

For a quick demonstration, upload the JSONL file through Splunk's Add Data workflow and select JSON as the source type. Use a dedicated training index such as `soc_simulation`. Confirm timestamp extraction and field names before running the searches in `../splunk/simulation_detections.spl`.
