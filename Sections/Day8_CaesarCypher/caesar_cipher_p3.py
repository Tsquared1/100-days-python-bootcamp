alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(start_text, shift_amount, action):
    final_text = ''
    if action == 'decode':
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        final_text += alphabet[new_position]
    print(f"The {action}d text is {final_text}.")



# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(start_text=text, shift_amount=shift, action=direction)


