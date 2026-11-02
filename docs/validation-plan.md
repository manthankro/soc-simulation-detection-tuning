# Detection Validation Plan

## Test matrix

| ID | Test | Expected result | Evidence |
|---|---|---|---|
| V01 | More than 25 unique destination ports inside configured window | D01 alerts | Search export with event range |
| V02 | Authorized scanner in lookup | D01 excludes it | Lookup match and excluded event |
| V03 | Repeated SSH failures without success | D02 behavior matches documented threshold | Auth event sample and search output |
| V04 | Repeated failures plus success in correlation window | D02 alerts | Ordered event timeline |
| V05 | Benign admin shell activity | D03 reviewed / tuned appropriately | Process tree and analyst disposition |
| V06 | Web service account launches suspicious shell pattern | D03 alerts | Auditd event and correlated Apache request |
| V07 | Normal cron maintenance | D04 reviewed without blind allowlisting | Cron event and owner/change ticket |
| V08 | Unexpected cron modification | D04 alerts | Auditd/syslog evidence |
| V09 | Missing source IP or destination port | Search handles nulls safely | Null-field test event |
| V10 | Delayed or out-of-order event arrival | Correlation limitations documented | Ingestion and event timestamps |

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

Do not mark a rule production-ready until positive tests alert, negative tests are reviewed, data dependencies are documented, and the operational owner signs off.
