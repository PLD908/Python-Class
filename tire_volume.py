# This program calculates the approximate volume of a tire in liters 

import math

def calculate_tire_volume(width, aspect_ratio, diameter):
    # Calculate tire volume using the formula
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

    return volume

def main():
    print("This program calculates the volume of space inside a tire.")
    
    # Get user input
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate the volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)

    # Output the result
    print(f"\nThe volume of space inside the tire is approximately {volume:.2f} liters.")

if __name__ == "__main__":
    main()