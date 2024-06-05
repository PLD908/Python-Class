# This program calculates and displays the wind chill values for various wind speeds at a given temperature. The user is prompted to enter a temperature and specify whether it's in Fahrenheit or Celsius. If the temperature is provided in Celsius, it is converted to Fahrenheit. The program then calculates the wind chill for wind speeds ranging from 5 to 60 miles per hour and displays the results.

"""
The wind chill is calculated using the formula provided by the National Weather Service:
    Wind Chill (°F) = 35.74 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)
where T is the air temperature in Fahrenheit and V is the wind speed in miles per hour.
"""

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Function to calculate the wind chill given the temperature in Fahrenheit and wind speed
def calculate_wind_chill(temp_f, wind_speed):
    if wind_speed >= 3:
        wind_chill = 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp_f * (wind_speed ** 0.16)
        return wind_chill
    else:
        return temp_f 

# Wind_chill function to execute the program
def wind_chill():
    # Ask user to enter the temperature
    temp = float(input("What is the temperature? "))
    # Ask user to specify the temperature unit (Fahrenheit or Celsius)
    unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    # Converting Celsius to Fahrenheit
    if unit == 'C':
        temp_f = celsius_to_fahrenheit(temp)
    elif unit == 'F':
        temp_f = temp
    else:
        print("Invalid unit. Please enter F or C.")
        return

    # Displaying the wind chill for wind speeds ranging from 5 to 60 mph
    for wind_speed in range(5, 65, 5):
        wind_chill = calculate_wind_chill(temp_f, wind_speed)
        print(f"At temperature {temp_f:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

wind_chill()
