# Asking the user for their grade percentage
user_grade = int(input("What is your grade: "))
print(user_grade)

# Letter grade for a course
if user_grade >= 90:
    letter = "A"
elif user_grade >= 80:
    letter = "B"
elif user_grade >= 70:
    letter = "C"
elif user_grade >= 60:
    letter = "D"
else:
    letter = "F"

# Print the letter grade
print("Your letter grade is:", letter)

# congratulatory and encouragement messages
if user_grade >= 70:
    print("Congratulations! You earned a passing grade of", user_grade, "and achieved a letter grade of", letter)
else:
    print("You didn't pass this time. Don't get discouraged! Keep working hard to improve your grade. Your current grade is", user_grade, "with a letter grade of", letter)
