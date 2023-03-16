# Step 5

import random
from hangman_words import word_list
from hangman_art import stages, logo, fireworks

# Welcome
print(logo + '\n')

lives = 6

# Choosing a random word
chosen_word = word_list[random.randint(0, len(word_list)-1)]

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for letter in chosen_word:
    display += '_'

# Changing blanks with found letter
chosen_word_len = len(chosen_word)

guessed_letters = []
correct_letters = []
wrong_letters = []

end_of_game = False
while end_of_game is False:
    # Join all the elements in the list and turn it into a String.
    print(f"The word is: {' '.join(display)}\n")

    guess = input('Guess a letter: ').lower()
    # Check guessed letter
    for position in range(chosen_word_len):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in guessed_letters:
        if guess not in chosen_word:
            lives -= 1
            # Checks if the user has any lives left.
            print(stages[lives])
            if lives == 0:
                end_of_game = True
                print("You lose!\n"
                      f"The word was: {chosen_word}")

            else:
                print("Incorrect. Try another letter.")
    else:
        print(f"\nYou already guessed this letter.\n"
              f"Already guessed letters: {', '.join(guessed_letters)}")
    guessed_letters += guess

    # Cheks if the user has got all letter
    if '_' not in display:
        end_of_game = True
        print("\nCongratulations! You won!"
              f"\nThe word was: {chosen_word}")
        print('\n' + fireworks)


