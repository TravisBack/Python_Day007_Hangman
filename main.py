import random

word_list = ["ardvark", "baboon", "camel"]

# Choose a random word
chosen_word = random.choice(word_list)

#  Ask the user to guess a letter
guess = input("Guess a letter: ").lower()

# Check if the letter guessed is in the chosen word.
for letter in chosen_word:
    if letter == guess:
        print(True)
    else:
        print(False)
