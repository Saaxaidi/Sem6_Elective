import re

def password_strength(password):
    score = 0
    reasons = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        reasons.append("Password too short (less than 8 characters).")

    # Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        reasons.append("No uppercase letter.")

    # Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        reasons.append("No lowercase letter.")

    # Numbers
    if re.search(r'\d', password):
        score += 1
    else:
        reasons.append("No number.")

    # Special characters
    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        reasons.append("No special character (@$!%*?&).")

    # Common patterns
    common_patterns = ["123", "password", "qwerty", "abc"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score = max(score - 2, 0)  # Penalize common patterns
        reasons.append("Contains common pattern (e.g., 123, password).")

    # Strength evaluation
    if score >= 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, reasons


# Test common passwords
common_passwords = [
    "password",
    "12345678",
    "P@ssw0rd",
    "qwerty123",
    "Admin@123",
    "letmein",
    "abc123!"
]

for pwd in common_passwords:
    strength, reasons = password_strength(pwd)
    print(f"Password: {pwd}\nStrength: {strength}")
    if reasons:
        print("Notes:")
        for r in reasons:
            print(f" - {r}")
    print("-" * 40)
