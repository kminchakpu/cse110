# Author: Kevin Cross Minchakpu
# Course: CSE 111 - Block 3
# Institution: Brigham Young University - Idaho
# Instructor: CJ Waisath

"""This module provides functions to evaluate the strength of passwords based on various criteria, including character types and complexity. It also includes a user input loop for testing password strength interactively."""

# Constants for character lists defined by Sven
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", "`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    #Checks if a word exists in a specified file.
    pass

def word_has_character(word, character_list):
    #Checks if a word contains any characters from a specific list."""
    pass

def word_complexity(word):
    #Calculates a complexity value (0-4) based on character types.
    pass

def password_strength(password, min_length=10, strong_length=16):
    #Evaluates password strength based on length, lists, and complexity.
    pass

def main():
    #Provides the user input loop and reports results.
    # Milestone requirement: get password and print it back
    user_password = input("Please enter a password (or 'q' to quit): ")
    
    if user_password.lower() != "q":
        print(f"Password entered: {user_password}")

# Standard block to start program execution
if __name__ == "__main__":
    main()