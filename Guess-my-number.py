#  Importing random
import random

#  Asking user their guessing number
guessing_number = int(input("What is your guessing number? "))

#  Generating a random number between 1 and 10
number = random.randint(1, 10)
print(f"What is the magic number? {number}.")

#  checking if the number is within the range
while guessing_number != number:
    print(f"What is your guess? {guessing_number}.")
    if guessing_number > number:
        guess = "Higher"
    else:
        guess = "Lower"
    guessing_number = int(input(f"Your guess is {guess} than the magic number. What is your guess? "))

print("You guessed the magic number.")