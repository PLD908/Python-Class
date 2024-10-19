import csv

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

    # Open the CSV file for reading
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        # Read the rows one at a time from the CSV file
        for row in reader:
            key = row[key_column_index]

            dictionary[key] = row

    return dictionary

def main():
    # Call read_dictionary and store the compound dictionary in products_dict
    products_dict = read_dictionary("products.csv", 0)
    
    # Print the products dictionary
    print("\nProducts Dictionary:")
    print(products_dict)
    print()

    # Open the request.csv file and process each row
    print("Requested Items:")
    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        
        next(reader)
        
        # Process each row in the request.csv file
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            
            # Use the product number to find the corresponding product in products_dict
            if product_number in products_dict:
                product = products_dict[product_number]
                name = product[1]
                price = float(product[2])
                
                print(f"{name}: {quantity} @ ${price}")

if __name__ == "__main__":
    main()