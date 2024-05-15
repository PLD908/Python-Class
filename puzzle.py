#  This program is a word guessing game where the user tries to guess a secret word.
print("Welcome to the word guessing game!")

secret_word = "anonymous"
#  Replacing underscores with the length of secret_word
replaced = "_" * len(secret_word)  
print("Your hint is: " + replaced)

# Initialize a counter variable for guesses
number_guesses = 0 

while True:
    #  Asking user their guessing word
    guess = input("What is your guess? ")
    # Increment the counter for each guess
    number_guesses += 1  
    replaced_word = ""

    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    elif guess == secret_word:
        print("Congratulations! You guessed the word correctly:", secret_word.upper())
        # Print the number of guesses
        print("Number of guesses:", number_guesses)  
        break
    else:
        print("Incorrect guess. Try again.")

        #  Looping through the secret word
        for i in range(len(secret_word)):
            if i < len(guess) and guess[i] == secret_word[i]:
                # Correct letter in the right position
                replaced_word += guess[i].upper()  
            elif guess[i] in secret_word:
                # Correct letter in the wrong position
                replaced_word += guess[i].lower()  
            else:
                # Incorrect letter
                replaced_word += "_"  

        print("Your hint is:", replaced_word)
