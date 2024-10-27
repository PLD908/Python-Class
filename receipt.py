"""
CREATIVE ELEMENTS ADDED:
1. BOGO 50% off discount for yogurt (item D083)
2. Return by date showing 9:00 PM 30 days in future
3. Days until New Year's Sale countdown
4. Random coupon generator for purchased items
5. Additional features beyond requirements:
    - Comprehensive error handling including csv.Error
    - Input validation for quantities and prices
    - Helper function for consistent currency formatting
    - Detailed error messages with context
"""

import csv
from datetime import datetime, timedelta, date
import random

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
            
            for row_number, row in enumerate(reader, start=2):
                # Validate that the key_column_index is valid
                if key_column_index >= len(row):
                    raise ValueError(f"Row {row_number}: Invalid key column index {key_column_index}")
                    
                key = row[key_column_index]
                dictionary[key] = row
                
    except FileNotFoundError as not_found_err:
        print(f"Error: missing file - {not_found_err.filename}")
        raise
    except PermissionError as perm_err:
        print(f"Error: permission denied - {perm_err.filename}")
        raise
    except csv.Error as csv_err:
        print(f"Error: invalid CSV file format - {filename}")
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
    if quantity <= 0 or price <= 0:
        raise ValueError("Quantity and price must be positive numbers")
        
    full_price_count = (quantity + 1) // 2  
    half_price_count = quantity // 2
    
    total = (full_price_count * price) + (half_price_count * price * 0.5)
    regular_price = quantity * price
    savings = regular_price - total
    
    return total, savings

def format_currency(amount):
    #Format amount as currency with $ and 2 decimal places.
    return f"${amount:.2f}"

def main():
    STORE_NAME = "Inkom Emporium"
    SALES_TAX_RATE = 0.06
    YOGURT_CODE = "D083"
    
    try:
        # Print store name
        print(f"\n{STORE_NAME}")
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
        
        # First pass: count yogurt items
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            
            for row in reader:
                if row[0] == YOGURT_CODE:
                    total_yogurt_count += int(row[1])
        
        # Second pass: process all items
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            
            for row in reader:
                try:
                    product_number = row[0]
                    quantity = int(row[1])
                    
                    if quantity <= 0:
                        raise ValueError(f"Invalid quantity {quantity} for product {product_number}")
                    
                    # Get the product from the dictionary
                    product = products_dict[product_number]
                    name = product[1]
                    price = float(product[2])
                    
                    if price <= 0:
                        raise ValueError(f"Invalid price {price} for product {product_number}")
                    
                    # Track ordered products for coupon
                    ordered_products.add(product_number)
                    
                    # Calculate cost for this item
                    if product_number == YOGURT_CODE:
                        item_total, savings = calculate_yogurt_discount(total_yogurt_count, price)
                        if savings > 0:
                            print(f"{name}: {quantity} @ {format_currency(price)}")
                            print(f"    BOGO 50% OFF - You saved: {format_currency(savings)}")
                            print(f"    Final price: {format_currency(item_total)}")
                        else:
                            item_total = quantity * price
                            print(f"{name}: {quantity} @ {format_currency(price)} = {format_currency(item_total)}")
                    else:
                        item_total = price * quantity
                        print(f"{name}: {quantity} @ {format_currency(price)} = {format_currency(item_total)}")
                    
                    # Add to running totals
                    item_count += quantity
                    subtotal += item_total
                    
                except KeyError as key_err:
                    print(f"Error: unknown product ID in the request.csv file - {key_err}")
                    raise
                except ValueError as val_err:
                    print(f"Error: {val_err}")
                    raise
        
        # Print the receipt summary
        print("\nOrder Summary:")
        print(f"Number of Items: {item_count}")
        print(f"Subtotal: {format_currency(subtotal)}")
        
        # Calculate and print sales tax
        sales_tax = subtotal * SALES_TAX_RATE
        print(f"Sales Tax: {format_currency(sales_tax)}")
        
        # Calculate and print total
        total = subtotal + sales_tax
        print(f"Total: {format_currency(total)}")
        
        # Print thank you message and date/time
        print(f"\nThank you for shopping at {STORE_NAME}.")
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")
        
        # Calculate and print return by date
        return_date = current_date_and_time + timedelta(days=30)
        return_date = return_date.replace(hour=21, minute=0, second=0)
        print(f"\nReturn by: {return_date:%a %b %d %I:%M %p %Y}")
        
        # Calculate and print days until New Year
        today = date.today()
        new_year = date(today.year + 1, 1, 1)
        days_until_new_year = (new_year - today).days
        print(f"\nDon't miss our New Year's Sale in {days_until_new_year} days!")
        
        # Print random coupon
        if ordered_products:
            coupon_product = random.choice(list(ordered_products))
            coupon_item = products_dict[coupon_product]
            coupon_expiry = current_date_and_time + timedelta(days=14)
            
            print(f"\n----- SPECIAL OFFER -----")
            print(f"Get 20% off your next purchase of:")
            print(f"{coupon_item[1]}")
            print(f"Valid until: {coupon_expiry:%b %d, %Y}")
            print("------------------------")
        
    except (FileNotFoundError, PermissionError, KeyError, ValueError, csv.Error) as error:
        print(f"\nProgram ended with error: {str(error)}")
        return
        
if __name__ == "__main__":
    main()