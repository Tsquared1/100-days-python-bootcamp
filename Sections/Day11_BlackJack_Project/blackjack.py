from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_deck = len(cards)


# TODO 1: Deal both user and computer a starting hand of 2 random card values.
def draw_cards(players_cards, players_cards_sum):
    # Assign 1 random card index
    card_index = random.randint(0, cards_deck - 1)
    # Card gets the card index
    card = cards[card_index]
    # Cards list receive the card
    players_cards.append(card)
    # Adds the card value to the cards sum
    players_cards_sum += card
    return players_cards_sum


# Draw 2 random cards for the player & computer
player_cards = []
player_cards_sum = 0

computer_cards = []
computer_cards_sum = 0

for i in range(2):
    player_cards_sum = draw_cards(player_cards, player_cards_sum)
    computer_cards_sum = draw_cards(computer_cards, computer_cards_sum)


print(f"Your cards: {player_cards}, current score: {player_cards_sum}")
print(f"Computer's first card: {computer_cards[0]}")


# TODO 2: Detect when computer or user has a blackjack. (Ace + 10 value card).
def final_hand():
    print(f"Your final hand: {player_cards}, final score: {player_cards_sum}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_cards_sum}")


def player_blackjack():
    final_hand()
    print("You win with a Blackjack!")


def computer_blackjack():
    final_hand()
    print("Lose, opponent has Blackjack!")


def went_over():
    final_hand()
    print("You went over. You lose!")


if computer_cards_sum == 21:
    computer_blackjack()
elif player_cards_sum == 21:
    player_blackjack()
# if player_cards_sum > 21:








# Ask the player if he/she wants to play
# want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
# if want_play == 'y':
#     print(logo)
# else:
#     print("Game closed!")

# Improvements: Show the total in the hand. Show the cards outside of a list