# Step 4
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

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

end_of_game = False
while end_of_game is False:
    guess = input('Guess a letter: ').lower()
    # Check guessed letter
    for position in range(chosen_word_len):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        # Checks if the user has any lives left.
        if lives == 0:
            end_of_game = True
            print("You lose!")
        print("Incorrect. Try another letter.")
        print(stages[lives])

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")

    # Cheks if the user has got all letter
    if '_' not in display:
        end_of_game = True
        print("You won!")

