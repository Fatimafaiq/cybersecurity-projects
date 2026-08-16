# File Integrity Monitor

A Python-based cybersecurity project that monitors files for unauthorized changes using SHA-256 hashing.

## Overview

This project demonstrates the concept of File Integrity Monitoring (FIM). It creates a baseline SHA-256 hash for files in a monitored directory and continuously checks the files for changes.

The program can detect when a file is:

- Modified
- Deleted
- Newly created

## Features

- Generates SHA-256 hashes for files
- Creates a baseline of monitored files
- Continuously monitors a directory
- Detects modified files
- Detects deleted files
- Detects newly created files
- Displays old and new hashes when modifications occur

## Technologies Used

- Python
- hashlib
- os
- time
- SHA-256

## Project Structure

02-file-integrity-monitor/
- monitor.py
- test-files/
  - config.txt
  - suspicious.txt
- README.md

## How It Works

1. The program scans the `test-files` directory.
2. A SHA-256 hash is generated for each file.
3. These hashes are stored as the baseline.
4. The directory is checked every two seconds.
5. Current hashes are compared with the baseline.
6. The program generates an alert when a file is modified, deleted, or created.

## Example Output

[MODIFIED] config.txt
Old hash: ...
New hash: ...

[NEW FILE] suspicious.txt
Hash: ...

[DELETED] users.txt

## Cybersecurity Relevance

File Integrity Monitoring is used in cybersecurity to detect unauthorized changes to important files. Unexpected modifications may indicate malware activity, configuration tampering, privilege abuse, or unauthorized access.

## Skills Demonstrated

- Python scripting
- File handling
- SHA-256 hashing
- File integrity monitoring
- Change detection
- Cybersecurity monitoring concepts