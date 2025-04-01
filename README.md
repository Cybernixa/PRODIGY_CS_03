**Password Strength Checker**

This Python script is designed to assess the strength of a password by analyzing various factors that contribute to password security. The script evaluates the password based on several checks, such as length, character variety, inclusion of numbers, and special characters. It also flags common and weak passwords. The password is assigned a score from 0 to 100 and is categorized into a strength level: Very Strong, Strong, Moderate, Weak, or Very Weak.

Key Features:
Password Length: Passwords of at least 8 characters are considered, with higher scores for longer passwords.

Character Variety: A password must contain both uppercase and lowercase letters, numbers, and special characters to score higher.

Common Password Check: The script checks if the password is part of a list of common weak passwords (e.g., "password", "123456").

Entropy Bonus: Passwords with high character variety (many unique characters) get an additional score bonus.

Visual Feedback: The tool provides a visual strength meter to help users easily understand the strength of their password.

Strength Scoring
The strength of the password is determined by several criteria:

Length: Longer passwords are scored higher, with a minimum length of 8 characters required.

Character Variety:

Uppercase and lowercase letters: Passwords with both uppercase and lowercase characters score higher.

Numbers: Inclusion of numeric digits adds to the score.

Special characters: The use of characters like !@#$%^&*() increases password strength.

Common Password Check: Passwords that match common weak passwords (like "password" or "123456") are flagged as very weak.

Entropy Bonus: The script rewards passwords with high entropy (many unique characters) with additional points.

Strength Categories:
Very Strong: Score 80-100

Strong: Score 60-79

Moderate: Score 40-59

Weak: Score 20-39

Very Weak: Score 0-19

How It Works:
The assess_password_strength function checks multiple aspects of the password, calculating a score based on length, character variety, and other factors.

The score is then used to assign a strength category, and detailed feedback is provided to the user about their password's strengths and weaknesses.

A visual representation of the password's strength is displayed using a "strength meter" with filled blocks (▓) and empty blocks (░).

The program runs in a loop where users can enter different passwords to assess their strength. To quit, they simply type quit.

Example Output:
For a password Password123!, the output might look like:

sql
Copy
Password Strength Checker

Enter a password to check (or 'quit' to exit): Password123!

Password Strength: Strong (75/100)

Detailed Feedback:
 - ✓ Good length (12+ characters)
 - ✓ Contains both uppercase and lowercase letters
 - ✓ Contains numbers
 - ✓ Contains special characters
 - ✓ Good character variety

Strength Meter:
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░]
For a weak password like password, the output would be:

markdown
Copy
Password Strength: Very Weak (10/100)

Detailed Feedback:
 - ✗ Too short (minimum 8 characters required)
 - ✗ Missing letters
 - ✗ Missing numbers
 - ✗ Missing special characters
 - ✗ This is an extremely common and weak password

Strength Meter:
[░░░░░░░░░░░░░░░░░░░░░░░░░░]
Code Structure:
assess_password_strength(password):

Takes a password as input and returns a dictionary with the score, strength level, and feedback.

It checks the password for length, character variety (uppercase, lowercase, digits, special characters), and flags common weak passwords.

display_password_strength(password):

Displays the password strength category, score, detailed feedback, and visual strength meter.

Error Handling:
The script handles invalid password input, such as passwords that are too short or too weak.

Common weak passwords are flagged and receive a score of 0.

The visual strength meter updates dynamically based on the score.

Installation Instructions:
Clone or Download the Repository:

You can clone this repository using the following Git command:

bash
Copy
git clone https://github.com/Cybernixa/password-strength-checker.git
Or, download the script directly from the repository.

Install Dependencies:

This script uses Python 3 and requires the re module for regular expressions (which is included by default in Python's standard library). No additional installations are required.

Run the Script:

Open a terminal, navigate to the folder where the script is located, and run:

bash
Copy
python password_strength_checker.py
Input Passwords:

The script will prompt you to input a password. After entering a password, you will see the strength evaluation.

Type quit to exit the program.


Contribution:
Contributions are welcome! If you find bugs, have suggestions for improvements, or want to add more features (such as more common password checks or password history), feel free to submit a pull request.

