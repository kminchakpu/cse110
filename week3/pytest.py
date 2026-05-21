"""
Enhancement: After displaying the volume, the program asks if the user wants 
to buy tires with those dimensions. If 'yes', it prompts for a phone number 
and saves it to the log file alongside the tire data.
"""
import math
from datetime import datetime

def compute_tire_volume(width: float, aspect_ratio: float, diameter: float) -> float:
    """
    Calculates and returns the volume of space inside a tire.
    Formula: v = (pi * w^2 * a * (w * a + 2540 * d)) / 10,000,000 [cite: 23]
    """
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10_000_000_000 
    return volume

def main() -> None:
    # 1. Get user input for tire dimensions 
    width = float(input("Enter the width of the tire in mm (ex 205): ")) 
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): ")) 
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): ")) 

    # 2. Calculate the volume using the logic-only function 
    volume = compute_tire_volume(width, aspect_ratio, diameter)

    # 3. Display the result rounded to two decimal places 
    print(f"\nThe approximate volume is {volume:.2f} liters")

    # 4. Get the current date (Do NOT include time) 
    current_date = datetime.now()
    
    # --- Enhancement (Exceeding Requirements) ---
    phone_number = ""
    wants_to_buy = input("Do you want to buy tires with these dimensions? (yes/no): ").lower() 
    if wants_to_buy == "yes":
        phone_number = input("Please enter your phone number: ") 

    # 5. Append information to volumes.txt 
    # Format: date, width, aspect_ratio, diameter, volume, [optional phone]
    with open("volumes.txt", "at") as volumes_file:
        if phone_number:
            # Logs include the phone number if provided 
            print(f"{current_date:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}, {phone_number}", 
                  file=volumes_file) 
        else:
            print(f"{current_date:%Y-%m-%d}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}", 
                  file=volumes_file) 

if __name__ == "__main__":
    main()