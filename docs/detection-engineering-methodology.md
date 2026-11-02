# Detection Engineering Methodology

## Lifecycle

1. **Define the hypothesis:** state the adversary behavior, required data, expected fields, and exclusions.
2. **Check data quality:** verify event arrival, timestamps, host identity, sourcetype, field extraction, and retention.
3. **Write a baseline query:** begin with transparent event selection and aggregation.
4. **Validate positive cases:** replay or generate known test events in the isolated lab.
5. **Validate negative cases:** include ordinary admin activity, scanner activity, failed parsing, and missing fields.
6. **Tune carefully:** thresholds and allowlists must have a documented owner, rationale, scope, and expiry/review date.
7. **Measure:** report TP, FP, FN, precision, recall, and alert volume from a defined test period.
8. **Operationalize:** document severity, triage steps, response actions, and dependencies.
9. **Regression test:** rerun known positive and negative cases after every meaningful change.

## Detection quality gates

- Required fields are populated for representative events.
- Search time range and correlation window are explicit.
- Query does not silently discard events due to null fields.
- Allowlist behavior is tested and bounded.
- Positive and negative test cases are retained.
- Query cost and schedule are understood before production deployment.
- Owner, version, review date, and rollback plan are documented.

## Metric definitions

- TP: malicious test cases correctly alerted.
- FP: benign test cases incorrectly alerted.
- FN: malicious test cases missed.
- Precision = TP / (TP + FP).
- Recall = TP / (TP + FN).
- False-positive rate = FP / (FP + TN), when true negatives are defined.
- Alert reduction = (baseline alerts - tuned alerts) / baseline alerts.

Always publish the evaluation dataset, test window, and counting method with metrics.
