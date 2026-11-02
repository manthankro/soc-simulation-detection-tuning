#!/usr/bin/env python3
"""Generate harmless synthetic SOC event records for local demos.

This script does not open sockets, scan hosts, authenticate, exploit services,
execute shell commands, or modify persistence settings.
"""
import argparse
import json
from datetime import datetime, timezone, timedelta


def build_events():
    base = datetime.now(timezone.utc)
    samples = [
        ("network_recon", "192.168.100.10", "192.168.100.20", "scanner", "LOW"),
        ("ssh_failed", "192.168.100.10", "192.168.100.20", "admin", "MEDIUM"),
        ("ssh_success", "192.168.100.10", "192.168.100.20", "admin", "HIGH"),
        ("web_shell_indicator", "192.168.100.20", "192.168.100.10", "www-data", "CRITICAL"),
        ("cron_persistence_indicator", "192.168.100.20", "192.168.100.10", "www-data", "CRITICAL"),
    ]
    for offset, (event, src, dest, user, severity) in enumerate(samples):
        yield {
            "timestamp": (base + timedelta(seconds=offset * 30)).isoformat(),
            "event_type": event,
            "src_ip": src,
            "dest_ip": dest,
            "user": user,
            "severity": severity,
            "simulation": True,
            "note": "Synthetic training record; not collected from a real host.",
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="sample-events.jsonl")
    args = parser.parse_args()
    with open(args.output, "w", encoding="utf-8") as handle:
        for event in build_events():
            handle.write(json.dumps(event) + "\n")
    print(f"Wrote synthetic events to {args.output}")


if __name__ == "__main__":
    main()
