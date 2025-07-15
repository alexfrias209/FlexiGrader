#Project: Notepad - Create a notepad where the user reads and writes to a text or csv file.. Be able to append, find words, replace words, delete words.
import os

#create the test files (both csv and text)
## short stories created by ChatGBT
def create():
    f = open("the_wishful_coin.txt", "w")
    f.write('\033[1m' + 'The Wishful Coin' + '\033[0m' + '\n')
    f.write('\n')
    f.write('Tim found an old coin by the fountain. With a chuckle, he tossed it in, making a wish. The coin fell with a plunk. The wish, it seemed, had a powerful echo, for the coin, now gleaming, landed back in his hand. Tim realized the true wish had already come true — he had found the coin, and that was the magic.')
    f.close()

    g = open("the_unseen_artist.txt", "w")
    g.write('\033[1m' + 'The Unseen Artist' + '\033[0m' + '\n')
    g.write('\n')
    g.write('A street artist painted a mural in an alleyway, but nobody noticed. Frustrated, he added a sign, "Invisible Art: $1." Suddenly, a crowd formed. People laughed, paid a dollar, and marveled at nothing. The artist\'s ironic statement had turned his ignored mural into a masterpiece.')
    g.close()

    h = open('the_lost_smile.txt', 'w')
    h.write('\033[1m' + 'The Lost Smile' + '\033[0m' + '\n')
    h.write('\n')
    h.write('Sophia\'s smile vanished one day. She searched high and low, asking everyone, but it was nowhere to be found. Frustrated, she sat alone, contemplating her lost joy. As she sighed deeply, a child handed her a colorful balloon, saying, "Here, this might help you find your smile." The simple act of kindness brought her smile back.')
    h.close()

    i = open('the_trees_secret.txt', 'w')
    i.write('\033[1m' + 'The Tree\'s Secret' + '\033[0m')
    i.write('\n')
    i.write('A tree in the park bore enigmatic carvings. An old man revealed they were messages from his youth, etched for a lost love. He visited the tree daily, but his love never returned. Upon his passing, the tree blossomed with identical carvings, as if his love had finally responded, in a language only trees could understand.')
    i.close()

    j = open('the_persistent_dandelion.txt', 'w')
    j.write('\033[1m'+'The Persistent Dandelion'+'\033[0m')
    j.write('\n')
    j.write('In a pristine garden, a dandelion sprouted, refusing to wither. The gardener couldn\'t remove it without causing damage. So, he allowed the stubborn dandelion to stay. The flower\'s resilience inspired the other plants. Before long, the garden flourished with wild beauty, proving that sometimes, what appears as a weed is simply a unique form of beauty.')
    j.close()

    ##CSV
    r = open("the_wishful_coin.csv", "w")
    r.write('\033[1m' + 'The Wishful Coin' + '\033[0m' + '\n')
    r.write('\n')
    r.write('Tim found an old coin by the fountain. With a chuckle, he tossed it in, making a wish. The coin fell with a plunk. The wish, it seemed, had a powerful echo, for the coin, now gleaming, landed back in his hand. Tim realized the true wish had already come true — he had found the coin, and that was the magic.')
    r.close()

    s = open("the_unseen_artist.csv", "w")
    s.write('\033[1m' + 'The Unseen Artist' + '\033[0m' + '\n')
    s.write('\n')
    s.write('A street artist painted a mural in an alleyway, but nobody noticed. Frustrated, he added a sign, "Invisible Art: $1." Suddenly, a crowd formed. People laughed, paid a dollar, and marveled at nothing. The artist\'s ironic statement had turned his ignored mural into a masterpiece.')
    s.close()

    t = open('the_lost_smile.csv', 'w')
    t.write('\033[1m' + 'The Lost Smile' + '\033[0m' + '\n')
    t.write('\n')
    t.write('Sophia\'s smile vanished one day. She searched high and low, asking everyone, but it was nowhere to be found. Frustrated, she sat alone, contemplating her lost joy. As she sighed deeply, a child handed her a colorful balloon, saying, "Here, this might help you find your smile." The simple act of kindness brought her smile back.')
    t.close()

    u = open('the_trees_secret.csv', 'w')
    u.write('\033[1m' + 'The Tree\'s Secret' + '\033[0m')
    u.write('\n')
    u.write('A tree in the park bore enigmatic carvings. An old man revealed they were messages from his youth, etched for a lost love. He visited the tree daily, but his love never returned. Upon his passing, the tree blossomed with identical carvings, as if his love had finally responded, in a language only trees could understand.')
    u.close()

    v = open('the_persistent_dandelion.csv', 'w')
    v.write('\033[1m'+'The Persistent Dandelion'+'\033[0m')
    v.write('\n')
    v.write('In a pristine garden, a dandelion sprouted, refusing to wither. The gardener couldn\'t remove it without causing damage. So, he allowed the stubborn dandelion to stay. The flower\'s resilience inspired the other plants. Before long, the garden flourished with wild beauty, proving that sometimes, what appears as a weed is simply a unique form of beauty.')
    v.close()

