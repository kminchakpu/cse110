"""
Author: Kevin Cross Minchakpu
Instructor: CJ Waisaith
Course: CSE 111 Programming with functions
Project: W05 Project: Grocery Store Receipt

Enhancements implemented to exceed requirements:
1. Calculates and prints a "Return by" date exactly 30 days in the future at 9:00 PM.
2. Dynamically generates a coupon at the bottom of the receipt for one of the items 
   the customer actually purchased today.
"""

import csv
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):
    """
    Read the contents of a CSV file into a compound dictionary and return it.
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    Return: a compound dictionary.
    """
    products_dict = {}
    
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader) # Skip header row
        
        for row in reader:
            if len(row) > 0:
                key = row[key_column_index]
                products_dict[key] = row
                
    return products_dict

def main():
    # Define constant variables
    SALES_TAX_RATE = 0.06
    STORE_NAME = "Cornerstone Provisions"
    
    # Initialize trackers
    total_items = 0
    subtotal = 0.0
    purchased_item_names = [] # Tracked for dynamic coupon generation
    
    try:
        # Load product catalog dictionary
        products_dict = read_dictionary("products.csv", 0)
        
        # Print Store Receipt Header
        print("=" * 40)
        print(f"{STORE_NAME:^40}")
        print("=" * 40)
        
        # Open and process the customer request file
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader) # Skip the header
            
            # Print itemized list
            for row in reader:
                if len(row) > 0:
                    product_number = row[0]
                    requested_quantity = int(row[1])
                    
                    # Key lookup (triggers KeyError if product number doesn't exist)
                    product_info = products_dict[product_number]
                    
                    product_name = product_info[1]
                    product_price = float(product_info[2])
                    
                    # Track item name for enhancement coupon
                    purchased_item_names.append(product_name)
                    
                    # Calculate math per item row
                    item_total_price = product_price * requested_quantity
                    subtotal += item_total_price
                    total_items += requested_quantity
                    
                    # Print current row receipt details
                    print(f"{product_name:<22} {requested_quantity:>2}  ${product_price:>6.2f}")
            
        print("-" * 40)
        
        # Calculate totals
        sales_tax_amount = subtotal * SALES_TAX_RATE
        total_amount_due = subtotal + sales_tax_amount
        
        # Display summary details
        print(f"Number of Items: {total_items}")
        print(f"Subtotal:        ${subtotal:>6.2f}")
        print(f"Sales Tax (6%):  ${sales_tax_amount:>6.2f}")
        print(f"Total Due:       ${total_amount_due:>6.2f}")
        print("-" * 40)
        
        print("Thank you for shopping with us!")
        
        # Get and print current date and time
        current_dt = datetime.now()
        print(f"{current_dt:%a %b %d %H:%M:%S %Y}")
        print("-" * 40)
        
        # --- EXCEEDING REQUIREMENTS: ENHANCEMENTS ---
        # Return policy text (30 days out at 9:00 PM)
        return_date = current_dt + timedelta(days=30)
        # Combine calculated date with standard 9:00 PM time
        return_deadline = datetime(return_date.year, return_date.month, return_date.day, 21, 0, 0)
        print(f"Return Policy: Items can be returned by\n{return_deadline:%b %d, %Y at %I:%M %p}")
        print("-" * 40)
        
        # Dynamic Coupon Generator
        if purchased_item_names:
            # Pick the first item they bought to guarantee they like it!
            coupon_item = purchased_item_names[0]
            print(f"*** BONUS COUPON FOR YOUR NEXT VISIT ***")
            print(f"Save 15% on your next purchase of:")
            print(f"--> {coupon_item} <--")
            print("=" * 40)

    except FileNotFoundError as file_err:
        print("\nError: Missing data file.")
        print(file_err)
    except PermissionError as perm_err:
        print("\nError: System lacks permissions to access the required data files.")
        print(perm_err)
    except KeyError as key_err:
        print("\nError: An item requested does not exist in our product catalog.")
        print(f"Unknown Product Code: {key_err}")

if __name__ == "__main__":
    main()