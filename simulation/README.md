# Reproducible SOC Scenario

This folder contains deterministic, fabricated telemetry for a controlled Splunk demonstration. The generator does not execute attack techniques or interact with any host.

## Generate

```bash
python3 simulation/generate_scenario.py --output simulation/sample-scenario.jsonl
```

The dataset contains 49 records:
- 30 synthetic connection-attempt records across distinct destination ports
- 12 SSH authentication failures followed by one success
- One synthetic web-service-to-shell process execution indicator
- One synthetic cron-file modification indicator
- Four benign SSH failures from an operations host

All records include `simulation=true` and `source=synthetic-training-data`. These are test fixtures, not proof of a real intrusion or a completed live lab. Event timestamps are fixed at 2026-01-15 UTC, so select **All time** in Splunk.

## Import into Splunk Enterprise

1. In Splunk, go to **Settings → Indexes → New Index** and create `soc_simulation`.
2. Open **Add Data → Upload** and select `sample-scenario.jsonl`.
3. Select JSON as the source type (or the JSON option offered by your Splunk version).
4. In the input settings, set the destination index to `soc_simulation`. Do not rely on the `index` JSON field to route data; index routing is an ingestion setting.
5. Finish the upload. In Search, select **All time** and run:

```spl
index=soc_simulation simulation=true
| stats count by event_type
```

Expected totals: 30 connection_attempt, 17 ssh_auth, 1 process_exec and 1 file_change (49 records total).

6. Verify field extraction and timestamps:

```spl
index=soc_simulation simulation=true
| table _time event_type sourcetype simulation src_ip dest_ip dest_port user auth_result exe path operation
```

The `sourcetype` column above is Splunk metadata. The JSON field called `sourcetype` in the generated records may be represented separately depending on the import configuration. The simulation detections deliberately do not depend on metadata `sourcetype=linux_audit`; they filter on `event_type` instead.

## Run the detections

Open `../splunk/simulation_detections.spl`, copy each D01–D04 search separately, and run it over **All time**.

Expected fixture matches:
- D01: one or more rows showing more than 25 unique ports for the attacker/target pair.
- D02: one success row with 12 preceding failures for the same source, destination and user.
- D03: one www-data shell execution indicator.
- D04: one cron-file modification indicator.

The exact number of D01 rows can vary with Splunk's streamstats output and event ordering. Validate the timestamps and values rather than assuming a fixed row count.

## Important limitations

- These searches are training examples, not production-ready detections.
- D01 and D02 use event-time-ordered `streamstats` time windows; test time-boundary, delayed-event and out-of-order ingestion behavior in your Splunk version.
- D03 and D04 depend on the JSON fields being extracted with the exact names and values shown.
- The generator's JSON `sourcetype` is a data field, not a guarantee about Splunk metadata sourcetype.
- Do not claim that these searches were run in a live Splunk instance until you have imported the data and captured your own results.
