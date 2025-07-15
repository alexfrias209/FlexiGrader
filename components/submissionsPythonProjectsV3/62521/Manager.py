import random

ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMERIC = '1234567890'
SYMBOLIC = ')(!@#$%^&*-_=+<>,.?:;'


def encrypting_password(password):
    password_characters = [char for char in password]
    key = str(random.randint(111, 999))
    # each different key is one digit from the overall key generated
    alphabet_key, numeric_key, symbolic_key = int(key[0]), int(key[1]), int(key[2])
    encrypted_password = []

    for char in password_characters:
        # for each character, gets new index using key corresponding to character's type
        if char in ALPHABET:
            alphabet_index = ALPHABET.index(char)
            new_char = alphabet_index + alphabet_key

            if new_char + ALPHABET.index(char) > len(ALPHABET) - 1:
                new_char = new_char - len(ALPHABET)
            encrypted_password.append(ALPHABET[new_char])

        elif char in NUMERIC:
            numeric_index = NUMERIC.index(char)
            new_char = numeric_index + numeric_key

            if new_char + NUMERIC.index(char) > len(NUMERIC) - 1:
                new_char = new_char - len(NUMERIC)
            encrypted_password.append(NUMERIC[new_char])

        elif char in SYMBOLIC:
            symbolic_index = SYMBOLIC.index(char)
            new_char = symbolic_index + symbolic_key

            if new_char + SYMBOLIC.index(char) > len(SYMBOLIC) - 1:
                new_char = new_char - len(SYMBOLIC)
            encrypted_password.append(SYMBOLIC[new_char])
    # list of password and key is returned for decrypting
    return [''.join(encrypted_password), key]


def decrypting_password(encrypted_password):
    decrypted_password = []
    alphabet_key, numeric_key, symbolic_key = int(encrypted_password[1][0]), int(encrypted_password[1][1]), int(
        encrypted_password[1][2])

    # simply reverses the original lists and uses the key of each char to get original position
    for char in encrypted_password[0]:
        if char in ALPHABET:
            alphabet_index = ALPHABET[::-1].index(char)
            new_char = alphabet_index + alphabet_key

            if new_char + ALPHABET[::-1].index(char) > len(ALPHABET) - 1:
                new_char = new_char - len(ALPHABET)
            decrypted_password.append(ALPHABET[::-1][new_char])

        elif char in NUMERIC:
            numeric_index = NUMERIC[::-1].index(char)
            new_char = numeric_index + numeric_key

            if new_char + NUMERIC[::-1].index(char) > len(NUMERIC) - 1:
                new_char = new_char - len(NUMERIC)
            decrypted_password.append(NUMERIC[::-1][new_char])

        elif char in SYMBOLIC:
            symbolic_index = SYMBOLIC[::-1].index(char)
            new_char = symbolic_index + symbolic_key

            if new_char + SYMBOLIC[::-1].index(char) > len(SYMBOLIC) - 1:
                new_char = new_char - len(SYMBOLIC)
            decrypted_password.append(SYMBOLIC[::-1][new_char])

    return ''.join(decrypted_password)


def generating_password():
    password = []

    # randomly defines how many of each character will be in a single password
    num_of_alphabets = random.randint(5, 7)
    num_of_numbers = random.randint(3, 5)
    num_of_symbols = random.randint(1, 3)

    for i in range(num_of_alphabets):
        password.append(random.choice(ALPHABET))
    for i in range(num_of_numbers):
        password.append(random.choice(NUMERIC))
    for i in range(num_of_symbols):
        password.append(random.choice(SYMBOLIC))

    random.shuffle(password)

    return ''.join(password)


def creating_file(name, password_amount=1, password=''):
    with open(f'{name}.txt', 'w+') as f:
        if password == '':
            for i in range(password_amount):
                i += 1
                encrypted_password = encrypting_password(generating_password())
                password = encrypted_password[0]
                key = encrypted_password[1]
                f.write(f'\nPassword {i}: {password} || Key {i}: {key}')
        else:
            with open(f'{name}.txt', 'w+') as f:
                for i in range(password_amount):
                    i += 1
                    encrypted_password = encrypting_password(password)
                    f.write(f'\nPassword {i}: {encrypted_password[0]} || Key {i}: {encrypted_password[1]}')


def decrypting_file(file):
    with open(f'{file}.txt', 'r+') as f:
        list = f.readlines()
        list.pop(0)

        for line, i in zip(list, range(len(list))):
            i += 1
            password_info = line.split('||')
            password = password_info[0].replace(f'Password {i}: ', '').rstrip()
            key = password_info[1].rstrip('\n').replace(f' Key {i}: ', '')
            print(f'{i}. The password ({password}) was decrypted into: ({decrypting_password([password, key])})')
