# Example Correlated Incident Timeline

The timestamps below are the illustrative UTC timeline from the source guide, not timestamps from a live execution.

| UTC time | Phase | Observed telemetry / activity | Example alert | Severity |
|---|---|---|---|---|
| 14:00:12–14:01:05 | Reconnaissance | 250 connection drops across ports 1–1024 | Network Recon – Port Scan | LOW |
| 14:05:22–14:07:10 | Brute force | 18 SSH failures from `192.168.100.10` | SSH Brute-Force Attempt | MEDIUM |
| 14:07:18 | Compromise | SSH login accepted for `admin` | SSH Brute-Force Success | HIGH |
| 14:12:45 | Execution | `www-data` spawned `/bin/bash` with a TCP redirect | Reverse Shell Execution | CRITICAL |
| 14:15:00 | Persistence | Cron job appended with outbound connection behavior | Cron Task Persistence | CRITICAL |

## Analyst correlation checklist

- Normalize timestamps and confirm clock synchronization across VMs.
- Pivot on source IP, target host, username, parent process, and process arguments.
- Confirm whether the SSH success follows the failures in the same correlation window.
- Review Apache access logs and Auditd process events around the web execution alert.
- Inspect cron changes and identify the modifying user/process.
- Preserve raw events and record the exact search time range used.
