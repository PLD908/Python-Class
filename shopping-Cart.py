#  Shopping Cart Program
# This program allows users to add, remove, view items, compute the total price, and quit from a shopping cart.

print("Welcome to the shopping Cart Program!")

carts = []
price_of_each_items = []

while True:
    print("What would you like to do?")

    #  Asking user to select one of the following 
    shopping_carts = ["Add an item", "Remove an item", "View cart", "Compute total", "Quit"]

    for item in shopping_carts:
        print(f"{shopping_carts.index(item) + 1}. {item}")
        
    #  Asking user to enter an action to display
    action = int(input("Please enter your action: "))

    if action == 1:
        item_to_add = input("What item would you like to add? ")
        price = input("What is the price of " + "'" + item_to_add + "'? ")
        carts.append(item_to_add)
        price_of_each_items.append(price)
        print(f"{item_to_add} has been added to the cart.")
    elif action == 2:
        item_to_remove = input("What item name would you like to remove? ")
        if item_to_remove in carts:
            index = carts.index(item_to_remove)
            carts.pop(index)
            price_of_each_items.pop(index)
            print(f"{item_to_remove} has been removed from the cart.")
        else:
            print(f"{item_to_remove} is not in the cart.")
    elif action == 3:
        print("The contents of the shopping cart are: ")
        if not carts:
            print("The cart is empty.")
        else:
            for (item, price) in zip(carts, price_of_each_items):
                print(f"{carts.index(item) + 1}. {item}: ${price}")
    elif action == 4:
        total = 0
        for each_price in price_of_each_items:
            total += float(each_price)
        print(f"The total price of the items in the shopping cart is: ${total:.2f}")
    elif action == 5:
        print("Thank you for using the shopping cart program.")
        break
    else:
        print("Invalid action. Please enter a number between 1 and 5.")