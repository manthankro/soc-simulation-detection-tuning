# Lab Build and Telemetry Setup Guide

## Scope

The source blueprint specifies Kali Linux, Ubuntu 22.04, and Splunk Enterprise on an isolated `192.168.100.0/24` network. Use snapshots and synthetic credentials. Never expose the intentionally vulnerable target to the public internet.

## 1. Create the virtual network

Assign:
- Kali: `192.168.100.10`
- Ubuntu target: `192.168.100.20`
- Splunk server: `192.168.100.30`

Use host-only networking or an equivalent isolated segment. Confirm only the required lab hosts can communicate.

## 2. Prepare the Ubuntu target

Install only the services required for your exercise (SSH and Apache/DVWA). Configure Auditd and Sysmon for Linux according to their official documentation and your Ubuntu release. Keep the host patched except where a deliberately vulnerable component is required for the lab; isolate that component.

## 3. Configure Splunk inputs

Review `../splunk/inputs.conf`. Create the `os_logs` and `web_logs` indexes in Splunk before forwarding events. Confirm file permissions allow the forwarder to read logs without granting unnecessary privileges.

## 4. Configure forwarding

Review `../splunk/outputs.conf`. Enable the Splunk receiving port on the SIEM only for the isolated lab network. Confirm connectivity and verify events arrive.

## 5. Verify telemetry

Run the preflight searches in [data dictionary](data-dictionary.md). Check timestamp parsing, host naming, sourcetype, and field extraction before enabling detections.

## 6. Record your own results

Use the [validation plan](validation-plan.md). Capture your own screenshots and measured alert metrics. The source guide's example metrics must not be represented as independently reproduced results.
