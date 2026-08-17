import string 

common_passwords = [
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "abc123",
    "admin",
    "letmein",
    "welcome",
    "iloveyou"
]

def has_repeated_characters(password):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True

    return False

password = input("Enter a password to analyze: ")

score = 0

if len(password) >= 12:
    score += 2
elif len(password) >= 8:
    score += 1

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

print("\n--- PASSWORD SECURITY ANALYSIS ---")
print(f"score: {score}/6")

if password.lower() in common_passwords:
    print("Strength: WEAK")
elif has_repeated_characters(password):
    print("Strength: MODERATE")
elif score <= 2:
    print("Strength: WEAK")
elif score <= 4:
    print("Strength: MODERATE")
else:
    print("Strength: STRONG")

print("\nRecommendations:")

if len(password) < 12:
    print("- Use at least 12 characters.")

if not has_upper:
    print("- Add an uppercase letter.")

if not has_lower:
    print("- Add a lowercase letter.")

if not has_digit:
    print("- Add a number.")

if not has_special:
    print("- Add a special character.")

if (
    score == 6
    and password.lower() not in common_passwords
    and not has_repeated_characters(password)
):
    print("- Your password meets all security checks.")

if password.lower() in common_passwords:
    print("- WARNING: This is a commonly used password.")
    print("- Choose a more unique password.")

if has_repeated_characters(password):
    print("- WARNING: Avoid repeating the same character 3 or more times.")