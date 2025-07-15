#IMPORTANT NOTES:
# ensure the 'Words.txt' file is in the same folder as the .py file
# in order for the program to correct any misspelled word, it must be the same length as the correct word
# You can miss type any letters at any position in the word but make sure to keep your misspelled word the same length as the correctly spelled word
# The program can only correct words that are given in the 'Words.txt' file, you must write with no Punctuation
# The program will correct a passage so long as its made up of words given in the 'Words.txt'
# You may add your own correctly spelled words to the 'Words.txt' file

import os
WordListFile = os.path.join(os.getcwd(), "62990_6416371_9342892.txt")

def intro():
    print('''Welcome to my spellchecker!
The purpose is to take user-entered text and return all instances of misspelled words. 
Then give the option to correct or ignore each word.\n''') #just an intro to my program

def Find_Mispelled_words(Usr,library): 
    library = set(library)
    Usr = set(Usr)
    mis = set.difference(Usr,library) #cleverly converted into a set and returns list of all different aka misspelled ones
    return list(mis) # this is me banking on the idea that i will read from a file full of all the words ever 

def Difference_counter(Usr,library):
    Usr = list(Usr) 
    library = list(library)
    i=0
    Tf=[] # container for list of true and false statements
    for letter in Usr: # goes through each letter per word
        if letter == library[i]:
            Tf.append('True')
        else:
            Tf.append('False')
        i=i+1
    return Tf.count('False') #gives back the number of different letters

def closest_match(Usr,library):
    Fixed_word = ''# container for correct word
    Max_differences = len(Usr) #finds a word of same length this is probably my programs biggest flaw, only corrects words of same length
    for word in library:
        if len(Usr) == len(word):
            differences = Difference_counter(Usr,word) #nested function calls for number of different letters
            if differences < Max_differences: # only works if the amount of different letters is less than the length of the word
                Fixed_word = word
                Max_differences = differences #sets the new low and does it over again until it finds a word with different letters closer to 0
    return Fixed_word
    
def go_through_each_word(Usr,Usr_txt):
    New_usr = Usr_txt.copy() # copy of user input to be altered
    New_usr_string = ''
    for Single_word in Usr: #goes one word at a time
        Fixed = closest_match(Single_word,WordList) #nested function calls for it to find closest word via the library and the user input
        yn = input(f'Would you like to replace {Single_word} with {Fixed}? (yes/no):\n') # gets yes no option to replace
        while yn not in ['yes', 'no']:# makes sure you only type yes or no also allows you to skip words
            print("Invalid input. Please enter 'yes' or 'no'.")
            yn = input(f'Would you like to replace {Single_word} with {Fixed}? (yes/no):\n') 
        if yn == 'yes': #if the input is yes then we get to the part where it updates the copy of the list with the new word
            print('Correct word has been applied!')
            index = New_usr.index(Single_word) #gets the position of the word 
            New_usr[index] = Fixed #replaces word with new word in the index position
            New_usr_string = ' '.join(New_usr) # converts list into string to print back to the user
    return New_usr_string

def open_and_reformat_list():
    with open(WordListFile,'r') as library:
        List = library.readlines()
    formatted_list = []
    for word in List:
        without = word.replace('\n','')
        formatted_list.append(without)
    return formatted_list

intro()
WordList = open_and_reformat_list()
while True:
    Usr_txt = input('Type your passage (or hit the enter key to quit)\n').lower() 
    Usr_txt = Usr_txt.split()
    mis = Find_Mispelled_words(Usr_txt,WordList) #function gives the misspelled words using sets
    if len(Usr_txt) == 0: #checks to see if user just pushes enter then ends the program
        break
    if len(mis) == 0:#checks to see if there are any words in the misspelled list and if not then that means there is no misspelled words
        print('All is good! There are no misspelled words')
    else:
        print(f'It seems like the follwing words may have been misspelled\n{mis}\n')# displays the list of words that are misspelled
        print(go_through_each_word(mis,Usr_txt))# does the function by going through each word and returns the new list it makes 
