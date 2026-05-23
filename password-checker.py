import re

COMMON_PASSWORDS = ["123456", "password", "admin", "qwerty", "12345678"]


def check_strength(password):
    score = 0
    feedback = []

    # length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")

    # uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    # special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    # common password check
    if password in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a commonly used password (very weak)")

    return score, feedback


def simulate_breach(password):
    leaked_db = ["123456", "admin123", "password", "welcome", "qwerty"]

    if password in leaked_db:
        return True
    return False


def main():
    password = input("Enter password to check: ")

    score, feedback = check_strength(password)

    print("\n--- PASSWORD ANALYSIS ---")

    if score >= 4:
        print("Strength: STRONG")
    elif score == 3:
        print("Strength: MODERATE")
    else:
        print("Strength: WEAK")

    print(f"Score: {score}/5")

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print("-", f)

    print("\n--- BREACH CHECK ---")

    if simulate_breach(password):
        print("WARNING: Password found in leaked database!")
    else:
        print("Good news: Not found in breach database")


if __name__ == "__main__":
    main()