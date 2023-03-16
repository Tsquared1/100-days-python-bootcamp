alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for letter in plain_text:
        x = alphabet.index(letter)
        new_position = x + shift_amount
        # If index is bigger than the length of the alfabet
        if new_position >= 26:
            new_position -= 26
        encoded_letter = alphabet[new_position]
        cipher_text += encoded_letter
    print(f"The encoded text is {cipher_text}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

 #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

def decrypt(cipher_text, shift_amount):
    plain_text = ''
    for letter in cipher_text:
        x = alphabet.index(letter)
        new_position = x - shift_amount
        if new_position < 0:
            new_position += 26
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("Invalid input. Please enter only 'encode' or 'decode'!")

