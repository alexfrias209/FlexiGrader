import os

from Manager import creating_file, decrypting_file, SYMBOLIC
def setting_mode():
    while True:
        mode = input('\n---\nCreate Password[c] -\n---\nOpen File[o] -\n---\nQuit[q] -\n---\nInput:')
        if mode in 'cCoOqQ':
            return mode
        else:
            print('\nInvalid input. Try Again.')


def initializing_create():
    naming_file = True
    setting_preference = True
    setting_password_amount = True
    password_amount = None

    while naming_file:
        file_name = input('\nName of file encrypted password will be saved to [No use of special characters]: ')
        for char in file_name:
            if char == '_':
                pass
            elif char in SYMBOLIC:
                print('Invalid Character Detected')
                break
        naming_file = False

    while setting_preference:
        password = input('\nDo you want a specific password to be saved and encrypted to your device [type in your password if \'yes\', type \'no\' if not]: ')
        if password.lower() == 'no':
            while setting_password_amount:
                password_amount = input('\nHow many passwords do you want generated? ')
                if password_amount.isdigit():
                    password_amount = int(password_amount)
                    setting_preference = False
                    setting_password_amount = False
                else:
                    print('Not a number')
                    continue
        elif password.lower() == 'yes':
            password = input('\nWhat is your password? ')
            setting_preference = False
        else:
            continue

    if password_amount == None:
        creating_file(file_name,1 ,password)
    else:
        creating_file(file_name, password_amount)


def initializing_open():
    opening_file = True

    while opening_file:
        file_name = input('\nWhat file would you like to open? ')
        if os.path.exists(f'{file_name}.txt'):
            decrypting_file(file_name)
            opening_file = False
        else:
            print('This file doesnt exist. Try again.')
            continue
    pass


def executing_mode(mode):
    if mode in 'Cc':
        initializing_create()
    elif mode in 'Oo':
        initializing_open()
    else:
        print('\nSee you next time.')
        print('\nQuitting')
        quit()


running = True

if __name__ == '__main__':
    print('\nWelcome to Password Manager.\nHere you can create passwords which will be encrypted in a file saved to your device.\nDeveloped by Adam Guerrero \nEnjoy!')

    while running:
        mode = setting_mode()
        executing_mode(mode)
