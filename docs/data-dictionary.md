# Telemetry Data Dictionary

Field availability depends on Splunk add-ons, parsing, OS version, and configuration. Treat this as a validation checklist, not a guarantee.

| Field | Meaning | Example source |
|---|---|---|
| `_time` | Event timestamp | Parsed event timestamp |
| `host` | Reporting endpoint | Universal Forwarder metadata |
| `src_ip` | Source IP address | Network event or extracted auth message |
| `dest_ip` | Destination IP address | Network event |
| `dest_port` | Destination port | Network event |
| `user` | Account name | SSH, syslog, Auditd |
| `uid` | Numeric user ID | Auditd |
| `exe` | Executed binary | Auditd |
| `ppid` | Parent process ID | Auditd / Sysmon mapping |
| `a0`, `a1` | Argument fields when parsed that way | Auditd EXECVE |
| `sourcetype` | Splunk event format label | Splunk metadata |

## Preflight searches

```spl
| tstats count where index=* by index sourcetype host
```

```spl
index=os_logs
| stats count values(sourcetype) as sourcetypes by host
```

```spl
index=os_logs sourcetype=linux_audit
| head 20
| table _time host type exe uid ppid a0 a1
```

If a field is absent, inspect raw events and configure parsing before relying on it in an alert.
