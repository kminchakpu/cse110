"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python
program named boxes.py that asks the user for two integers:  1) the
number of manufactured items and 2) the number of items that the user
will pack per box. Your program must compute and print the number of
boxes necessary to hold the items. This must be a whole number. Note
that the last box may be packed with fewer items than the other boxes.
"""

import math

def main() -> None:
    # Get input from the user and convert to integers
    num_items: int = int(input("Enter the number of items: "))
    items_per_box: int = int(input("Enter the number of items per box: "))

    # Calculate the number of boxes
    # math.ceil() rounds the result up to the nearest integer
    num_boxes: int = math.ceil(num_items / items_per_box)

    # Display a blank line.
    print()

    # Display the results
    print(f"For {num_items} items, packing {items_per_box} items in each box, "
          f"you will need {num_boxes} boxes.")

if __name__ == "__main__":
    main()