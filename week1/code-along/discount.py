# Author: Kevin Cross Minchakpu
"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""


from datetime import datetime

# Initialize variables
subtotal = 0.0
DISCOUNT_RATE = 0.10
TAX_RATE = 0.06


# Loop for user input (Enhancement )
print("Enter the price and quantity for each item. Enter 0 for quantity to finish.")
while True:
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    if quantity == 0:
        break
    
    subtotal += price * quantity

# Get the current day of the week
# 0 is Monday, 1 is Tuesday, 2 is Wednesday...
today = datetime.now()
weekday = today.weekday()


discount_amount = 0.0

#Check for Tuesday (1) or Wednesday (2)
if subtotal >= 50:
    if weekday == 1 or weekday == 2:
        discount_amount = subtotal * DISCOUNT_RATE
        print(f"Discount ${discount_amount:.2f}")
    else:
        print("You qualify for a discount, but it's only available on Tuesday and Wednesday.")
else:
    difference = 50 - subtotal
    print(f"Add ${difference:.2f} more to your order to receive a 10% discount!")

# Compute Tax and Final Total
sales_tax = subtotal * TAX_RATE
total_due = subtotal + sales_tax

# Final Output
if discount_amount > 0:
    print(f"Discount amount: ${discount_amount:.2f}")

print(f"Sales tax amount: ${sales_tax:.2f}")
print(f"Total amount due: ${total_due:.2f}")