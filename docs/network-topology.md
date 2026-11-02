# Virtual Lab Network Topology

The source guide specifies three virtual machines on an isolated hypervisor network: `192.168.100.0/24`.

```text
                 ISOLATED VIRTUAL NETWORK
                      192.168.100.0/24

  RED TEAM                 VICTIM ENDPOINT             BLUE TEAM
  Kali Linux               Ubuntu 22.04               Splunk Enterprise 9.x
  192.168.100.10  ------>  192.168.100.20  --------->  192.168.100.30
  Nmap / Hydra             Apache2 + DVWA              Receiver TCP/9997
  Netcat listener          SSH                         Web UI TCP/8000
  Test scripts             Sysmon for Linux            Detection rules
                           Auditd
                           Splunk Universal Forwarder
```

## Node responsibilities

| Node | Responsibilities |
|---|---|
| Kali | Generate authorized test activity from the isolated attacker VM. |
| Ubuntu | Host the web/SSH services and collect endpoint telemetry. |
| Splunk | Receive, index, correlate, and alert on endpoint and network events. |

## Network and safety controls

- Use a host-only or otherwise isolated virtual network.
- Do not bridge the vulnerable target to a public or production network.
- Use disposable snapshots and test credentials.
- Restrict Splunk receiver access to the lab segment.
- Keep test data and credentials synthetic.

## Forwarding path

Ubuntu Universal Forwarder monitors authentication, Apache, and Auditd logs and sends events to `192.168.100.30:9997`. Splunk Web is listed at `192.168.100.30:8000` in the source guide.
