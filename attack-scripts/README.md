# Safe Sample Event Generator

`generate_sample_events.py` writes synthetic JSON-lines records to a local file. It performs no network operations and does not attempt authentication, exploitation, scanning, shell execution, or persistence.

```bash
python3 attack-scripts/generate_sample_events.py --output sample-events.jsonl
```

Use the output for parser development or demonstrations only. It is not a substitute for validating detections against real Splunk events from your isolated lab.
