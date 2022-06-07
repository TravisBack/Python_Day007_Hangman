import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
letters_to_find = len(chosen_word)
strikes = 0

#  print(f"DEBUG: {chosen_word}")
display = []

for _ in range(letters_to_find):
    display.append('_')

print(display)

while letters_to_find > 0:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
            letters_to_find -= 1

    print(display)