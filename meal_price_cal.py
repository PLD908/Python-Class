# Asking user the price of child's and adult's meal
price_of_childs_meal = input("What is the price of a child's meal? ")
price_of_adults_meal = input("What is the price of a adult's meal? ")

# Asking user the number of children and adults
number_of_children = input("How many children are there? ")
number_of_adults = input("How many adults are there? ")

#  Getting the subtotal of the meal
subtotal = (int(price_of_childs_meal) * int(number_of_children)) + (int(price_of_adults_meal) * int(number_of_adults))

#  Printing the subtotal of the meal
print(f"Subtotal: ${subtotal:.2f}")