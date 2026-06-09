"""
Author: Kevin Cross Minchakpu
Purpose: W06 Checkpoint: Using Objects
Description: Modifies a list of fruits using various object methods like 
             reverse, append, insert, remove, pop, sort, and clear.
"""

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    #Add code to reverse and print fruit_list.
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    #Add code to append "orange" to the end of fruit_list and print the list.
    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")

    #Add code to find where "apple" is located in fruit_list and
    #insert "cherry" before "apple" in the list and print the list.
    apple_index = fruit_list.index("apple")
    fruit_list.insert(apple_index, "cherry")
    print(f"insert cherry: {fruit_list}")

    #Add code to remove "banana" from fruit list and print the list.
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")

    #Add code to pop the last element from fruit_list and print the popped element and the list.
    popped_fruit = fruit_list.pop()
    print(f"popped element: {popped_fruit}")
    print(f"after pop: {fruit_list}")

    #Add code to sort and print fruit_list.
    fruit_list.sort()
    print(f"sorted: {fruit_list}")

    #Add code to clear and print fruit_list.
    fruit_list.clear()
    print(f"cleared: {fruit_list}")

if __name__ == "__main__":
    main()