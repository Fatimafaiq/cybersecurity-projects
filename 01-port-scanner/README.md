# Port Scanner

A beginner Python TCP port scanner built to understand sockets, TCP connections, ports, service lookup, and basic network reconnaissance.

## Features

- User-defined target IP
- User-defined port range
- TCP connection testing
- Open-port detection
- Basic service lookup
- Open-port counter
- Scan duration

## Technologies Used

- Python
- socket
- time

## How It Works

The scanner asks the user for:

1. A target IP address
2. A starting port
3. An ending port

It then attempts a TCP connection to each port using Python's `socket` library.

If `connect_ex()` returns `0`, the TCP connection succeeded and the port is reported as open.

## Example

```text
Enter target IP: 127.0.0.1
Enter start port: 7995
Enter end port: 8000

--- PORT SCANNER ---
Target: 127.0.0.1
Scanning ports 7995 to 8000...

Port 8000 is OPEN - Service: Unknown

--- SCAN COMPLETE ---
Open ports found: 1