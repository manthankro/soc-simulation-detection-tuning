# Detection Tuning and Reported Metrics

## Tuning strategies described in the source guide

1. **Lookup-based allowlisting:** use `known_scanners.csv` to identify approved scanner and management hosts. Validate ownership and review allowlist entries periodically.
2. **Threshold and time-window tuning:** the guide contrasts an original threshold of more than 3 failures in 15 minutes with a tuned threshold of more than 15 failures in 2 minutes, with a subsequent successful login within 3 minutes.

## Reported before/after figures

| Metric | Raw / untuned | Tuned | Reported improvement |
|---|---:|---:|---:|
| Total alerts per day | 142 | 8 | 94.3% reduction |
| True positives | 6 attacks | 6 attacks | 100% recall maintained |
| False positives | 136 | 2 | 98.5% FP elimination |
| Rule precision | 4.2% | 75.0% | +70.8 percentage points |

The source guide also describes 85 false alerts per day in its narrative about scanner and automated SSH backup noise. These figures are reproduced as stated and are not independently reconciled or verified here.

## Reproduce your own measurements

For each test run, record:
- test date and duration
- total alerts
- confirmed true positives
- confirmed false positives
- false negatives found during review
- precision = TP / (TP + FP)
- recall = TP / (TP + FN)

Do not present the source guide's figures as your own measured results unless you reproduce them and retain supporting evidence.
