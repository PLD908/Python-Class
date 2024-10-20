import csv
from datetime import datetime, timedelta, date

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    
    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
                
    except FileNotFoundError as not_found_err:
        print(f"Error: missing file - {not_found_err.filename}")
        raise
    except PermissionError as perm_err:
        print(f"Error: permission denied - {perm_err.filename}")
        raise

    return dictionary

def calculate_yogurt_discount(quantity, price):
    """Calculate the total price for yogurt with BOGO 50% off.
    
    Parameters:
        quantity: number of items ordered
        price: price per item
    Returns:
        tuple of (total price, savings)
    """
    full_price_count = (quantity + 1) // 2  
    half_price_count = quantity // 2
    
    total = (full_price_count * price) + (half_price_count * price * 0.5)
    regular_price = quantity * price
    savings = regular_price - total
    
    return total, savings

def main():
    try:
        # Print store name
        print("\nInkom Emporium")
        print()
        
        # Get current date and time
        current_date_and_time = datetime.now()
        
        # Call read_dictionary and store the compound dictionary
        products_dict = read_dictionary("products.csv", 0)
        
        print("Ordered Items:")
        
        # Initialize counters
        item_count = 0
        subtotal = 0
        total_yogurt_count = 0
        ordered_products = set()
        
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            
            # First pass: count total yogurt for accurate BOGO calculation
            for row in reader:
                if row[0] == "D083":
                    total_yogurt_count += int(row[1])
            
            # Reset file pointer to beginning
            request_file.seek(0)
            next(reader)
            
            # Second pass: process all items and print receipt
            for row in reader:
                try:
                    product_number = row[0]
                    quantity = int(row[1])
                    
                    # Get the product from the dictionary
                    product = products_dict[product_number]
                    name = product[1]
                    price = float(product[2])
                    
                    # Track ordered products for coupon
                    ordered_products.add(product_number)
                    
                    # Calculate cost for this item
                    if product_number == "D083":
                        item_total, savings = calculate_yogurt_discount(total_yogurt_count, price)
                        if savings > 0:
                            print(f"{name}: {quantity} @ ${price:.2f}")
                            print(f"    BOGO 50% OFF - You saved: ${savings:.2f}")
                            print(f"    Final price: ${item_total:.2f}")
                        else:
                            item_total = quantity * price
                            print(f"{name}: {quantity} @ ${price:.2f} = ${item_total:.2f}")
                    else:
                        item_total = price * quantity
                        print(f"{name}: {quantity} @ ${price:.2f} = ${item_total:.2f}")
                    
                    # Add to running totals
                    item_count += quantity
                    subtotal += item_total
                    
                except KeyError as key_err:
                    print(f"Error: unknown product ID in the request.csv file - {key_err}")
                    raise
        
        # Print the receipt summary
        print()
        print(f"Number of Items: {item_count}")
        print(f"Subtotal: ${subtotal:.2f}")
        
        # Calculate and print sales tax (6%)
        sales_tax = subtotal * 0.06
        print(f"Sales Tax: ${sales_tax:.2f}")
        
        # Calculate and print total
        total = subtotal + sales_tax
        print(f"Total: ${total:.2f}")
        
        # Print thank you message
        print()
        print("Thank you for shopping at the Inkom Emporium.")
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
        
        # Calculate and print return by date (30 days at 9 PM)
        return_date = current_date_and_time + timedelta(days=30)
        return_date = return_date.replace(hour=21, minute=0, second=0)
        print(f"\nReturn by: {return_date:%a %b %d %I:%M %p %Y}")
        
        # Calculate and print days until New Year
        today = date.today()
        new_year = date(today.year + 1, 1, 1)
        days_until_new_year = (new_year - today).days
        print(f"\nDon't miss our New Year's Sale in {days_until_new_year} days!")
        
        # Print random coupon for one of the ordered products
        import random
        coupon_product = random.choice(list(ordered_products))
        coupon_item = products_dict[coupon_product]
        print(f"\n----- SPECIAL OFFER -----")
        print(f"Get 20% off your next purchase of:")
        print(f"{coupon_item[1]}")
        print(f"Valid until: {(current_date_and_time + timedelta(days=14)).strftime('%b %d, %Y')}")
        print("------------------------")
        
    except FileNotFoundError as not_found_err:
        print(f"Error: missing file - {not_found_err.filename}")
    except PermissionError as perm_err:
        print(f"Error: permission denied - {perm_err.filename}")

if __name__ == "__main__":
    main()