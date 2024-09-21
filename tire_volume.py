#This program not only meets all the basic requirements for calculating and storing tire volume, but also includes additional features such as tire price lookup and the option to store customer phone numbers for potential purchases, enhancing its practical utility.

import math
import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    # Calculate volume
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return volume

def get_tire_price(width, aspect_ratio, diameter):
    if width == 205 and aspect_ratio == 60 and diameter == 15:
        return 100
    elif width == 215 and aspect_ratio == 65 and diameter == 16:
        return 120
    elif width == 225 and aspect_ratio == 55 and diameter == 17:
        return 140
    elif width == 235 and aspect_ratio == 50 and diameter == 18:
        return 160
    else:
        return None

def main():
    print("This program calculates the volume of space inside a tire.")

    # Get input from the user
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    width = float(width)
    aspect_ratio = float(aspect_ratio)
    diameter = float(diameter)

    # Calculate the volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)

    # Print the result
    print(f"The approximate volume is {volume:.2f} liters")

    # Look up the price
    price = get_tire_price(width, aspect_ratio, diameter)
    if price:
        print(f"The price for tires of this size is ${price}")
    else:
        print("Price information not available for this tire size")

    # Get the current date
    current_date = datetime.date.today()

    # Ask if the user wants to buy tires
    buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ").lower()

    # Open the volumes.txt file for appending
    with open("volumes.txt", "a") as file:
        # Write the basic information to the file
        file.write(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}")
        
        # If the user wants to buy tires, ask for the phone number
        if buy_tires == "yes":
            phone_number = input("Please enter your phone number: ")
            file.write(f", {phone_number}")
        
        file.write("\n")

    print("Tire information has been saved to volumes.txt")

if __name__ == "__main__":
    main()