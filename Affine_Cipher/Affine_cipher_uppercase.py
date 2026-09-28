import sys

while True:    
    a = 3
    try:
        b = int(input("Enter the no,from 0 to 25:- "))
        if b<0 or b>25:
            print("Invalid input")
        else:
            break
    except ValueError:
        print("Invalid Value")

def affine_cipher_encryption(text):
    result =""
    for char in text:
        if char.isalpha():
            new_index = (a*(ord(char)-ord('A'))+b)%26
            new_char = chr(ord('A') + new_index)
            result += new_char
        else:
            result += char
    return result
def affine_cipher_decryption(text):
    result =""
    for char in text:
        if char.isalpha():
            new_index = ((ord(char)-ord('A')-b)/a)%26
            new_char = chr(ord('A')+new_index)
            result += new_char
        else:
            result += char
    return result

def main():
    while True:
        print("1.Encryption\n2.Decryption\n3.Exit")
        usr = input("Choose an option:-")
        if usr == "1":
            text = input("Enter the text you wanna encrypt:-")
            print(affine_cipher_encryption(text))
        elif usr == "2":
            text = input("Enter the text you wanna decrypt:- ")
            print(affine_cipher_decryption(text))
        elif usr == "3":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid Input")

main()
