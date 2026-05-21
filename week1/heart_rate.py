"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

def main():
    # Ask the user for their age.
    # Convert the input string to an integer for calculations.
    user_input = input("Please enter your age: ")
    age = int(user_input)

    # Calculate the maximum heart rate.
    # Formula: 220 - age
    max_rate = 220 - age

    # Calculate the target range (65% and 85%).
    # Use float multipliers for the percentages.
    slowest_rate = max_rate * 0.65
    fastest_rate = max_rate * 0.85

    # Display the results for the user.
    # Round the results to the nearest integer.
    print(f"When you exercise to strengthen your heart, you should keep your")
    print(f"heart rate between {slowest_rate:.0f} and {fastest_rate:.0f} beats per minute.")

# Call the main function to run the program
if __name__ == "__main__":
    main()