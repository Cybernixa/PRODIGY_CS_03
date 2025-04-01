import re

def assess_password_strength(password):
    """
    Assesses the strength of a password based on multiple criteria.
    Returns a strength score (0-100) and detailed feedback.
    """
    feedback = []
    score = 0
    
    # Length check
    length = len(password)
    if length >= 12:
        score += 30
        feedback.append("✓ Good length (12+ characters)")
    elif length >= 8:
        score += 20
        feedback.append("✓ Minimum length (8+ characters)")
    else:
        feedback.append("✗ Too short (minimum 8 characters required)")
    
    # Character variety checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    if has_upper and has_lower:
        score += 20
        feedback.append("✓ Contains both uppercase and lowercase letters")
    elif has_upper or has_lower:
        score += 10
        feedback.append("✓ Contains letters (but needs both cases)")
    else:
        feedback.append("✗ Missing letters")
    
    if has_digit:
        score += 15
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Missing numbers")
    
    if has_special:
        score += 15
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Missing special characters")
    
    # Common password check (simplified)
    common_passwords = ["password", "123456", "qwerty", "letmein"]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("✗ This is an extremely common and weak password")
    
    # Entropy bonus (simplified)
    unique_chars = len(set(password))
    if unique_chars >= 8 and length >= 8:
        score += 20
        feedback.append("✓ Good character variety")
    
    # Cap score at 100
    score = min(score, 100)
    
    # Determine strength level
    if score >= 80:
        strength = "Very Strong"
    elif score >= 60:
        strength = "Strong"
    elif score >= 40:
        strength = "Moderate"
    elif score >= 20:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

def display_password_strength(password):
    """Displays the password strength assessment results"""
    assessment = assess_password_strength(password)
    
    print(f"\nPassword Strength: {assessment['strength']} ({assessment['score']}/100)")
    print("\nDetailed Feedback:")
    for item in assessment['feedback']:  # Fixed the quotation mark here
        print(f" - {item}")
    
    # Visual strength indicator
    print("\nStrength Meter:")
    filled = "▓" * (assessment['score'] // 5)
    empty = "░" * (20 - (assessment['score'] // 5))
    print(f"[{filled}{empty}]")

# Example usage
if __name__ == "__main__":
    print("Password Strength Checker")
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break
        display_password_strength(password)
