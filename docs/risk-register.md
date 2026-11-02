# Lab Risk Register

| Risk | Impact | Mitigation | Evidence |
|---|---|---|---|
| Vulnerable target exposed outside lab | Unauthorized compromise | Host-only isolated network; verify routes | Network settings screenshot |
| Test credentials reused elsewhere | Account compromise | Unique disposable credentials | Credential handling checklist |
| Reverse-shell exercise escapes intended boundary | Host/network compromise | Use isolated snapshots and strict egress controls; do not adapt payloads for external hosts | Firewall/network validation |
| Splunk receiver exposed broadly | Data leakage / abuse | Restrict receiver to lab subnet | Firewall rule |
| Allowlist suppresses real behavior | Missed detection | Owner, scope, expiry, periodic review | Lookup review log |
| Unverified metrics published as personal results | Portfolio credibility loss | Label source figures and collect reproducible evidence | Validation report |
| Sensitive logs committed publicly | Privacy/security exposure | Sanitize IPs, usernames, tokens, hostnames | Pre-commit review |

## Stop conditions

Stop the exercise if a VM obtains an unexpected route to a public/production network, unexpected systems receive traffic, credentials are exposed, or activity is not clearly attributable to the authorized lab.
