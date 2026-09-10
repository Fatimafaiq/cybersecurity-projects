# Project 09 - Phishing Email Analysis & Detection

## Overview

This project demonstrates a SOC-style investigation of a simulated phishing email. The investigation focuses on identifying social-engineering indicators, analyzing email authentication results, extracting Indicators of Compromise (IOCs), and creating a detection rule.

All domains, IP addresses, and email data used in this project are synthetic and intended only for cybersecurity training.

---

## Objectives

- Identify phishing and social-engineering indicators
- Analyze suspicious sender and lookalike domains
- Examine email headers
- Evaluate SPF, DKIM, and DMARC results
- Extract URLs, domains, email addresses, and IP addresses
- Automate IOC extraction using Python
- Create a phishing detection rule
- Map the activity to MITRE ATT&CK
- Document appropriate SOC response actions

---

## Tools & Technologies

- Kali Linux
- Git / GitHub
- Linux command-line utilities
- grep
- Python 3
- Regular Expressions
- Sigma-style detection rules

---

## Project Structure

```text
09-phishing-analysis/
├── README.md
├── analysis/
│   ├── findings.txt
│   └── header-analysis.txt
├── evidence/
│   ├── suspicious_email.txt
│   └── email_headers.txt
├── scripts/
│   └── extract_iocs.py
└── detection/
    └── phishing-detection-rule.yml
```

---

## 1. Initial Email Analysis

The simulated email was reviewed for common phishing characteristics.

Indicators identified included:

- Urgent account-verification language
- Brand impersonation
- Suspicious sender information
- Lookalike domain
- Social-engineering techniques
- Suspicious URL/domain indicators

The lookalike domain uses:

```text
micros0ft-support.example
```

The number `0` is used in place of the letter `o` in an attempt to visually resemble a trusted brand.

---

## 2. Email Header Analysis

The email headers were analyzed to evaluate sender authenticity and message routing.

### Authentication Results

| Control | Result |
|---|---|
| SPF | FAIL |
| DKIM | NONE |
| DMARC | FAIL |

These results reduce confidence in the claimed sender identity.

Additional analysis included:

- From address
- Return-Path
- Message-ID
- Received header
- Sending host
- Source IP address

The source IP used in this laboratory scenario is:

```text
192.0.2.55
```

This is a documentation address used only for the simulated investigation.

---

## 3. IOC Extraction

Indicators of Compromise were identified from the email evidence.

The investigation extracted:

- URLs
- Email addresses
- Domains
- IPv4 addresses

Basic command-line extraction was performed using tools such as `grep`.

A Python script was then created to automate IOC extraction:

```text
scripts/extract_iocs.py
```

The script parses the evidence files and identifies common IOC types using regular expressions.

---

## 4. Detection Engineering

A Sigma-style detection rule was created:

```text
detection/phishing-detection-rule.yml
```

The rule looks for characteristics associated with the simulated campaign, including:

- Lookalike sender domain
- Urgent subject language
- Account-verification terminology

This demonstrates how investigation findings can be converted into detection logic.

---

## 5. MITRE ATT&CK Mapping

The simulated activity maps to:

**T1566 - Phishing**

**T1566.002 - Spearphishing Link**

Tactic:

```text
Initial Access
```

The scenario demonstrates how phishing can be used as an initial-access technique through social engineering and malicious-link delivery.

---

## 6. SOC Assessment

### Classification

**Phishing**

### Severity

**High**

### Key Findings

The email contained multiple indicators consistent with phishing:

- Lookalike domain
- Brand impersonation
- SPF failure
- No DKIM authentication
- DMARC failure
- Urgency-based social engineering
- Account-verification pretext

---

## 7. Recommended SOC Response

If similar indicators were observed in a real environment, appropriate actions could include:

1. Quarantine the suspicious email.
2. Identify other recipients of the campaign.
3. Search email and security telemetry for matching indicators.
4. Validate domains, URLs, and IP addresses using approved threat-intelligence sources.
5. Block confirmed malicious indicators where appropriate.
6. Determine whether users clicked links or submitted credentials.
7. Reset affected credentials if compromise is confirmed.
8. Escalate according to the organization's incident-response procedure.
9. Document findings and preserve relevant evidence.

---

## Skills Demonstrated

- Phishing analysis
- Email header analysis
- SPF / DKIM / DMARC interpretation
- Social-engineering analysis
- IOC extraction
- Python scripting
- Regular expressions
- Detection engineering
- Sigma rule creation
- MITRE ATT&CK mapping
- SOC investigation methodology
- Incident-response documentation

---

## Disclaimer

This project was completed in a controlled training environment for educational and defensive cybersecurity purposes. All suspicious indicators used in the laboratory are synthetic examples and do not represent an active phishing campaign.
