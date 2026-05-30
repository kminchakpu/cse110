"""
Author: Kevin Cross Minchakpu
Course: CSE 111 Programming and Problem Solving
Assignment: Week 5 Code-Along
Instructor: CJ Waisaith
Description: This program reads student data from a CSV file and allows the user to look up 
student names by their ID numbers.
Enhancements: The program includes enhanced input validation to ensure that the ID numbers are 
in the correct format and length."""

import csv


def validate_and_clean_id(raw_id: str) -> str | None:
    """Validates the raw ID string and returns a cleaned, digit-only string.

    Returns None if the ID is invalid.
    """
    # Enhancement: Check for invalid characters (only digits and dashes allowed)
    # Iterate explicitly to avoid using 'any'
    for char in raw_id:
        if not (char.isdigit() or char == "-"):
            print("Invalid ID Number")
            return None

    # Enhancement: Remove dashes from the user input
    cleaned_id: str = raw_id.replace("-", "")

    # Enhancement: Check length constraints (assuming a standard length of 9 digits)
    # Adjust the target length (9) if the specific csv uses a different length
    target_length: int = 9
    if len(cleaned_id) < target_length:
        print("Invalid ID Number: too few digits")
        return None
    elif len(cleaned_id) > target_length:
        print("Invalid ID Number: too many digits")
        return None

    return cleaned_id


def main() -> None:
    # Dictionary to store student data
    students_dict: dict[str, str] = {}

    # Open and read the students.csv file
    try:
        with open("students.csv", mode="r", newline="", encoding="utf-8") as file:
            # Use csv.reader to handle the comma-separated format safely
            csv_reader = csv.reader(file)

            # Skip the header row
            next(csv_reader)

            # Read rows into the dictionary
            for row in csv_reader:
                # Ensure the row has both ID and Name before processing
                if len(row) >= 2:
                    student_id: str = row[0].strip().replace("-", "")
                    student_name: str = row[1].strip()
                    students_dict[student_id] = student_name

    except FileNotFoundError:
        print("Error: The file 'students.csv' was not found.")
        return

    # Creative Enhancement: Wrap the lookup in a loop so the user can look up
    # multiple students without restarting the program. They can type 'quit' to exit.
    print("--- Student Lookup System ---")
    print("Type 'quit' at any time to exit the program.\n")

    while True:
        user_input: str = input("Please enter a student ID number: ").strip()

        # Check for exit condition
        if user_input.lower() == "quit":
            print("Exiting program. Goodbye!")
            break

        # Skip empty inputs gracefully
        if not user_input:
            continue

        # Validate input and remove dashes
        cleaned_id: str | None = validate_and_clean_id(user_input)

        # If validation passed, look up the student in the dictionary
        if cleaned_id is not None:
            if cleaned_id in students_dict:
                print(f"Student Name: {students_dict[cleaned_id]}\n")
            else:
                print("No such student\n")


if __name__ == "__main__":
    main()