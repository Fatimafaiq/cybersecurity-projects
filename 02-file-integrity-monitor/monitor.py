import hashlib
import os
import time


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def create_baseline(folder_path):
    baseline = {}

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            baseline[filename] = calculate_hash(file_path)

    return baseline


folder_path = "02-file-integrity-monitor/test-files"

baseline_hashes = create_baseline(folder_path)

print("\n--- FILE INTEGRITY MONITOR ---")
print(f"Monitoring folder: {folder_path}")
print(f"Baseline created for {len(baseline_hashes)} file(s).")

for filename, file_hash in baseline_hashes.items():
    print(f"{filename}: {file_hash}")

print("\nMonitoring started. Press Ctrl+C to stop.\n")


while True:
    time.sleep(2)

    current_hashes = create_baseline(folder_path)

    # Detect newly created files
    for filename in current_hashes:
        if filename not in baseline_hashes:
            print(f"\n[NEW FILE] {filename}")
            print(f"Hash: {current_hashes[filename]}")

    # Detect deleted files
    for filename in baseline_hashes:
        if filename not in current_hashes:
            print(f"\n[DELETED] {filename}")

    # Detect modified files
    for filename in current_hashes:
        if filename in baseline_hashes:
            if current_hashes[filename] != baseline_hashes[filename]:
                print(f"\n[MODIFIED] {filename}")
                print(f"Old hash: {baseline_hashes[filename]}")
                print(f"New hash: {current_hashes[filename]}")

    # Update the baseline after checking
    baseline_hashes = current_hashes