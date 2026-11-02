# Incident Response Playbook

Use this checklist for alerts generated inside the authorized lab.

## 1. Validate and triage
- [ ] Confirm alert time range, index, sourcetype, and field extraction.
- [ ] Identify source IP, target host, username, process, parent process, and command arguments.
- [ ] Check whether the source is listed in the approved scanner/management lookup.
- [ ] Compare activity with the lab exercise schedule.

## 2. Scope the activity
- [ ] Pivot from reconnaissance to authentication events.
- [ ] Correlate SSH failures with any later successful login.
- [ ] Review Apache access/error logs around suspected command injection.
- [ ] Inspect Auditd process execution and parent-child relationships.
- [ ] Review cron modifications and scheduled task execution.

## 3. Contain the lab
- [ ] Isolate the affected VM using the hypervisor network controls.
- [ ] Stop the controlled test exercise and preserve relevant VM snapshots.
- [ ] Disable test accounts or credentials if required.
- [ ] Do not delete evidence before collection.

## 4. Eradicate and recover
- [ ] Remove unauthorized lab cron entries after evidence capture.
- [ ] Revert the target VM to a known-good snapshot where appropriate.
- [ ] Rotate any credentials used during the exercise.
- [ ] Confirm forwarding and endpoint telemetry resume after recovery.

## 5. Document and improve
- [ ] Record event IDs, timestamps, searches, and evidence locations.
- [ ] Classify true/false positives and explain each decision.
- [ ] Tune thresholds or lookup entries with an owner and review date.
- [ ] Re-test detections against both attack simulation and benign activity.
