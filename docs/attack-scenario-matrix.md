# Attack Scenario and Detection Matrix

This matrix translates the source guide's four-stage lab into observable defensive hypotheses. It is a lab exercise plan, not a claim that each event has already been executed.

| Scenario | ATT&CK tactic (reference mapping) | Expected telemetry | Detection | Analyst validation |
|---|---|---|---|---|
| Port and service discovery | Reconnaissance / Discovery | Firewall or flow records, network connection events | D01 high unique destination-port count | Confirm source, target, time window, scanner allowlist |
| SSH password guessing | Credential Access | `/var/log/auth.log` | D02 repeated SSH failures | Review username diversity, source reputation within lab, success sequence |
| Web process launches shell | Execution | Auditd EXECVE/SYSCALL, Sysmon for Linux, Apache logs | D03 suspicious child process / shell arguments | Confirm parent process, UID, command arguments, web request correlation |
| Cron task change | Persistence | Syslog CRON, Auditd file/process events | D04 cron modification indicator | Inspect crontab owner, changed file, command destination, change authorization |

## ATT&CK mapping notes

Mappings are intentionally high-level and should be refined to the exact technique IDs only after validating the telemetry and behavior observed in your own lab. Do not claim technique coverage solely because a tool or command appears in a scenario.
