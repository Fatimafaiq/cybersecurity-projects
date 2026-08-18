# Network Traffic Analyzer

A Python-based network traffic analysis tool designed to parse simulated network traffic logs and identify potentially suspicious network activity.

## Features

- Parses network traffic log entries
- Extracts source and destination IP addresses
- Identifies TCP and UDP traffic
- Extracts destination port numbers
- Tracks ports accessed by each source IP
- Detects possible port scanning activity
- Monitors security-sensitive ports
- Generates a network traffic summary

## Security Detection

The analyzer can identify a potential port scan when a single source IP attempts to access multiple different ports.

Example:

```text
--- PORT SCAN DETECTION ---
ALERT: Possible port scan detected from 192.168.1.50
Ports accessed: [21, 22, 23, 25, 80, 443]
```

## Monitored Services

The analyzer can monitor common network services such as:

| Port | Service |
|------|---------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |

## Traffic Summary

The program provides a summary of the analyzed network activity.

Example:

```text
--- TRAFFIC SUMMARY ---
Unique source IPs: 4
Unique source-port connections: 9
```

## Project Structure

```text
05-network-traffic-analyzer/
├── analyzer.py
├── traffic.log
└── README.md
```

## How to Run

From the main repository directory:

```bash
python ./05-network-traffic-analyzer/analyzer.py
```

On Windows PowerShell:

```powershell
python .\05-network-traffic-analyzer\analyzer.py
```

## Cybersecurity Concepts Demonstrated

- Network traffic analysis
- TCP/IP fundamentals
- Port and service identification
- Log parsing
- Port scan detection
- Network security monitoring
- Basic intrusion detection concepts
- Security event analysis

## Disclaimer

This project uses simulated network traffic and is intended for educational and cybersecurity learning purposes.