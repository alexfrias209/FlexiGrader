print('Welcome to the Lviing Dictionary')
word = input('What word would you like looked up today? Please use all lowercase.\nYou can also input a letter to see all words of that letter.').lower()
print('We will now find all words that start with the letter', word[0])
def no_word(word, new_def):
    print('We are sorry your word is not in the dictionary.')
    new_def = input('Please put in the complete definition of the word you were trying to access.').lower()
    #All of the inputs are in lowercase to make sure that they can all be found using the same system
    f.write(f'{word} : {new_def} \n')
    print('Your word', word, 'and defintion', new_def, 'has been added to the dictionary.')
    return new_def
    #This function allows the user to input the defintion of a word not found in the dictionary into the dictionary.
def new_loop(line):
    for line in f:
        (key, value) = line.split(':')
        key = key.strip()
        value = value.strip()
        new_diction[key] = value
        #This function turns the text file into a dictionary using a for loop
def diction_loop(line):
    for line in new_diction:
        if word[0] == line[0]:
            print(line)
            #Using this for loop function the code can output and word that contains the same first letter as the inputed word
def word_loop(word, new_diction):
    for line in new_diction:
        if word == line:
            print(word, new_diction[word])
            print('Here is your word and defenition.')
            #This function, displays the word you were trying to look up and the defenition of it from the dictionary
            #Of course if the word isn't in the text file the output would be nothing
new_diction = {}
with open('62105_6411337_2538237.txt', 'r+') as f:
    line = 0
    new_loop(line)
    diction_loop(line)
    word = input('To confirm word selection please input the word you asked above again.').lower()
    word_loop(word, new_diction)
    y_or_n = input('Did you find your word today? If not put n if you did put y.')
    if y_or_n == 'y':
        print('Have a good day!')
    elif y_or_n == 'n':
        new_def = 0
        no_word(word, new_def)
    #This if else loop is to confirm if you have found your word or not
    #It makes sure that if you have found your word it doesn't need to do the new_def function