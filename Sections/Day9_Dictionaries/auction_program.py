from art import logo

print(logo)
print("Welcome to the secret auction program!")



bids_dictionary = {}
other_bidders = True
while other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids_dictionary[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if choice == 'no':
        other_bidders = False

max_bid = 0
for bidder_name in bids_dictionary:
    bid = bids_dictionary[bidder_name]
    if bid > max_bid:
        max_bid = bid
        winner_name = bidder_name

print(f"The winner is {winner_name} with a bid of ${max_bid}.")


