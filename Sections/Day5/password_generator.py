# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Finding out the total number of each category
no_of_letters = len(letters) - 1
no_of_numbers = len(numbers) - 1
no_of_symbols = len(symbols) - 1

password = []
# Adding letters:
for letter_index in range(1, nr_letters + 1):
    password.append(letters[random.randint(0, no_of_letters)])
# Adding symbols
for symbol_index in range(1, nr_symbols + 1):
    password.append(symbols[random.randint(0, no_of_symbols)])
# Adding numbers:
for nr_index in range(1, nr_numbers + 1):
    password.append(numbers[random.randint(0, no_of_numbers)])

# Transforming the password list into a string
password = ''.join(password)
print(f"Order not randomized: {password}\n")


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

final_password = []
final_password_len = nr_symbols + nr_numbers + nr_letters

for i in range(0, final_password_len):
    final_password.append(0)
print(final_password)
characters_list = [nr_symbols, nr_numbers, nr_letters]

for i in range(0, final_password_len):
    position = random.randint(0, final_password_len - 1)
    type_of_character = random.randint(0, 2)
    while final_password[position] != 0:

        if type_of_character == 1 and nr_symbols != 0:
            nr_symbols -= 1
            final_password.append(symbols[random.randint(0, no_of_symbols)])
        elif type_of_character == 2 and nr_numbers != 0:
            nr_numbers -= 1
            final_password.append(numbers[random.randint(0, no_of_numbers)])
        elif type_of_character == 3 and nr_letters != 0:
            nr_letters -= 1
            final_password.append(letters[random.randint(0, no_of_letters)])


# print(final_password_len)
# for i in range(0, final_password_len):
#     type_of_character = random.randint(1, 3)
#     if type_of_character == 1 and nr_symbols != 0:
#         nr_symbols -= 1
#         final_password.append(symbols[random.randint(0, no_of_symbols)])
#     elif type_of_character == 2 and nr_numbers != 0:
#         nr_numbers -= 1
#         final_password.append(numbers[random.randint(0, no_of_numbers)])
#     elif type_of_character == 3 and nr_letters != 0:
#         nr_letters -= 1
#         final_password.append(letters[random.randint(0, no_of_letters)])
#
# final_password = ''.join(final_password)
# print(f'Order Randomized: {final_password}')
