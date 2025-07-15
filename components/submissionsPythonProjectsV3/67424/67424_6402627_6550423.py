import random #allows for me to generate a random selection from character I have choosen.
1
def generate_password(): #Created my own module in order to use  
    low_letters = 'abcdefghijklmnopqrstuvwxyz'
    up_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symb = '!#$%&*:[]+-?'
    nums = '0123456789'
    #list of characters we will use for a random password ^^^

    list_characters = low_letters + up_letters + symb + nums
    #list_characters is a string of all characters above put togther hence the + 

    num_passwords = 1
    #by defualt I have set number of passwords to be generated to be 1
    length_choice = int(input( 'Enter number of characters you would like to use?'))
    #length_choice will allow user to input the number of random characters they would like to be used

    for x in range(num_passwords):  #range is restricted to only 1 password being generated
        password = ''.join(random.sample(list_characters, length_choice))
        #uses the number of characters that the user choose from the list of characters.
        print('Newly generated password:', password)
    return

filename = '67424_6402628_9559515.txt'
def append_to_file(filename, website, password):
    with open(filename, 'a') as file: #opens file and appends to the file
        file.write(f'\n{website}, {password}') #.write writes website, password in the txt file.
    return 



print('Welcome to the password generator')
print('my project is a password generator that can also store passwords created for you the user.')

x='y'
while x == 'y':
    decision = int(input('\n Choices: \nPress 1 to generate password and store. \nPress 2 to print all passwords saved \nPress 3 to End \n Your choice:  '))
    filename = "67424_6402628_9559515.txt"
    if decision == int(1):
        generate_password()
    
        website = input('Enter name of password: ')
        password = input('Rewrite newly generated password: ')

        append_to_file(filename, website, password)

    elif decision == int(2):
        with open(filename, 'r') as f: #reads the file
            print(f.read()) #prints whatis in the file
    
    else: #My option for the user to end the program.
        print('Thank you')
        break


