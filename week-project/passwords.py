# Author: Kevin Cross Minchakpu
# Course: CSE 111 - Block 3
# Institution: Brigham Young University - Idaho
# Instructor: CJ Waisath

"""This program evaluates the strength of a password based on various criteria, including dictionary checks, length, and character complexity. It provides feedback to the user on the strength of their password and allows them to check multiple passwords until they choose to quit.

Enhancement: Added a keyboard pattern check. This function detects if a 
password contains common sequential keyboard rows (like 'qwerty' or 'asdf'), 
which are often used as weak passwords but might not be in the dictionary 
or top-password files. This adds an additional layer of security evaluation, as many users choose passwords based on keyboard patterns that are easy to guess. The function checks for these patterns in a case-insensitive manner and can be easily expanded to include more patterns as needed.
"""

import math

# Constants for character lists
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", "`", "~"]

def word_in_file(word: str, filename: str, case_sensitive: bool = False) -> bool:
    """Reads a file and checks if a word matches a line in that file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if case_sensitive:
                    if word == clean_line:
                        return True
                else:
                    if word.lower() == clean_line.lower():
                        return True
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    return False

def has_keyboard_pattern(word: str) -> bool:
    """Checks for common sequential keyboard patterns."""
    patterns = ["qwerty", "asdfgh", "zxcvbn", "123456"]
    word_low = word.lower()
    for pattern in patterns:
        if pattern in word_low:
            return True
    return False

def word_has_character(word: str, character_list: list[str]) -> bool:
    """Checks if any character in the word is present in the character_list."""
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word: str) -> int:
    """Calculates complexity (0-4) based on types of characters used."""
    complexity: int = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password: str, min_length: int = 10, strong_length: int = 16) -> int:
    """Evaluates password strength (0-5) based on security requirements."""
    
    # Check for keyboard patterns (Enhancement)
    if has_keyboard_pattern(password):
        print("Password contains a common keyboard pattern and is not secure.")
        return 0

    #Check Dictionary File (Case Insensitive)
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    #Check Top Passwords File (Case Sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    #Check Length Requirements
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    #Complexity Scoring
    complexity_score: int = word_complexity(password)
    strength: int = 1 + complexity_score
    return strength

def main():
    """Provides the user input loop for checking passwords."""
    while True:
        user_input: str = input("Enter a password to check (or 'q' to quit): ")
        if user_input.lower() == "q":
            break
            
        strength: int = password_strength(user_input)
        print(f"Password Strength: {strength}")
        print("-" * 20)

if __name__ == "__main__":
    main()