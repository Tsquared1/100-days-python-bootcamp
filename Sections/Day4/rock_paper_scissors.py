import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# 0 beats 2, 1 beats 0, 2 beats 1
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_input = random.randint(0, 2)

# Player lose:
if player_input == 0 and computer_input == 1:
    print(f"Your choice: {rock}\n")
    print(f"Computer chose: {paper}\n")
    print("You lose!")
elif player_input == 1 and computer_input == 2:
    print(f"Your choice: {paper}\n")
    print(f"Computer chose: {scissors}\n")
    print("You lose!")
elif player_input == 2 and computer_input == 0:
    print(f"Your choice: {scissors}\n")
    print(f"Computer chose: {rock}\n")
    print("You lose!")
# Player wins:
elif player_input == 1 and computer_input == 0:
    print(f"Your choice: {paper}\n")
    print(f"Computer chose: {rock}\n")
    print("You win!")
elif player_input == 2 and computer_input == 1:
    print(f"Your choice: {scissors}\n")
    print(f"Computer chose: {paper}\n")
    print("You win!")
elif player_input == 0 and computer_input == 2:
    print(f"Your choice: {rock}\n")
    print(f"Computer chose: {scissors}\n")
    print("You win!")
# Draw
elif player_input == 0 and computer_input == 0:
    print(f"Your choice: {rock}\n")
    print(f"Computer chose: {rock}\n")
    print("Draw!")
elif player_input == 1 and computer_input == 1:
    print(f"Your choice: {paper}\n")
    print(f"Computer chose: {paper}\n")
    print("Draw!")
elif player_input == 1 and computer_input == 1:
    print(f"Your choice: {scissors}\n")
    print(f"Computer chose: {scissors}\n")
    print("Draw!")


