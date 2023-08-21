from other import *
from os import system
import platform

def clear_display():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

def encode(text, key):
    cipher_text = ""
    
    for char in text:
        position = alphabet.index(char) + 1
        cipher_text_i = position + key
        if cipher_text_i > alphabet_len:
            cipher_text_i = cipher_text_i % alphabet_len
        cipher_text += alphabet[cipher_text_i - 1]
    print(f"The {choice}d text is : \"{cipher_text}\"")
    

def decode(text, key):
    plain_text = ""
    
    for char in text:
        position = alphabet.index(char) + 1
        plain_text_i = position - key
        if plain_text_i < 1:
            plain_text_i = plain_text_i + (alphabet_len * (int((plain_text_i*(-1)) / alphabet_len)+1))
        plain_text += alphabet[plain_text_i - 1]
    print(f"The {choice}d text is : \"{plain_text}\"")



#Program start from here
global alphabet_len
alphabet_len = len(alphabet)

clear_display()
    
while True:
    print(logo)
    choice = input("Type 'encode' to encrypt\nType 'decode' to decrypt\n==> ")
    if choice == "encode" or choice == "decode":
        text = input("Type your messege : ")
        key = int(input("Type the key number : "))
        # key = key % int((len(alphabet) / 2))
        if choice == "encode":
            encode(text, key)
        else:
            decode(text, key)
    else:
        print("\nWrong Selection\nYou need to type 'encode' to encrypt or 'decode' to decrypt\n")

    isContinue = input("Do you want to continue? (Y/N) : ")
    clear_display()
    if isContinue == 'n' or isContinue == 'N': break
    
print("\n\n---------------------------------------------------")
print("\nGoodbye\nThanks for using....")
print("---------------------------------------------------")