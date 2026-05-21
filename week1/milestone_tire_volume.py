"""
Enhancement: After displaying the volume, the program asks if the user wants 
to buy tires with those dimensions. If 'yes', it prompts for a phone number 
and saves it to the log file alongside the tire data.
"""
import math
from datetime import datetime

def main() -> None:
    # Get user input for tire dimensions
    width: float = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio: float = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter: float = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate the volume in liters using the provided formula
    # Formula: v = (pi * w^2 * a * (w * a + 2540 * d)) / 10,000,000
    volume: float = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10_000_000

    # Display the result rounded to two decimal places
    print(f"\nThe approximate volume is {volume:.2f} liters")


if __name__ == "__main__":
    main()