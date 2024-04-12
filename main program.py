# Team members: Jinghan Wu, Cesar Carbaloo
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
            encode_password(code)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            pass
        elif option == "3":
            break




if __name__ == '__main__':
    main()

