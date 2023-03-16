# Step 3
import random

# Creating a list of words
word_list = ["arctic", "baboon", "camel", "apple"]

# Choosing a random word
chosen_word = word_list[random.randint(0, len(word_list)-1)]

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for letter in chosen_word:
    display += '_'

# Changing blanks with found letter
chosen_word_len = len(chosen_word)

while '_' in display:
    # User inputs a letter
    guess = input('Guess a letter: ').lower()
    for position in range(chosen_word_len):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    print(display)
print("You won")







