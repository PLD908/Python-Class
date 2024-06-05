# This program reads life expectancy data from a CSV file and calculates the overall maximum and minimum life expectancy, as well as the average, maximum, and minimum life expectancy for a user-specified year.

# Asking user to enter the year of interest
year_of_interest = input('Enter the year of interest: ')

expectancy = ""
entity = ""
year = ""
min_year = ""
min_entity = ""
# Initialize min_expectancy to positive infinity
min_expectancy = float('inf')  
# Initialize max_expectancy to negative infinity
max_expectancy = float('-inf')  

with open("life-expectancy.csv") as f:
    # Skip the header line
    next(f)
    for line in f:
        each_line = line.strip().split(",")
        the_ent = each_line[0]
        the_year = int(each_line[2])
        the_exp = float(each_line[3])

        # Find overall min and max life expectancy
        if the_exp > max_expectancy: 
            max_expectancy = the_exp
            year = the_year
            entity = the_ent

        if the_exp < min_expectancy:
            min_expectancy = the_exp
            min_year = the_year
            min_entity = the_ent

print(f"The overall max life expectancy is: {max_expectancy:.2f} from {entity} in {year}")
print(f"The overall min life expectancy is: {min_expectancy:.2f} from {min_entity} in {min_year}")

# Variables to calculate average life expectancy for the year of interest
total_life_expectancy = 0
count = 0
max_life_expectancy_year = float('-inf')
min_life_expectancy_year = float('inf')
max_entity_year = ""
min_entity_year = ""

with open("life-expectancy.csv") as file:
    # Skip the header line
    next(file)
    for line in file:
        each_line = line.strip().split(",")
        the_ent = each_line[0]
        the_year = int(each_line[2])
        the_exp = float(each_line[3])

        if the_year == int(year_of_interest):
            total_life_expectancy += the_exp
            count += 1

            if the_exp > max_life_expectancy_year:
                max_life_expectancy_year = the_exp
                max_entity_year = the_ent

            if the_exp < min_life_expectancy_year:
                min_life_expectancy_year = the_exp
                min_entity_year = the_ent

if count > 0:
    average_life_expectancy = total_life_expectancy / count
    print(f"For the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
    print(f"The max life expectancy was in {max_entity_year} with {max_life_expectancy_year:.2f}")
    print(f"The min life expectancy was in {min_entity_year} with {min_life_expectancy_year:.2f}")
else:
    print(f"No data found for the year {year_of_interest}")
