"""
Author: Kevin Cross Minchakpu
Instructor: CJ Waisaith
Course: CSE 111 Programming with functions

Description:
This program reads product information from a CSV file and processes a request for items, 
printing the details of the requested items based on the product information. 
The program uses a compound dictionary to store product data and handles CSV files using the csv 
module for robust parsing.
"""

import csv
import pprint

def read_dictionary(filename, key_column_index):
    """
    Read the contents of a CSV file into a compound dictionary and return it.
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    Return: a compound dictionary.
    """
    products_dict = {}
    
    # Open the CSV file for reading
    with open(filename, "rt") as csv_file:
        # Use csv.reader to handle commas and rows properly
        reader = csv.reader(csv_file)
        
        # Skip the header row if the products.csv contains one
        next(reader)
        
        for row in reader:
            if len(row) > 0:
                # Use the specified column index as the dictionary key
                key = row[key_column_index]
                # Store the entire row list as the value
                products_dict[key] = row
                
    return products_dict

def main():
    # Call read_dictionary and store the result
    # Index 0 is the product number (key)
    products_dict = read_dictionary("products.csv", 0)
    
    # Print the product dictionary (required for milestone)
    print("Products Dictionary:")
    pprint.pprint(products_dict)
    print()
    
    print("--- Requested Items ---")
    # Open the request.csv file for reading
    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        
        # Skip the first line containing headings
        next(reader)
        
        # Loop through and process each row in request.csv
        for row in reader:
            if len(row) > 0:
                product_number = row[0]
                requested_quantity = int(row[1])
                
                # Find the item in products_dict
                product_info = products_dict[product_number]
                
                # Extract details (Name is at index 1, Price is at index 2)
                product_name = product_info[1]
                product_price = float(product_info[2])
                
                # Print the requested details
                print(f"{product_name}: {requested_quantity} @ {product_price}")

# Protect the call to main
if __name__ == "__main__":
    main()