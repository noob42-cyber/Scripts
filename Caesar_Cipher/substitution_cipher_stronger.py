import secrets
import string
import sys

letters1 = list(string.ascii_uppercase)
letters2 = list(string.ascii_lowercase)
letters = letters1 + letters2

secrets.SystemRandom().shuffle(letters)

key = "".join(letters)
value = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def substitution_encryption(text):
    table = str.maketrans(value,key)
    output= text.translate(table)
    return output

def substitution_decryption(text):
    table = str.maketrans(key,value)
    output = text.translate(table)
    return output

def main():
    while True:
        print("1.Encryption\n2.Decryption\n3.Exit")
        usr = input("Choose an option:- ")

        if usr == "1":
            text = input("Enter a text  or string to encrypt :-")
            print(substitution_encryption(text))

        elif usr == "2":
            text = input("Enter a text or string to decrypt::-")
            print(substitution_decryption(text))

        elif usr == "3":
            print("Exiting.....")
            sys.exit()

        else:
            print("Invalid Input")
main()

