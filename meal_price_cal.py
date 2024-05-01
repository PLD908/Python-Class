# Asking user the price of child's and adult's meal
price_of_childs_meal = float(input("What is the price of a child's meal? "))
price_of_adults_meal = float(input("What is the price of a adult's meal? "))

# Asking user the number of children and adults
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

#  Getting the subtotal of the meal
subtotal = ((price_of_childs_meal) * (number_of_children)) + ((price_of_adults_meal) * (number_of_adults))

#  Printing the subtotal of the meal
print(f"Subtotal: ${subtotal:.2f}")

# Asking user the sales tax rate
sales_tax_rate = int(input("What is the sales tax rate? "))

#  Getting the sales tax
sales_tax = (subtotal * sales_tax_rate) / 100

#  Print the sales tax 
print(f"Sales Tax: ${sales_tax:.2f}")

#  Print total
total = (subtotal + sales_tax)
print(f"Total: ${total:.2f}")

#  Asking user the payment amount
payment_amount = float(input("What is the payment amount? "))

#  Getting user change and print the result
change_amount = payment_amount - total
print(f"Change: ${change_amount:.2f}")