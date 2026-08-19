import re
import getpass

print("=" * 55)
print("PASSWORD STRENGTH & SECURITY CHECKER")
print("Cybersecurity Portfolio - Project 2")
print("=" * 55)

print("\nEnter a password to check its strength.")
password = getpass.getpass("Password: ")

# Check password requirements
has_length = len(password) >= 12
has_uppercase = bool(re.search(r"[A-Z]", password))
has_lowercase = bool(re.search(r"[a-z]", password))
has_number = bool(re.search(r"[0-9]", password))
has_special = bool(re.search(r"[^A-Za-z0-9]", password))

# Common weak passwords
common_passwords = [
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "abc123",
    "letmein",
    "admin",
    "welcome",
    "iloveyou"
]

print("\nSecurity checks:")
print(f"12 or more characters: {'PASS' if has_length else 'FAIL'}")
print(f"Uppercase letter:       {'PASS' if has_uppercase else 'FAIL'}")
print(f"Lowercase letter:       {'PASS' if has_lowercase else 'FAIL'}")
print(f"Number:                 {'PASS' if has_number else 'FAIL'}")
print(f"Special character:      {'PASS' if has_special else 'FAIL'}")

# Calculate password score
score = sum([
    has_length,
    has_uppercase,
    has_lowercase,
    has_number,
    has_special
])

print(f"\nSecurity score: {score}/5")

# Calculate strength
if password.lower() in common_passwords:
    strength = "WEAK"
elif score <= 2:
    strength = "WEAK"
elif score <= 4:
    strength = "MEDIUM"
else:
    strength = "STRONG"

print(f"Password strength: {strength}")

# Common password warning
if password.lower() in common_passwords:
    print("\nWARNING: This is a commonly used password.")
    print("Choose a more unique password.")

# Recommendations
print("\nRecommendations:")

if not has_length:
    print("- Use at least 12 characters.")

if not has_uppercase:
    print("- Add at least one uppercase letter.")

if not has_lowercase:
    print("- Add at least one lowercase letter.")

if not has_number:
    print("- Add at least one number.")

if not has_special:
    print("- Add at least one special character.")

if password.lower() in common_passwords:
    print("- Avoid commonly used passwords.")

if score == 5 and password.lower() not in common_passwords:
    print("- Your password meets all security requirements.")

print("\n" + "=" * 55)
print("Password check complete.")
print("=" * 55)