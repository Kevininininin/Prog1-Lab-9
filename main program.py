# Team members: Jinghan Wu, Cesar Carbaloo

# Encode_password function encodes a string of numbers and returns the encoded string
# The encoding mechnism works by adding 3 to each digit
def encode_password(code):
    encoded_password = ""
    for char in code:
        if int(char) <= 6:
            encoded_char = int(char) + 3
            encoded_char = str(encoded_char)
            encoded_password += encoded_char
        else:
            encoded_char = int(char) + 3
            encoded_char = str(encoded_char)
            encoded_password += str(encoded_char[1])
    # print(encoded_password)
    return encoded_password

def decode_password(password):
    decoded_password = ""
    for char in password:
        if char == "0":
            decoded_password += "7"
        if char == "1":
            decoded_password += "8"
        if char == "2":
            decoded_password += "9"
        if (char != "2") and (char != "1") and (char != "0"):
            char = int(char)
            char -= 3
            decoded_password += str(char)
    return decoded_password


# The main function loops the menu until user input 3. Quit

def main():
    while True:
        print("Menu"
              "\n-------------"
              "\n1. Encode"
              "\n2. Decode"
              "\n3. Quit\n")

        option = input("Please enter an option: ")

        if option == "1":
            code = input("Please enter your password to encode: ")
            password = encode_password(code)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            decode = decode_password(password)
            print("The encoded password is " + password + ", and the original password is " + decode + ".")
            print(" ")
            pass
        elif option == "3":
            break
        else:
            print("Invalid input!")


if __name__ == '__main__':
    main()

