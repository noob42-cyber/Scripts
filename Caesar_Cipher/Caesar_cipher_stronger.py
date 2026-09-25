import sys 
import secrets

usr = secrets.randbelow(52)
print(usr)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def Ceasar_Cipher_Encryption(text):
    result = ""
    for char in text:
        if char.isalpha():
            index = alphabet.index(char)
            new_index = (index + usr)%52
            new_char = alphabet[new_index]
            result += new_char
        else:
            result += char
    return result

def Caesar_Cipher_Decryption(text):
    result = ""

    for char in text:
        if char.isalpha():
            index = alphabet.index(char)
            new_index = (index-usr)%52
            new_char = alphabet[new_index]
            result += new_char

        else:
            result += char

    return result

def main():
    while True:
        print("1.Encryption\n2.Decryption\n3.Exit")
        option = input("Choose an option:- ")
        if option == "1":
            text = input("Enter the text you wanna encrypt:- ")
            print(f"The encrypted string is:-{Ceasar_Cipher_Encryption(text)}")
        elif option == "2":
            text = input("Enter the text you wanna decrypt:- ")
            print(f"The decrypted string is :- {Caesar_Cipher_Decryption(text)}")
        elif option == "3":
            print("Exiting....")
            sys.exit()
        else:
            print("Invalid Option")


main()



