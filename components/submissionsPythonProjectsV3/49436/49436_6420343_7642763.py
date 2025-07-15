print('Welcome to ME 021 Wordle project!')
print('The purpose of this project is to recreate the very popular game: Wordle where a user has to guess the correct word while guessing using other words the program will notify you when a letter is in the word and when it is in wrong or right spot.')
#--------------------------------------------------------------------------------------------------
def startgame(): 
    game_start = False #set condition to keep the loop running
    while game_start == False: # allows for the code to repeat until the correct word is guessed
        game_length = input('Please enter length of the word you would like to guess: 3 or 5 \n')
        if game_length == '3': #if player chooses a 3 letter word
            print('You have choosen to play Wordle using 3 letter words!')

            import random #importing a random module 
            filename = 'wordle_3.txt' 
            with open(filename, 'r') as file: # will open the file in read mode 
                lines = file.read().splitlines() #puts all items in a list
            wordle = random.choice(lines) # the the random module picks a random item for the list
            print(wordle) # the random word is set to be guessed, only here for testing purposes
            game_attempt = 1

            game_start == True # stops the while loop and moves on to the game
            break 

        elif game_length == '5':
            print('You have choosen to play Wordle using 5 letter words!')

            import random # importing a random module
            filename = 'wordle_5.txt'
            with open(filename, 'r') as file: #will open and close the file in read mode
                lines = file.read().splitlines() # puts all items from the fill into a list
            wordle = random.choice(lines) # the random module picks a word at random from the list
            print(wordle) #the random word is set to be guessed, only here for testing purposes
            game_attempt = 1

            game_start == True #stop the while loop and moves on to the game
            break
        else:
            print("Sorry! That's not a valid option to play Wordle.")
    #--------------------------------------------------------------------------------------------------
    game_running = True 
    game_count = False
    while game_running == True: # while the condition remains true, the loop continues to run until the correct word is guessed
        print(f'Attempt {game_attempt}/6')
        guess = input('Please enter your guess! The first letter of your guess should always be capitalized \n')

        if guess == wordle:
            print(f'Correct! {guess} was the wordle!') 
            game_running = False #stops the while loop
            game_count = True
            return # breaks the loop 

        if guess != wordle: 
            print(f'{guess} is not the correct word')
            game_attempt += 1
        if game_attempt == 6 + 1:
            print('Sorry! You failed to guess the wordle.')
            return 
        x = 0
        for letter in guess:
            if letter in wordle and letter == wordle[x]: #check if every letter is in the wordle and in the correct spot
                print(f'{letter} is in the wordle and in the correct spot')
                x += 1
            elif letter in wordle: # check if the letter is in the word
                print(f'{letter} is in the wordle')
                x += 1
            else:
                print(f'{letter} is not in the wordle') 
                x += 1

game = '1'
while game == '1':  
    startgame() # while game meets the condition it will send the user right back to the start of the game
    game = input('If you wish to continue playing enter 1, if not enter any other number. \n') # allows the user to continue playing or stop playing 