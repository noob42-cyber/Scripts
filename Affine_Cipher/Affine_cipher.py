while True:    
    a = 2
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
            result += new_char

    print(result)
text = "HELLO"
affine_cipher_encryption(text)
