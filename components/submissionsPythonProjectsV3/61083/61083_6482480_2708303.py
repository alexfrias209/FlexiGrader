import random
#added to make upper case lower case
def shift_char(char, shift_amount, is_uppercase):
    if char.isalpha():
        char_base = ord('A') if is_uppercase else ord('a')
        shifted_char = chr(((ord(char) - char_base - shift_amount) % 26) + char_base)
        return shifted_char
    return char

def generate_key():
    return [random.randint(1, 9) for _ in range(3)]
#need to find a way to make it so that ints larger than 9 work

def encrypt(message):
    key = generate_key()
    encoded_message = ""

    for i, char in enumerate(message):
        is_uppercase = char.isupper()
        char = char.lower()
        shift_amount = key[i % 3]
        encoded_message += shift_char(char, shift_amount, is_uppercase)

    return key, encoded_message

def decrypt(message, key):
    decoded_message = ""
    for i, char in enumerate(message):
        is_uppercase = char.isupper()
        char = char.lower()
        shift_amount = key[i % 3]
        decoded_message += shift_char(char, -shift_amount, is_uppercase)
    return decoded_message

def main():
    while True:
        option = input("Enter 'encode', 'decode', or 'quit': ").lower()
        if option == 'quit':
            break
        if option not in ['encode', 'decode']:
            print("Invalid option. Please enter 'encode', 'decode', or 'quit'.")
            continue

        message = input("Enter a message: ")
        if option == 'encode':
            key, encoded = encrypt(message.lower())
            print("Key:", ''.join(map(str, key)))
            print("Encoded Message:", encoded)
        else:
            key = input("Enter a 3-digit key: ")
            if len(key) != 3 or not key.isdigit():
                print("Key should be a 3-digit number.")
                continue
            decoded = decrypt(message.lower(), [int(digit) for digit in key])
            print("Decoded Message:", decoded)

if __name__ == "__main__":
    main()

#todo
#get code to work with shift numbers above 9
#get program to write to a text file on desktop called secretMessage.txt
