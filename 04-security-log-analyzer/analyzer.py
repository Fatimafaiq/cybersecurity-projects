from collections import defaultdict

log_file = "04-security-log-analyzer/security.log"

failed_attempts = defaultdict(int)
successful_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "LOGIN_FAILED" in line:
            parts = line.split("ip=")

            if len(parts) == 2:
                ip_address = parts[1].strip()
                failed_attempts[ip_address] += 1

        if "LOGIN_SUCCESS" in line:
            parts = line.split("ip=")

            if len(parts) == 2:
                ip_address = parts[1].strip()
                successful_attempts[ip_address] += 1

print("\n--- FAILED LOGIN SUMMARY ---")

for ip, count in failed_attempts.items():
    print(f"{ip}: {count} failed attempt(s)")

print("\n--- SECURITY ALERTS ---")

for ip, count in failed_attempts.items():
    if count >= 4:
        print(f"ALERT: Possible brute-force attack from {ip}")
        print(f"Failed login attempts: {count}")

print("\n--- RISK CLASSIFICATION ---")

for ip, count in failed_attempts.items():

    if count >= 6:
        risk = "HIGH"

    elif count >= 4:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    print(f"{ip}: {risk} RISK")

print("\n--- SUCCESSFUL LOGIN SUMMARY ---")

for ip, count in successful_attempts.items():
    print(f"{ip}: {count} successful login(s)")

print("\n--- SUSPICIOUS SUCCESSFUL LOGINS ---")

for ip, success_count in successful_attempts.items():
    failed_count = failed_attempts.get(ip, 0)

    if failed_count >= 3 and success_count >= 1:
        print(f"ALERT: Suspicious successful login from {ip}")
        print(f"Previous failed attempts: {failed_count}")
        print(f"Successful logins: {success_count}")

print("\n--- SECURITY ANALYSIS COMPLETE ---")

total_failed = sum(failed_attempts.values())
total_successful = sum(successful_attempts.values())

print(f"Total failed logins: {total_failed}")
print(f"Total successful logins: {total_successful}")
print(f"Unique IPs with failed attempts: {len(failed_attempts)}")
print(f"Unique IPs with successful logins: {len(successful_attempts)}")