#This overview combines the business context, program requirements, and the Python implementation into a single, comprehensive document. It explains the purpose of the program, how it works, and the benefits it provides to the retail store.

import datetime

# Get the current day of the week
current_day = datetime.datetime.now().weekday()

# Get the subtotal from the user
subtotal = float(input("Enter the subtotal: $"))

discount = 0

# Check if it's Tuesday or Wednesday and subtotal is $50 or more
if current_day in [1, 2] and subtotal >= 50:
    discount = subtotal * 0.1
    subtotal -= discount

sales_tax = subtotal * 0.06

total = subtotal + sales_tax

if discount > 0:
    print(f"Discount amount: ${discount:.2f}")
print(f"Sales tax amount: ${sales_tax:.2f}")
print(f"Total amount due: ${total:.2f}")