# 09-Phishing-Email-Analysis

## Objective
Analyze a simulated phishing email and identify indicators of phishing and social engineering.

## Tools Used
- Kali Linux
- grep
- nano
- Linux command line

## Analysis Performed
1. Examined the suspicious email.
2. Extracted the embedded URL using grep.
3. Searched for urgency and social-engineering language.
4. Inspected the sender address.
5. Identified a lookalike domain.
6. Documented the phishing indicators.

## Indicators Identified
- Lookalike sender domain: `micros0ft-security.example`
- Suspicious URL: `microsoft-login-security.example/verify`
- Urgent account suspension warning
- Request for immediate verification
- Threat of permanent loss of access

## Assessment
The simulated email contains multiple characteristics commonly associated with phishing attacks, including domain impersonation, urgency, threatening language, and a suspicious verification link.

## Recommended Response
- Do not click suspicious links.
- Do not enter credentials.
- Report the message to the SOC/security team.
- Verify alerts through the organization's official website.
- Investigate and block confirmed malicious indicators.

## Skills Demonstrated
- Phishing analysis
- Indicator identification
- Social-engineering detection
- Linux text analysis
- Security incident documentation
