# Interview Demonstration Script (10–12 minutes)

## 1. Problem and architecture (1–2 min)
"I built an isolated three-node SOC lab with a Kali test workstation, an Ubuntu endpoint, and Splunk as the SIEM. The objective was to collect endpoint and service telemetry, detect a multi-stage scenario, and validate the detections against benign activity."

Show the network diagram and explain trust boundaries, forwarding, indexes, and sourcetypes.

## 2. Telemetry quality (1–2 min)
Show ingestion health and representative raw events. Explain timestamp normalization, host identity, field extraction, and why detections should not be enabled before data quality is checked.

## 3. Detection engineering (3–4 min)
Walk through D01–D04. For each rule, explain:
- behavior hypothesis
- data source and required fields
- threshold / time window
- expected false positives
- triage pivots and severity

Use the synthetic scenario searches for a repeatable demonstration. Clearly label synthetic data as synthetic.

## 4. Investigation (2 min)
Pivot from reconnaissance to SSH failures and success, then process execution and cron modification. Explain what evidence would confirm or disprove each hypothesis.

## 5. Tuning and measurement (1–2 min)
Explain allowlist ownership, false-positive review, and precision/recall. Distinguish figures reproduced from the source guide from metrics you measured yourself.

## 6. Lessons and next steps (1 min)
Discuss field extraction gaps, event ordering, window semantics, telemetry dependencies, and what you would improve before production deployment.

## Interview honesty checklist
- Never say synthetic events came from a live attack.
- Never claim the lab ran unless you built and tested it.
- Explain one detection query line by line.
- Be ready to discuss a false positive and a missed-detection scenario.
- State what is incomplete and how you would validate it.
