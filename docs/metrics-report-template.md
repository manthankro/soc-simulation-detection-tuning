# Detection Evaluation Report

> Template — replace every placeholder with results from a reproducible test run.

## Evaluation scope

- Evaluation period:
- Dataset / scenario IDs:
- Query version:
- Splunk version:
- Environment:
- Exclusions and allowlists:

## Confusion matrix

| | Predicted positive | Predicted negative |
|---|---:|---:|
| Actual positive | TP: [value] | FN: [value] |
| Actual negative | FP: [value] | TN: [value] |

## Metrics

- Precision = TP / (TP + FP): [value]
- Recall = TP / (TP + FN): [value]
- False-positive rate = FP / (FP + TN): [value]
- Alerts per day: [value]
- Baseline-to-tuned alert reduction: [value]

## Interpretation

Describe what improved, what was missed, the impact of exclusions, and remaining limitations. Include evidence links and do not infer performance from a tiny or unrepresentative sample.
