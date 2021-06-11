import os
import art



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    cipher_text =""

    for letter in text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            position = alphabet.index(letter)
            if direction == 'encode':
                new_position = position + shift
            elif direction == 'decode':
                new_position = position - shift
            cipher_text += alphabet[new_position]
    
    print(f"The {direction}d text is {cipher_text}")

os.system("cls")
print(art.logo)
repeat = 'yes'
while (repeat == 'yes'):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if(shift > 25):
        shift = shift % 25 - 1





    caesar(text = text, direction = direction, shift = shift)
    repeat = input(f"Do you want to repeat? Type 'yes' or 'no' \n")

print(f"Thanks for using my program!")

# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         x = alphabet.index(letter)
#         if(x+shift <= 25):
#             cipher_text += alphabet[x+shift]
#         else:
#             cipher_text += alphabet[x-26+shift]    
    
#     print(f"The encoded text is {cipher_text}")



# def decrypt(text, shift):
#     plain_text = ""
#     for letter in text:
#         x = alphabet.index(letter)
#         if(x-shift >= 0):
#             plain_text += alphabet[x-shift]
#         else:
#             plain_text += alphabet[x+26-shift]    
    
#     print(f"The decoded text is {plain_text}")

# if(direction == "encode"):
#     encrypt(text,shift)
# elif(direction == "decode"):
#     decrypt(text,shift)
# else:
#     print(f"Error. Please input 'encode' or 'decode'")