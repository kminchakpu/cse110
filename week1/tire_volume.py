# Author: Kevin Cross Minchakpu
# Course: CSE 111 - Block 3
# Institution: Brigham Young University - Idaho
# Instructor: CJ Waisath

"""
Enhancement:
After displaying the volume, the program asks if the user wants
to buy tires with those dimensions. If 'yes', it prompts for
a phone number and saves it to the log file alongside the tire data.
"""

import math
from datetime import datetime


def main() -> None:
    """Calculate tire volume and save data to a log file."""

    # Get user input
    width: float = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio: float = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter: float = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate tire volume
    volume: float = (
        math.pi * width**2 * aspect_ratio
        * (width * aspect_ratio + 2540 * diameter)
    ) / 10_000_000_000

    # Display result
    print(f"\nThe approximate volume is {volume:.2f} liters")

    # Get current date
    current_date: datetime = datetime.now()

    # Ask user if they want to buy tires
    phone_number: str = ""
    wants_to_buy: str = input(
        "Do you want to buy tires with these dimensions? (yes/no): "
    ).lower()

    if wants_to_buy == "yes":
        phone_number = input("Please enter your phone number: ")

    # Append information to volumes.txt
    with open("volumes.txt", "at") as volumes_file:

        # If customer wants to buy tires, include phone number
        if phone_number:
            print(
                f"{current_date:%Y-%m-%d}, "
                f"{width:.0f}, "
                f"{aspect_ratio:.0f}, "
                f"{diameter:.0f}, "
                f"{volume:.2f}, "
                f"{phone_number}",
                file=volumes_file
            )

        # Otherwise, save without phone number
        else:
            print(
                f"{current_date:%Y-%m-%d}, "
                f"{width:.0f}, "
                f"{aspect_ratio:.0f}, "
                f"{diameter:.0f}, "
                f"{volume:.2f}",
                file=volumes_file
            )


if __name__ == "__main__":
    main()