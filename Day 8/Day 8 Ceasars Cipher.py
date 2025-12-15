import os
import time
import cipher_resources as cr

def encrypt(original_text, shift, encode_or_decode):
    new_text = ""
    if encode_or_decode == 'decode':
        shift *= -1
    for letters in original_text:
        if letters in cr.alphabet:
            new_index = (cr.alphabet.index(letters) + shift) % len(cr.alphabet)
            new_text += cr.alphabet[new_index]
        else:
            new_text += letters

    print(f"Your {encode_or_decode}ed message is: {new_text}")

running = True
while running:
    os.system("cls")
    print(cr.header)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        os.system("cls")
        print(f"Your choice of {direction} is not either 'encode' or 'decode' please choose again.")
        time.sleep(5)
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    encrypt(text, shift, direction)

    user_choice = input("Would you like to keep encoding or decoding? Type 'yes' or 'no':\n").lower()
    if user_choice == 'no':
        os.system("cls")
        print(cr.header)
        print("Thanks for using the Ceasars Cipher!")
        time.sleep(3)
        running = False


