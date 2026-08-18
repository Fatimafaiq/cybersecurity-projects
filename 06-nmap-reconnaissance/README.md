# Nmap Network Reconnaissance Lab

## Objective

The objective of this project is to perform network reconnaissance against an intentionally vulnerable Metasploitable 2 virtual machine using Nmap from Kali Linux.

The lab demonstrates host discovery, port scanning, service and version detection, operating system detection, and Nmap Scripting Engine enumeration.

## Lab Environment

- Attacker Machine: Kali Linux
- Kali IP: 192.168.1.66
- Target Machine: Metasploitable 2
- Target IP: 192.168.1.68
- Platform: VirtualBox
- Tool: Nmap

## Reconnaissance Methodology

### 1. Connectivity Test

Before scanning, connectivity between Kali Linux and the target was verified.

```bash
ping -c 4 192.168.1.68

## Security Findings

The reconnaissance identified a large attack surface with 23 open TCP ports and several legacy services.

### Key Findings

| Port | Service | Detected Software | Security Observation |
|------|---------|-------------------|----------------------|
| 21 | FTP | vsftpd 2.3.4 | Legacy FTP service exposed |
| 22 | SSH | OpenSSH 4.7p1 | Remote administration service exposed |
| 23 | Telnet | Linux telnetd | Telnet transmits traffic without modern encryption |
| 80 | HTTP | Apache 2.2.8 | Legacy web server detected |
| 139/445 | SMB | Samba 3.0.20 | SMB services exposed; message signing reported disabled |
| 1524 | Bind Shell | Metasploitable root shell | Highly sensitive remote shell service exposed |
| 3306 | MySQL | MySQL 5.0.51a | Database service accessible over the network |
| 5432 | PostgreSQL | PostgreSQL 8.3.x | Database service exposed |
| 5900 | VNC | VNC | Remote desktop service exposed |
| 6667 | IRC | UnrealIRCd | IRC service detected |
| 8180 | HTTP | Apache Tomcat 5.5 | Legacy application server detected |

### OS Identification

Nmap fingerprinting identified the target as a Linux system using a 2.6-series kernel.

### SMB Observation

Nmap NSE reported that SMB message signing was disabled. This represents a security-relevant configuration weakness because message signing can help protect SMB communications against certain tampering and relay scenarios.

### Overall Assessment

The Metasploitable 2 host presents a deliberately large and insecure attack surface. Multiple legacy network services, remote administration interfaces, database services, and web services are accessible from the network.

These findings demonstrate how reconnaissance can be used to identify services that should be investigated further during an authorized vulnerability assessment.
