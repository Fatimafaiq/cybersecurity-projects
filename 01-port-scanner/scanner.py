import socket

target = input("Enter target IP: ")

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print("\n--- PORT SCANNER ---")
print(f"Target: {target}")
print(f"Scanning ports {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)


    result = sock.connect_ex((target, port))

if result == 0:
    try:
        service = socket.getservbyport(port, "tcp")
    except OSError:
        service = "Unknown"

    print(f"Port {port} is OPEN - Service: {service}")

    sock.close()