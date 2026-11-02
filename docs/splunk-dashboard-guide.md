# Splunk Dashboard Build Guide

Create a dashboard named **SOC Simulation Overview** using the saved searches in `../splunk/simulation_detections.spl`.

Recommended panels:

1. **Events by phase** — `index=soc_simulation simulation=true | timechart span=1m count by phase`
2. **Authentication outcomes** — `index=soc_simulation simulation=true event_type=ssh_auth | timechart span=1m count by auth_result`
3. **Top source IPs** — `index=soc_simulation simulation=true | stats count by src_ip`
4. **Detection counts** — run each D01–D04 search and chart count by detection_id.
5. **Incident timeline** — `index=soc_simulation simulation=true scenario_id="SOC-CASE-001" | sort 0 _time`

Add a visible dashboard note: **Synthetic training data — not live security telemetry.**

Take screenshots only after importing the data and confirming the panels render correctly in your own Splunk instance. Store sanitized screenshots in `evidence/screenshots/` and link them from the README.
