# Detection Validation Plan

## Preflight: Splunk ingestion

1. Create the `soc_simulation` index before upload.
2. Upload `simulation/sample-scenario.jsonl` with JSON parsing and explicitly choose `soc_simulation` as the destination index.
3. Select **All time**; fixture timestamps are fixed at 2026-01-15 UTC.
4. Confirm 49 events are present and fields are extracted:

```spl
index=soc_simulation simulation=true
| stats count by event_type
```

Expected: 30 connection_attempt, 17 ssh_auth, 1 process_exec, 1 file_change. Total: 49.

Then inspect representative fields with:

```spl
index=soc_simulation simulation=true
| table _time event_type src_ip dest_ip dest_port user auth_result exe path operation
```

Do not require metadata `sourcetype=linux_audit` for this uploaded JSON dataset. The event payload has an `event_type` field; Splunk metadata sourcetype is controlled by the upload configuration.

## Detection test matrix

| ID | Test | Expected result |
|---|---|---|
| V01 | 30 unique ports within the same 120-second window | D01 detects more than 25 unique ports |
| V02 | 25 or fewer unique ports | D01 does not alert |
| V03 | 11 SSH failures then a success within 300 seconds for same source/destination/user | D02 alerts on the success |
| V04 | 11 SSH failures with no subsequent success | D02 does not alert |
| V05 | Success occurs before the failures | D02 does not alert on that earlier success |
| V06 | Failures are outside the preceding 300-second window | D02 does not alert |
| V07 | www-data executes /bin/bash or /bin/sh | D03 alerts |
| V08 | Other user executes a shell | D03 does not alert |
| V09 | Cron path is modified | D04 alerts |
| V10 | Non-cron path is modified | D04 does not alert |
| V11 | Missing source IP or destination port | D01 handles null fields safely |
| V12 | Delayed or out-of-order event arrival | Document the effect of event-time sorting and search-window limits |

## Evidence capture

For each test, save:
- test ID and date/time (UTC)
- Splunk search and time range
- raw event sample with secrets removed
- expected vs actual result
- analyst disposition
- query version / commit SHA
- screenshots with environment details redacted

## Acceptance criteria

Do not mark a rule production-ready until positive and negative tests pass in the target Splunk version, field extraction and timestamp parsing are verified, data dependencies are documented, and the operational owner signs off.

The repository's Python tests check fixture content and query safeguards; they do not run SPL. A passing GitHub Actions workflow is not evidence of live Splunk execution.
