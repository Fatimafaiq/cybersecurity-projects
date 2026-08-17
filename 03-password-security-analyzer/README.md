# Password Security Analyzer

A Python-based cybersecurity tool that analyzes password strength and provides security recommendations.

## Overview

This project evaluates a password using several security criteria and assigns it a strength rating.

The analyzer checks password complexity as well as potentially unsafe password patterns.

## Features

- Checks password length
- Checks for uppercase letters
- Checks for lowercase letters
- Checks for numbers
- Checks for special characters
- Detects commonly used passwords
- Detects repeated characters
- Calculates a password security score
- Classifies passwords as WEAK, MODERATE, or STRONG
- Provides recommendations for improving password security

## Security Checks

The analyzer evaluates whether a password contains:

- At least 12 characters
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Appropriate password complexity

Additional security checks detect:

- Common passwords such as `password123`
- Characters repeated three or more times

## Example

Input:

    CyberShield#2026

Output:

    --- PASSWORD SECURITY ANALYSIS ---
    score: 6/6
    Strength: STRONG

    Recommendations:
    - Your password meets all security checks.

Another example:

Input:

    Password1111!

Output:

    --- PASSWORD SECURITY ANALYSIS ---
    score: 6/6
    Strength: MODERATE

    Recommendations:
    - WARNING: Avoid repeating the same character 3 or more times.

## How to Run

Make sure Python is installed.

From the repository root, run:

    python 03-password-security-analyzer/analyzer.py

Then enter a password when prompted.

## Technologies Used

- Python
- String analysis
- Conditional logic
- Password security concepts

## Cybersecurity Concepts Demonstrated

This project demonstrates:

- Password complexity analysis
- Password policy enforcement
- Weak password detection
- Pattern-based password analysis
- Credential security awareness

## Disclaimer

This project is intended for educational and cybersecurity learning purposes. Do not enter real passwords or credentials into demonstration or testing tools.