#append function
def append(name_file, words):
    f = open(name_file, "a")
    f.write('\033[1m' + ' ' + words + '\033[0m')
    f.close()

#find function
def find(name_file, words):
    f = open(name_file, "r")
    reading = f.read()
    temp = False
    if words in reading:
        temp = True
    g = open(name_file, "w")
    if temp == True:
        reading = reading.replace(words, '\033[1m' + words + '\033[0m')
    else:
        g.write("The word is not in the file.\n")
    g.write(reading)

    g.close()
    f.close()

#replace function
def replace(name_file, words, find_words):
    f = open(name_file, "r")
    reading = f.read()
    temp = False
    if find_words in reading:
        temp = True
    g = open(name_file, "w")
    if temp == True:
        reading = reading.replace(find_words, '\033[1m' + words + '\033[0m')
    else:
        g.write("The word you want to replace is not in the file.\n")
    g.write(reading)

    g.close()
    f.close()

#delete function
def delete(name_file, words):
    f = open(name_file, "r")
    reading = f.read()
    temp = False
    if words in reading:
        temp = True
    g = open(name_file, "w")
    if temp == True:
        reading = reading.replace(words, '')
    else:
        g.write("The word you want to delete is not in the file.\n")
    g.write(reading)

    g.close()
    f.close()


#main screen
def main_menu():
    print('Welcome to the Notepad Python Project!!!')
    print('D')
    print('Project Description: Create a notepad where the user reads and writes into a text or csv file. Must be able to append, find words, replace words, and delete woryourds.')
    print()

    print('\033[1m'+'MAIN MENU'+'\033[0m')
    print('Choose what kind of file you will like to work with for your notepad:')
    print('1. text file')
    print('2. csv file')
    type_file = input('Enter the number of the file you will like to work with (EX. 1. text file, type "1"): ')
    temp = ' '
    if type_file.isnumeric() == False:
        temp = type_file
        type_file = 0
    else:
        type_file = int(type_file)
    print()

    while type_file < 1 or type_file > 2:
        if temp != ' ':
            print(f'{temp} isn\'t an option. Try again.')
            temp = ' '
        else:
            print(f'{type_file} isn\'t an option. Try again.')
        type_file = input('Enter the number of the file you will like to work with (EX. 1. text file, type "1"): ')
        if type_file.isnumeric() == False:
            temp = type_file
            type_file = 0
        else:
            type_file = int(type_file)
        print()
    if type_file == 1:
        os.system('cls')
        print('\033[1m'+'FILE CHOICE'+'\033[0m')
        print('Choose which file you want to work on: ')
        print('1. The Wishful Coin')
        print('2. The Unseen Artist')
        print('3. The Lost Smile')
        print('4. The Tree\'s Secret')
        print('5. The Persistent Dandelion')
        temp = ' '
        name_file = input('Enter the number of the file you want to work on (EX. 1. The Wishful Coin, type "1"): ')
        if name_file.isnumeric() == False:
            temp = name_file
            name_file = 0
        else:
            name_file = int(name_file)
        print()
        while name_file < 1 or name_file > 5:
            if temp != ' ':
                print(f'{temp} isn\'t an option. Try again.')
                temp = ' '
            else:
                print(f'{name_file} isn\'t an option. Try again.')
            name_file = input('Enter the number of the file you want to work on (EX. 1. The Wishful Coin, type "1"): ')
            if name_file.isnumeric() == False:
                temp = name_file
                name_file = 0
            else:
                name_file = int(name_file)
            print()
        type_file = 'text'
        if name_file == 1:
            name_file = 'the_wishful_coin.txt'
        elif name_file ==2 :
            name_file = 'the_unseen_artist.txt'
        elif name_file == 3:
            name_file = 'the_lost_smile.txt'
        elif name_file == 4:
            name_file = 'the_trees_secret.txt'
        else:
            name_file = 'the_persistent_dandelion.txt'
        print(f'You will like to work with a {type_file} file named {name_file}.')
    else:
        os.system('cls')
        print('\033[1m'+'FILE CHOICE'+'\033[0m')
        print('Choose which file you want to work on: ')
        print('1. The Wishful Coin')
        print('2. The Unseen Artist')
        print('3. The Lost Smile')
        print('4. The Tree\'s Secret')
        print('5. The Persistent Dandelion')
        temp = ' '
        name_file = input('Enter the number of the file you want to work on (EX. 1. The Wishful Coin, type "1"): ')
        if name_file.isnumeric() == False:
            temp = name_file
            name_file = 0
        else:
            name_file = int(name_file)
        print()
        while name_file < 1 or name_file > 5:
            if temp != ' ':
                print(f'{temp} isn\'t an option. Try again.')
                temp = ' '
            else:
                print(f'{name_file} isn\'t an option. Try again.')
            name_file = input('Enter the number of the file you want to work on (EX. 1. The Wishful Coin, type "1"): ')
            if name_file.isnumeric() == False:
                temp = name_file
                name_file = 0
            else:
                name_file = int(name_file)
            print()
        type_file = 'text'
        if name_file == 1:
            name_file = 'the_wishful_coin.csv'
        elif name_file ==2 :
            name_file = 'the_unseen_artist.csv'
        elif name_file == 3:
            name_file = 'the_lost_smile.csv'
        elif name_file == 4:
            name_file = 'the_trees_secret.csv'
        else:
            name_file = 'the_persistent_dandelion.csv'
    return name_file

