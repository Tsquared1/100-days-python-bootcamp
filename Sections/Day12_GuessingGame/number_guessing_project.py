from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def play_game(lives):
    while True:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            return f"You got it! The answer was {number}"
        elif guess > number:
            print("Too high.")
            lives -= 1
        elif guess < number:
            print("Too low.")
            lives -= 1

        if lives == 0:
            return f"You've run out of guesses, you lose. The answer was {number}"
        else:
            print("Guess again.")


# Loop repeats until user chooses easy or hard
while True:
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == 'easy':
        player_lives = 10
        break
    elif choice == 'hard':
        player_lives = 5
        break
    else:
        print("Input error. Please try again!")

numbers_list = []
for i in range(1, 101):
    numbers_list.append(i)
number = random.choice(numbers_list)

print(play_game(player_lives))






