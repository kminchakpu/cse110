# Author: Kevin Cross Minchakpu
# Course: CSE 111 - Block 3
# Institution: Brigham Young University - Idaho
# Instructor: CJ Waisath

"""
This program calculates the fuel efficiency of a vehicle in miles per gallon and liters per 100 kilometers based on user input for odometer readings and fuel used.
Enhancement: Added a function to calculate the fuel efficiency in liters per 100 kilometers.
The program now also includes a function to convert miles per gallon to liters per 100 kilometers, and displays both results to the user.
"""

def main():
    # Get an odometer value in U.S. miles from the user.
    start_miles: float = float(input("Enter the starting odometer reading (miles): "))
    
    # Get another odometer value in U.S. miles from the user.
    end_miles: float = float(input("Enter the ending odometer reading (miles): "))
    
    # Get a fuel amount in U.S. gallons from the user.
    amount_gallons: float = float(input("Enter the amount of fuel used (gallons): "))

    # Call the miles_per_gallon function and store the result in a variable named mpg.
    mpg: float = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Call the lp100k_from_mpg function to convert the miles per gallon to 
    # liters per 100 kilometers and store the result in a variable named lp100k.
    lp100k: float = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")

def miles_per_gallon(start_miles: float, end_miles: float, amount_gallons: float) -> float:
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    """
    mpg: float = (end_miles - start_miles) / amount_gallons
    return mpg

def lp100k_from_mpg(mpg: float) -> float:
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    """
    lp100k: float = 235.215 / mpg
    return lp100k

# Call the main function so that this program will start executing.
if __name__ == "__main__":
    main()