#Action Menu
def action_menu(name_file):
    os.system('cls')

    #print file before action
    os.system('cls')
    f = open(name_file, "r")
    print(f.read())
    print()
    input('Press Enter when you are done reading the files.')

    os.system('cls')
    print('\033[1m'+'ACTION MENU'+'\033[0m')
    print(f'Choose what you will like to do to {name_file}:')
    print('1. Append your own word or phrase (add words to file)')
    print('2. Find a certain word or phrase')
    print('3. Replace a certain word or phrase with your own word or phrase')
    print('4. Delete a certain word or phrase within the file')
    temp = ' '
    action_file = input('Enter the number of the action you will like to do (EX. 1. Append, type "1"): ')
    if action_file.isnumeric() == False:
        temp = action_file
        action_file = 0
    else:
        action_file = int(action_file)
    print()
    while action_file < 1 or action_file > 4:
        if temp != ' ':
            print(f'{temp} isn\'t an option. Try again.')
            temp = ' '
        else:
            print(f'{action_file} isn\'t an option. Try again.')
        action_file = input('Enter the number of the action you will like to do (EX. 1. Append, type "1"): ')
        if action_file.isnumeric() == False:
            temp = action_file
            action_file = 0
        else:
            action_file = int(action_file)
        print()

    #start action
    words = ''
    if action_file == 1:
        words = input('Enter the word or phrase you will like to append. \n')
        append(name_file, words)
    elif action_file == 2:
        words = input('Enter the word or phrase you will like to find. \n')
        find(name_file, words)
    elif action_file == 3:
        find_words = input('Enter the word or phrase you will like to replace.  \n')
        words = input('Enter the word or phrase you will like to replace it with. \n')
        replace(name_file, words, find_words)
    else:
        words = input('Enter the word or phrase you will like to delete. \n')
        delete(name_file, words)

    #print file after action
    os.system('cls') 
    again = open(name_file, "r")
    print(again.read())
    print()
    
    print('ACTION DONE')
    print('When you finish reading the file, choose to: ')
    print('1. Return to the action menu to continue to work on the current file')
    print('2. Return to the main menu to choose a different file and/or reset your current file')
    print('3. Exit notepad')
    temp = ' '
    finish = input('Enter the number of the option you will like to do (EX. 3. Exit notepad, type "3"): ')
    if finish.isnumeric() == False:
        temp = finish
        finish = 0
    else:
        finish = int(finish)
    print()
    while finish < 1 or finish > 3:
        if temp != ' ':
            print(f'{temp} isn\'t an option. Try again.')
            temp = ' '
        else:
            print(f'{finish} isn\'t an option. Try again.')
        finish = input('Enter the number of the option you will like to do (EX. 3. Exit notepad, type "3"): ')
        if finish.isnumeric() == False:
            temp = finish
            finish = 0
        else:
            finish = int(finish)
        print()
    finishing(finish, name_file)

    again.close()
    f.close()

def finishing(finish, name_file):
    os.system('cls')
    if finish == 3:
        print('Thank You For Participating!')
    elif finish == 2:
        create()
        name_file = main_menu()
        action_menu(name_file)
    else:
        action_menu(name_file)

#starting system output
os.system('cls')
create()
name_file = main_menu()
action_menu(name_file)