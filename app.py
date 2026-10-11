import getpass
import string


def check_password_strength(password):
    checks = {
        "At least 8 characters": len(password) >= 8,
        "Uppercase letter (A-Z)": any(c.isupper() for c in password),
        "Lowercase letter (a-z)": any(c.islower() for c in password),
        "Number (0-9)": any(c.isdigit() for c in password),
        "Special character": any(c in string.punctuation for c in password),
    }

    score = sum(checks.values())

    print("\n--- Password Strength Report ---")

    for rule, passed in checks.items():
        status = "Passed" if passed else "Missing"
        print(f"{rule}: {status}")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print(f"\nPassword Strength: {strength}")

    if score < 5:
        print("Suggestions to improve your password:")
        for rule, passed in checks.items():
            if not passed:
                print(f"- Add: {rule}")

    return strength


if __name__ == "__main__":
    password = getpass.getpass("Enter a password to check: ")
    check_password_strength(password)