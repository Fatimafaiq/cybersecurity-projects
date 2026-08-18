from collections import defaultdict

traffic_file = "05-network-traffic-analyzer/sample_traffic.txt"

ports_by_source = defaultdict(set)

suspicious_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet"
}

with open(traffic_file, "r") as file:
    for line in file:
        parts = line.strip().split()

        src_ip = parts[2].split("=")[1]
        dst_ip = parts[3].split("=")[1]
        protocol = parts[4].split("=")[1]
        port = int(parts[5].split("=")[1])

        ports_by_source[src_ip].add(port)

        print(f"Source: {src_ip}")
        print(f"Destination: {dst_ip}")
        print(f"Protocol: {protocol}")
        print(f"Port: {port}")

        if port in suspicious_ports:
            service = suspicious_ports[port]
            print(
                f"WARNING: Connection to monitored port "
                f"{port} ({service}) from {src_ip}"
            )

        print("-" * 30)

print("\n--- PORT SCAN DETECTION ---")

for ip, ports in ports_by_source.items():
    if len(ports) >= 5:
        print(f"ALERT: Possible port scan detected from {ip}")
        print(f"Ports accessed: {sorted(ports)}")

print("\n--- TRAFFIC SUMMARY ---")

total_sources = len(ports_by_source)
total_connections = sum(len(ports) for ports in ports_by_source.values())

print(f"Unique source IPs: {total_sources}")
print(f"Unique source-port connections: {total_connections}")