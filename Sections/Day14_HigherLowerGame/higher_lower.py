# Import random
import random
from art import logo, vs

# Import game_data file
from game_data import data


# print the game logo
print(logo)

# Generate a random number to pick an Instagram account from game_data
account_a = random.choice(data)


answer_wrong = False
score = 0
while not answer_wrong:
    # Print the score if the score is greater than 0
    if score > 0:
        print(f"\nYou're right! Current score: {score}.")

    # Format the text to appear like this: "Compare A: Zendaya, a Actress and musician, from United States."
    # Print option A.
    print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}.")

    # Create a while loop that generates another random choice for account b
    account_b = random.choice(data)
    # If against_b is the same as compare_a, it needs to be changed.
    # Make a loop that generates random choice for against_b as long as they are different
    while account_a == account_b:
        account_b = random.choice(data)

    # Print the 'vs' logo between the two accounts
    print(vs)
    print(f"Against B: {account_b['name']}, {account_b['description']}, from {account_b['country']}.")

    # Create a variable name higher_follower_count that stores the higher value of follower count
    # between the two dicts (compare_a and against_b)
    higher_follower_count = max(account_a['follower_count'], account_b['follower_count'])

    # Validate user's input
    invalid_input = True
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    while invalid_input:
        # Ask the user to choose between account 'A' or 'B'
        if user_choice == 'a' or user_choice == 'b':
            invalid_input = False
        else:
            print("Invalid input. Try again!\n")
            user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
            invalid_input = True
    # Compare the user_choice follower count with the other account followers
    answer_right = False
    if user_choice == 'a' and account_a['follower_count'] > account_b['follower_count']:
        score += 1
    elif user_choice == 'b' and account_b['follower_count'] > account_a['follower_count']:
        score += 1
    else:
        answer_wrong = True
    account_a = account_b

# When users answer's wrong, print the final score
print(f"Sorry, that's wrong. Final score: {score}")

