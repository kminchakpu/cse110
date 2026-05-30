"""
Author: Kevin Cross Minchakpu
Course: CSE 111 Programming with functions
Instructor: CJ Waisaith
Description: This program reads a list of provinces from a file, 
modifies the list by removing certain elements and replacing occurrences 
of "AB" with "Alberta", and counts the number of occurrences of "Alberta" in the modified list.
"""

def main() -> None:
    # Open the provinces.txt file and read contents into a list
    try:
        with open("provinces.txt", "r") as file:
            # Read lines and strip newline characters
            provinces_list: list[str] = [line.strip() for line in file]
    except FileNotFoundError:
        print("Error: The file 'provinces.txt' was not found.")
        return

    # Print the entire list
    print("Original List:")
    print(provinces_list)
    print("-" * 40)

    # Remove the first element from the list
    if len(provinces_list) > 0:
        provinces_list.pop(0)

    # Remove the last element from the list
    if len(provinces_list) > 0:
        provinces_list.pop()

    # Replace all occurrences of "AB" with "Alberta"
    # Using a list comprehension to rebuild the list with replacements
    provinces_list = [
        "Alberta" if province == "AB" else province 
        for province in provinces_list
    ]

    # Alternative approach without list comprehension:
    # for i in range(len(provinces_list)):
    #     if provinces_list[i] == "AB":
    #         provinces_list[i] = "Alberta"

    print("Modified List:")
    print(provinces_list)
    print("-" * 40)

    # Count the number of elements that are "Alberta" and print it
    alberta_count: int = provinces_list.count("Alberta")
    print(f"Number of occurrences of 'Alberta': {alberta_count}")


if __name__ == "__main__":
    main()