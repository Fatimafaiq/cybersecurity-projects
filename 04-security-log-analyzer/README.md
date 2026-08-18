# Security Log Analyzer

A Python-based security log analysis tool that detects suspicious authentication activity, failed login attempts, and potential brute-force attacks.

## Features

- Parses authentication events from a security log
- Counts failed login attempts by IP address
- Counts successful login attempts by IP address
- Detects potential brute-force attacks
- Assigns risk levels to suspicious IP addresses
- Detects successful logins following repeated failed attempts
- Generates an overall security analysis summary

## Security Concepts Demonstrated

- Log analysis
- Authentication monitoring
- Brute-force attack detection
- Rule-based threat detection
- Risk classification
- Security event correlation
- Basic SIEM concepts

## Project Structure

```text
04-security-log-analyzer/
├── analyzer.py
├── security.log
└── README.md