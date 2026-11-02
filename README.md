# End-to-End SOC Simulation & Detection Rule Tuning

> Enterprise-grade cyber defense lab | Portfolio project for Detection Engineer / SOC Analyst L2

This repository documents an isolated, three-VM SOC lab based on the supplied **End-to-End SOC Simulation & Detection Rule Tuning** guide. It covers telemetry collection, a four-stage attack lifecycle, Splunk detections, false-positive tuning, and incident handling.

## Lab at a glance

| Role | Platform | Address | Key components |
|---|---|---:|---|
| Attacker | Kali Linux | `192.168.100.10` | Nmap, Hydra, Metasploit, Netcat |
| Target | Ubuntu 22.04 | `192.168.100.20` | Apache2, DVWA, SSH, Sysmon for Linux, Auditd, Universal Forwarder |
| SIEM | Splunk Enterprise 9.x | `192.168.100.30` | Receiver `:9997`, Web `:8000`, SPL detections |

Network: isolated hypervisor segment `192.168.100.0/24`.

## Attack lifecycle represented

1. Network reconnaissance — Nmap port and service discovery.
2. SSH authentication attack — failed logins followed by a successful login.
3. Web command injection / shell execution — Apache/DVWA process telemetry.
4. Persistence — cron task modification.

**Safety:** Only reproduce attack activity inside an isolated lab that you own or are explicitly authorized to test. The included Python utility is a harmless event-data generator; it does not scan, authenticate to, exploit, or connect to any host.

## Repository map

```text
.
├── README.md
├── docs/
│   ├── network-topology.md
│   ├── incident-timeline.md
│   ├── incident-response-playbook.md
│   └── tuning-metrics.md
├── splunk/
│   ├── detection_rules.spl
│   ├── inputs.conf
│   ├── outputs.conf
│   └── lookups/
│       └── known_scanners.csv
└── attack-scripts/
    ├── generate_sample_events.py
    └── README.md
```

## Telemetry pipeline

The Ubuntu target forwards:
- `/var/log/auth.log` as `syslog` into `os_logs`
- Apache access logs as `access_combined` into `web_logs`
- Apache error logs as `apache_error` into `web_logs`
- Auditd logs as `linux_audit` into `os_logs`

See [Splunk inputs](splunk/inputs.conf) and [outputs](splunk/outputs.conf).

## Detection coverage

| Rule | Detection objective | Source |
|---|---|---|
| 1 | High-volume port scan | Network / OS telemetry |
| 2 | SSH brute-force followed by success | `auth.log` |
| 3 | Web process spawning shell / reverse-shell-like command | Auditd EXECVE/SYSCALL |
| 4 | Cron-based persistence indicators | Syslog / CRON |

Queries are provided in [detection_rules.spl](splunk/detection_rules.spl). Review the tuning notes before treating any query as production-ready.

## Tuning results reported by the guide

| Metric | Raw | Tuned | Reported improvement |
|---|---:|---:|---:|
| Alerts/day | 142 | 8 | 94.3% reduction |
| True positives | 6 | 6 | 100% recall maintained |
| False positives | 136 | 2 | 98.5% FP elimination |
| Precision | 4.2% | 75.0% | +70.8 percentage points |

These are **figures stated in the source guide**, not independently reproduced benchmark results. See [tuning metrics](docs/tuning-metrics.md).

## Incident handling

Use the [incident response playbook](docs/incident-response-playbook.md) to validate alerts, preserve evidence, scope affected systems, contain the lab target, eradicate persistence, and document recovery.

## Validation notes and limitations

The source guide describes time-windowed logic, but some of its sample SPL snippets do not fully implement those constraints:
- Rule 1's prose says a two-minute rolling window; the sample query does not bucket or constrain events to that window.
- Rule 2's prose says failures and success must correlate within five minutes; the sample aggregation does not enforce event ordering or a five-minute span.
- The sample port-scan search uses broad index/sourcetype syntax; validate field extraction and parenthesize base-search logic for your Splunk environment.
- Confirm Auditd field mappings (`exe`, `a0`, `uid`, `ppid`) against actual events before enabling Rule 3.

The repository labels the supplied logic as a starting point rather than claiming it is tested production content. Tune against representative lab data and document measured results.

## Getting started

1. Build the isolated three-VM network described in [network topology](docs/network-topology.md).
2. Install and configure Splunk Enterprise and the Universal Forwarder.
3. Confirm telemetry arrives in the expected indexes and sourcetypes.
4. Load the lookup CSV and validate field names.
5. Test each SPL detection against known benign and simulated lab events.
6. Record alert counts, true positives, false positives, and precision in your own test run.


## Complete project documentation

- [Lab build guide](docs/lab-build-guide.md)
- [Network topology](docs/network-topology.md)
- [Attack scenario matrix](docs/attack-scenario-matrix.md)
- [Detection engineering methodology](docs/detection-engineering-methodology.md)
- [Telemetry data dictionary](docs/data-dictionary.md)
- [Detection validation plan](docs/validation-plan.md)
- [Incident timeline example](docs/incident-timeline.md)
- [Incident response playbook](docs/incident-response-playbook.md)
- [Tuning metrics](docs/tuning-metrics.md)
- [Risk register](docs/risk-register.md)
- [Evidence log template](docs/evidence-log-template.md)
- [Metrics report template](docs/metrics-report-template.md)
- [Portfolio evidence checklist](docs/portfolio-evidence-checklist.md)

## Engineering quality

The repository also includes:
- A synthetic event generator that performs no network activity.
- A Python test and GitHub Actions workflow for basic safety/format validation.
- Security policy, contribution guidance, and ignore rules for local evidence and secrets.

## Roadmap to a standout portfolio

The repository is a structured project framework. To make it a credible demonstration of hands-on skill, complete the lab and add your own sanitized evidence:
1. Build the three VMs and prove isolation.
2. Verify ingestion and field extraction in Splunk.
3. Execute only authorized lab test cases and capture raw telemetry.
4. Validate D01–D04 against positive and benign cases.
5. Calculate metrics from your actual test dataset.
6. Add screenshots, a topology image, and an incident report.
7. Record a short walkthrough explaining one detection from raw event to triage.

See the [portfolio evidence checklist](docs/portfolio-evidence-checklist.md). Do not describe planned tests, illustrative timestamps, or source-guide metrics as personally completed measurements.


## Reproducible demonstration lab

A deterministic synthetic dataset generator is available in [simulation/](simulation/). It creates a multi-stage scenario and benign comparison events without performing network activity or executing attacks. Import the generated JSONL into a dedicated Splunk index and use [simulation detections](splunk/simulation_detections.spl).

- [Generate and import the scenario](simulation/README.md)
- [Build a Splunk dashboard](docs/splunk-dashboard-guide.md)
- [Interview walkthrough script](docs/interview-demo-script.md)
- [Incident case study template](docs/case-study-template.md)
- [Evidence directory guidance](evidence/README.md)

**Evidence integrity:** the included scenario is synthetic training data. Replace templates with screenshots and measurements from your own lab before claiming hands-on execution.

## Disclaimer

This project is for education, defensive security engineering, and authorized lab use only. Do not run attack techniques against public, third-party, or production systems without explicit written authorization.
