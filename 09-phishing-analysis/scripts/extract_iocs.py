import re
from pathlib import Path


def extract_iocs(text):
    urls = sorted(set(re.findall(r'https?://[^\s<>"\']+', text)))
    emails = sorted(set(re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)))
    ipv4 = sorted(set(re.findall(
        r'\b(?:25[0-5]|2[0-4]\d|1?\d?\d)'
        r'(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3}\b',
        text
    )))
    domains = sorted(set(re.findall(
        r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b',
        text
    )))

    return urls, emails, ipv4, domains


evidence_dir = Path("../evidence")

files = [
    evidence_dir / "suspicious_email.txt",
    evidence_dir / "email_headers.txt",
]

combined_text = ""

for file_path in files:
    if file_path.exists():
        combined_text += file_path.read_text(errors="ignore") + "\n"

urls, emails, ipv4, domains = extract_iocs(combined_text)

print("=== PHISHING IOC EXTRACTION ===\n")

print("URLs:")
for item in urls:
    print(f"  {item}")

print("\nEmail Addresses:")
for item in emails:
    print(f"  {item}")

print("\nIPv4 Addresses:")
for item in ipv4:
    print(f"  {item}")

print("\nDomains:")
for item in domains:
    print(f"  {item}")
