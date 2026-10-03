import sys

def modular_inverse(a):
    for i in range(1,26):
        if (a*i)%26==1:
            return i
    return None

while True:
    try:
        a = int(input("Enter a number from 1 to 26:-"))
        if a >=1 and a<=26:
            c = modular_inverse(a)
            if c == None:
                print("This no.doesn't have a modular inverse")
            else:
                break
        else:
            print("Invalid No.")

    except ValueError:
        print("Invalid Input")


while True:
    try:
        b = int(input("Enter a no. from 0 to 25:- "))
        if b<0 or b>25:
            print("Invalid Input")
        else:
            break
    except ValueError:
        print("Invalid Input")

def affine_cipher_encryption(text):
    result =""
    for char in text:
        if char.isalpha():
            if char.isupper():
                new_index = (a*(ord(char)-ord('A'))+b)%26
                new_char = chr(ord('A') + new_index)
                result += new_char
            else:
                new_index = (a*(ord(char)-ord('a'))+b)%26
                new_char = chr(ord('a') + new_index)
                result += new_char
        else:
            result += char

    return result

def affine_cipher_decryption(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                new_index = (c*(ord(char)-ord('A')-b))%26
                new_char = chr(ord('A') + new_index)
                result += new_char
            else:
                new_index = (c*(ord(char)-ord('a')-b))%26
                new_char = chr(ord('a') + new_index)
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
            print("Exiting....")
            sys.exit()
        else:
            print("Invalid Input")

main()