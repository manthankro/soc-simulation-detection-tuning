#!/usr/bin/env python3
"""Generate deterministic, synthetic SOC telemetry for Splunk demonstrations.

Safe by design: no sockets, scanning, authentication, shell execution, exploitation,
or host modification. All records are fabricated training data.
"""
import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE = datetime(2026, 1, 15, 14, 0, 0, tzinfo=timezone.utc)
ATTACKER = "192.168.100.10"
TARGET = "192.168.100.20"


def event(seconds, **fields):
    return {
        "_time": (BASE + timedelta(seconds=seconds)).isoformat(),
        "host": "ubuntu-target-01",
        "index": "os_logs",
        "simulation": True,
        "source": "synthetic-training-data",
        **fields,
    }


def build_scenario():
    rows = []
    # Reconnaissance-like network telemetry: 30 unique destination ports.
    for port in range(20, 50):
        rows.append(event(
            port, sourcetype="lab_network", event_type="connection_attempt",
            src_ip=ATTACKER, dest_ip=TARGET, dest_port=port, action="denied",
            scenario_id="SOC-CASE-001", phase="reconnaissance",
        ))
    # SSH failures followed by a successful login in the same short window.
    for i in range(12):
        rows.append(event(
            180 + i * 5, sourcetype="syslog", event_type="ssh_auth",
            src_ip=ATTACKER, dest_ip=TARGET, user="lab-admin",
            auth_result="failure", scenario_id="SOC-CASE-001", phase="credential-access",
        ))
    rows.append(event(
        250, sourcetype="syslog", event_type="ssh_auth", src_ip=ATTACKER,
        dest_ip=TARGET, user="lab-admin", auth_result="success",
        scenario_id="SOC-CASE-001", phase="initial-access",
    ))
    # Suspicious process execution telemetry, represented as records, not executed.
    rows.append(event(
        360, sourcetype="linux_audit", event_type="process_exec",
        user="www-data", uid=33, exe="/bin/bash", parent_exe="/usr/sbin/apache2",
        ppid=712, command_line="/bin/bash -c [SYNTHETIC_TEST_ARGUMENTS]",
        scenario_id="SOC-CASE-001", phase="execution",
    ))
    # Cron modification indicator, also represented as data only.
    rows.append(event(
        480, sourcetype="linux_audit", event_type="file_change",
        user="www-data", path="/var/spool/cron/crontabs/www-data",
        operation="modified", scenario_id="SOC-CASE-001", phase="persistence",
    ))
    # Benign examples for analyst tuning / false-positive discussion.
    for i in range(4):
        rows.append(event(
            900 + i * 60, sourcetype="syslog", event_type="ssh_auth",
            src_ip="192.168.100.5", dest_ip=TARGET, user="ops-user",
            auth_result="failure", scenario_id="BENIGN-OPS-001", phase="maintenance",
        ))
    return sorted(rows, key=lambda row: row["_time"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="simulation/sample-scenario.jsonl")
    args = parser.parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = build_scenario()
    output.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
    print(f"Wrote {len(rows)} synthetic records to {output}")
    print("Training data only: no network or host activity was performed.")


if __name__ == "__main__":
    main()
