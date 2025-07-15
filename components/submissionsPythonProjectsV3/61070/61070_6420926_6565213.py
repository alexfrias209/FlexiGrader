import random
import time
import os
import sys    


print( """
                   ### ### ### ###
               ###                 ###
           ###                         ###
        ###                               ###
      ###                                   ###
    ###   __      ___  _ ___ ___ _            ###
   ###    \ \    / / || | __| __| |            ###
  ###      \ \/\/ /| __ | _|| _|| |__           ###
 ###        \_/\_/ |_||_|___|___|____|           ###
 ###                                 ___  ___    ###
 ###                                / _ \| __|   ###
 ###                               | (_) | _|    ###
 ###                                \___/|_|     ###
 ###          ___        _                       ###
 ###         | __|__ _ _| |_ _  _ _ _  ___      ###  
  ###        | _/ _ \ '_|  _| || | ' \/ -_)    ###
   ###       |_|\___/_|  \__|\_,_|_||_\___|   ###
      ###                                   ###
        ##                                ###
           ###                         ###
               ###                 ###
                   ### ### ### ###
""")
time.sleep(2)
os.system('cls')


# Load the Data from file:
from wheel_of_fortune_defined_lists import all_data
# Words/data scraped from: "https://wheeloffortuneanswer.com/"
scores = []

with open('61070_6420927_7513282.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split(' = ')
        score = parts[1].split(' ')[0]
        scores.append(score)
   

print("Welcome to Denys' project! \nDenys is the developer of the project. \n ------------------------------------------\nThis project is a wheel of fortune game. \nYou, the player, compete against two AI opponents for 5 rounds. \nThe game emulates the essence of the classic TV show.\nYou will be earning money, guessing letters, buying vowels, and solving puzzles.")
print('If at any point you need a reminder on what you can do, just type "help"\n ------------------------------------------')

print()
print('The scores are a count of each round win (words correctly solved)')
print(f'You have {scores[0]} points from previous games')
print(f'CPU 1 has {scores[1]} points from previous games')
print(f'CPU 2 has {scores[2]} points from previous games')

score_player = int(scores[0])
score_cpu1 = int(scores[1])
score_cpu2 = int(scores[2])


print()

name = input('What is your name? ')
while True:
    global ai_diff
    ai_diff = input('How difficult do you want the ai AND game to be (Hard, Medium, Easy)? ')
    if ai_diff.lower() in ['easy', 'medium', 'hard']:
        print('Alright, have fun!')
        time.sleep(3)
        print()
        break
    else:
        print('Invalid choice, try again')
        continue

os.system('cls')

def show_help():
    print("####################################################")
    print('_____________________________________')
    print('To earn money you will spin the wheel and for each letter guessed correctly you will get that amount.')
    print('You have to pay $250 for each vowel, and you dont get any money for guessing vowels correctly.')
    print('There are 5 rounds.')
    print('_____________________________________')
    print("Available choices:")
    print(" vowel : Buy a vowel.")
    print(" solve : Attempt to solve the puzzle.")
    print("_____________________________________")
    print(" consonants: ", end="")
    for i in consonants:
        print(i, " ", end="")
    print()
    print(" vowels:  ", end='')
    for i in vowels:
        print(i, " ", end="")
    print()
    print("####################################################")

money = 0
money_cpu1 = 0
money_cpu2 = 0

def buy_vowel():
    while True:
        global money
        if money < 250:
            print('Not enough money to buy vowel')
            return 0
        vowel = input('Type a vowel to buy (A, E, I, O, U) ')
        if len(vowel) != 1:
            print('Type one letter!')
            continue
        else:
            if vowel.upper() in vowels:
                print('You bought: ', vowel.upper())
                money -= 250
                return vowel
            else:
                print('Invalid vowel!')
                continue


def round_win(winner):
        global score_player
        global score_cpu1
        global score_cpu2
        global name
        global money
        global money_cpu1
        global money_cpu2
        print('Puzzle solved!')
        if winner == name:
            money += 1000
            score_player += 1
            print()
            print(f'Congrats {winner}!! You got $1000, and your total money is ${money}')
        else:
            if winner == 'CPU1':
                money_cpu1 += 1000
                score_cpu1 += 1
                print(f'{winner} got $1000, their total money is ${money_cpu1}')
            else:
                money_cpu2 += 1000
                score_cpu2 += 1
                print(f'{winner} got $1000, their total money is ${money_cpu2}')
                

def spin_wheel():
    spin_values = [500, 500, 550, 600, 600, 650, 700, 700, 750, 800, 800, 850, 900, 900, 2500, 'Bankrupt' , 'Bankrupt' , 'Lose A Turn'] #Add other cases, bankrupt, free spin? etc.
    spin_value = spin_values[random.randint(0, len(spin_values) - 1)]
    return spin_value
            


round = 1

phrases = []
for i in all_data:
    b = [phrase.upper() for phrase in i[1:]]
    phrases.append(b)


for turn in range(5):
    random_num = random.randint(0, 23)
    category = all_data[random_num][0]
    random_num_2 = random.randint(1, len(category))
    phrase = all_data[random_num][random_num_2].upper()
    os.system('cls')
    print('------------------------------------------')
    print('Round', round)
    
    
    
    puzzle_solved = 0
    
    contestants = [name, 'CPU 1' , 'CPU 2']
    consonants = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'V', 'X', 'Z', 'H', 'R', 'W', 'Y']
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    special_chars = ["'", '&', ',' , '-' , '.' , '"' , '!' , '?']
    sorted_guesses = ['Z', 'Q', 'X', 'J', 'K', 'V', 'B', 'P', 'Y', 'G', 'F', 'W', 'M', 'U', 'C', 'L', 'D', 'R', 'H', 'S', 'N', 'I', 'O', 'A', 'T', 'E']
    
    
    puzzle = []
    for letter in phrase:
        if letter == ' ':
            puzzle.append(' ') 
        elif letter in special_chars:
            puzzle.append(letter) 
        else:
            puzzle.append('_')

    def print_board():
            for i in puzzle:
                print('|',i, end="")
            print('|')
            print()
            print('Category: ', category)
                
    print()
    next_round = False
    sorted_guesses_copy = sorted_guesses[:]
    def remove_from_copy(guess):
        if guess.upper() in sorted_guesses_copy:
            sorted_guesses_copy.remove(guess.upper())
            
    time.sleep(3)
    while '_' in puzzle and next_round == False:
        for i in range(3):
            wrong_guess = False
            if contestants[i] == name:
                os.system('cls')
                print(contestants[i], "taking turn.")
                wheel = spin_wheel()
                n = '' if wheel == 'Bankrupt' or wheel == 'Lose A Turn' else '$'
                print(f'You spun {n}{wheel}!')
                if wheel == 'Bankrupt':
                    print('Oh no! You lost your money!')
                    print()
                    money *= 0
                    wheel = 0
                    time.sleep(3)
                elif wheel == 'Lose A Turn':
                    print('Oh no! You lost your turn!')
                    print()
                    time.sleep(3)
                    continue # USING CONTINUE IN RANGES SKIPS THE TURN
                else:
                    print()
                time.sleep(3)
                
                while wrong_guess == False:
                    os.system('cls')
                    print()
                    print()
                    print() 
                    if '_' not in puzzle:
                        round_win(name)
                        next_round = True
                        time.sleep(4)
                        break
                    print_board()
                    print()
                    print(f'You have ${money}')
                    n = '' if wheel == 'Bankrupt' or wheel == 'Lose A Turn' else '$'
                    print(f'You spun {n}{wheel}!')
                    player_guess_2 = input(f'Enter a consonant, buy a vowel, or "solve": ')
                    player_guess = player_guess_2.upper()
                    if player_guess.lower() == 'help':
                        show_help()
                        input('Type anything to continue')
                        continue 
                    
                    if player_guess.lower() == 'vowel':
                        bought_vowel = buy_vowel()
                        time.sleep(1)
                        if bought_vowel == 0:
                            time.sleep(2)
                            continue
                        
                        remove_from_copy(bought_vowel)
                        occurrences = phrase.count(bought_vowel.upper())
                        
                        if occurrences == 0:
                            print("Letter not found in puzzle!")
                            wrong_guess = True
                            print()
                            time.sleep(3)
                            break
                        
                        position = -1
                        
                        for occurence in range(occurrences):
                            position = phrase.find(bought_vowel.upper(), position + 1)
                            if position < len(puzzle):
                                puzzle[position] = bought_vowel.upper()
                        continue

                    if len(player_guess) == 1 and player_guess.upper() in consonants:
                        if player_guess not in sorted_guesses_copy:
                            print('You cant guess already guessed letters!')
                            time.sleep(3)
                            continue
                        occurrences = phrase.count(player_guess) 
                        
                        if player_guess.upper() in sorted_guesses_copy:
                            sorted_guesses_copy.remove(player_guess.upper())
                            
                        if occurrences == 0:
                            print("Letter not found in puzzle!")
                            wrong_guess = True
                            print()
                            time.sleep(3)
                            break
                        
                        position = -1
                        
                        for occurence in range(occurrences):
                            position = phrase.find(player_guess.upper(), position + 1)
                            
                            money += wheel
                            if position < len(puzzle):
                                puzzle[position] = player_guess.upper()
                    if len(player_guess) == 1 and player_guess.upper() in vowels:
                        print('You cant guess vowels! You have to buy them!')
                        time.sleep(3)
                        continue

                    if player_guess.lower() == 'solve':
                            answer_guess = input('Type your answer to solve the puzzle (with the spaces/special characters) ')
                            if answer_guess.upper() == phrase:
                                round_win(name)
                                next_round = True
                                time.sleep(4)
                                break
                            else:
                                print()
                                print(f'Nope! {answer_guess} is not the phrase!')
                                time.sleep(3)
                                break
                    

                    #these have to be the bottom if else statements
                    if len(player_guess) > 1:
                        print('You have to guess one letter!')
                        time.sleep(3)
                        continue

                
            if i == 1 and next_round == False:
                os.system('cls')
                print(contestants[i], "taking turn.")
                time.sleep(2)
                wheel = spin_wheel()
                index = -1
                while True:
                    os.system('cls')
                    print()
                    if '_' not in puzzle:
                        round_win("CPU1")
                        time.sleep(4)
                        next_round = True
                        
                        break
                    print()
                    print()
                    print()
                    print_board()
                    print()
                    print(f'{contestants[i]} has ${money_cpu1}')
                    
                    n = '' if wheel == 'Bankrupt' or wheel == 'Lose A Turn' else '$'
                    print(f'{contestants[i]} spun {n}{wheel}!')
                    if wheel == 'Bankrupt':
                        print(f'Oh no! {contestants[i]} lost their money!')
                        print()
                        money_cpu1 *= 0
                        wheel = 0
                        time.sleep(3)
                    elif wheel == 'Lose A Turn':
                        print(f'Oh no! {contestants[i]} lost their turn!')
                        print()
                        time.sleep(3)
                        break
                    else:
                        print()
                    
                    
                    if ai_diff.lower() == 'easy':
                        guess = random.choice(sorted_guesses_copy)
                        if puzzle.count('_') <= 4:
                            print(f'{contestants[i]} tried to solve the puzzle!')
                            random.randint(0,2)
                            time.sleep(3)
                            if random.randint(0,1) == 0:
                                print(f'{contestants[i]} solved the puzzle!')
                                print(f'The puzzle was {phrase}')
                                round_win("CPU1")
                                next_round = True
                                time.sleep(4)
                                break
                                
                            else:
                                print(f'{contestants[i]} guessed wrong!')
                                time.sleep(3)
                                break
                        
                    
                    if ai_diff.lower() == 'medium':
                        random.randint(0,1)
                        if random.randint(0,1) == 0:
                            guess = random.choice(sorted_guesses_copy) 
                        else:
                            guess = sorted_guesses_copy[index]
                            index -= 1
                        if puzzle.count('_') <= 5:
                            print(f'{contestants[i]} tried to solve the puzzle!')
                            random.randint(0,1)
                            time.sleep(3)
                            if random.randint(0,1) == 0:
                                print(f'{contestants[i]} solved the puzzle!')
                                print(f'The puzzle was {phrase}')
                                round_win("CPU1")
                                next_round = True
                                time.sleep(4)
                                break
                                
                            else:
                                print(f'{contestants[i]} guessed wrong!')
                                time.sleep(3)
                                break
                            
                    if ai_diff.lower() == 'hard':
                        guess = sorted_guesses_copy[index]
                        index -= 1
                    if puzzle.count('_') <= 6:
                            print(f'{contestants[i]} tried to solve the puzzle!')
                            random.randint(0,1)
                            time.sleep(3)
                            if random.randint(0,1) == 0:
                                print(f'{contestants[i]} solved the puzzle!')
                                print(f'The puzzle was {phrase}')
                                round_win("CPU1")
                                next_round = True
                                time.sleep(4)
                                break
                                
                            else:
                                print(f'{contestants[i]} guessed wrong!')
                                time.sleep(3)
                                break
                    
                    if money_cpu1 >= 250:
                        index = -1
                    
                    if guess in vowels:
                        if money_cpu1 < 250:
                         continue
                
                    
                    print(f'CPU 1 guesses: {guess}')
                    
                    time.sleep(3)
                    if guess in consonants:
                        remove_from_copy(guess)
                        occurrences = phrase.count(guess) 
                        if occurrences == 0:
                            print("Letter not found in puzzle!")
                            print()
                            time.sleep(3)
                            break
                        
                        position = -1
                        for occurence in range(occurrences):
                            position = phrase.find(guess, position + 1)
                            
                            money_cpu1 += wheel
                            if position < len(puzzle):
                                puzzle[position] = guess
                    
                    if guess in vowels:
                        if money_cpu1 < 250:
                            print('CPU 1 tried to guess a vowel but doesnt have enough money!')
                            time.sleep(1.3)
                            continue
                        else:
                            print(f'CPU 1 bought vowel {guess}')
                            remove_from_copy(guess)
                            money_cpu1 -= 250 
                            time.sleep(3)
                            occurrences = phrase.count(guess) 
                            if occurrences == 0:
                                print("Letter not found in puzzle!")
                                print()
                                time.sleep(3)
                                break
                            
                            position = -1
                            for occurence in range(occurrences):
                                position = phrase.find(guess, position + 1)
                                
                                if position < len(puzzle):
                                    puzzle[position] = guess

            
                
            if i == 2 and next_round == False:
                os.system('cls')
                print(contestants[i], "taking turn.")
                time.sleep(2)
                wheel = spin_wheel()
                index = -1
                while True:
                    os.system('cls')
                    print()
                    if '_' not in puzzle:
                        round_win("CPU2")
                        next_round = True
                        time.sleep(4)
                        break
                    print()
                    print()
                    print()
                    print_board()
                    print()
                    print(f'{contestants[i]} has ${money_cpu2}')
                    
                    n = '' if wheel == 'Bankrupt' or wheel == 'Lose A Turn' else '$'
                    print(f'{contestants[i]} spun {n}{wheel}!')
                    if wheel == 'Bankrupt':
                        print(f'Oh no! {contestants[i]} lost their money!')
                        print()
                        money_cpu2 *= 0
                        wheel = 0
                        time.sleep(3)
                    elif wheel == 'Lose A Turn':
                        print(f'Oh no! {contestants[i]} lost their turn!')
                        print()
                        time.sleep(3)
                        break
                    else:
                        print()
                    
                    
                
                    if ai_diff.lower() == 'easy':
                        guess = random.choice(sorted_guesses_copy)
                        if puzzle.count('_') <= 4:
                            print(f'{contestants[i]} tried to solve the puzzle!')
                            random.randint(0,2)
                            time.sleep(3)
                            if random.randint(0,1) == 0:
                                print(f'{contestants[i]} solved the puzzle!')
                                print(f'The puzzle was {phrase}')
                                round_win("CPU2")
                                next_round = True
                                time.sleep(4)
                                break
                                
                            else:
                                print(f'{contestants[i]} guessed wrong!')
                                time.sleep(3)
                                break
                        
                    
                    if ai_diff.lower() == 'medium':
                        random.randint(0,1)
                        if random.randint(0,1) == 0:
                            guess = random.choice(sorted_guesses_copy) 
                        else:
                            guess = sorted_guesses_copy[index]
                            index -= 1
                        if puzzle.count('_') <= 5:
                            print(f'{contestants[i]} tried to solve the puzzle!')
                            random.randint(0,1)
                            time.sleep(3)
                            if random.randint(0,1) == 0:
                                print(f'{contestants[i]} solved the puzzle!')
                                print(f'The puzzle was {phrase}')
                                round_win("CPU2")
                                next_round = True
                                time.sleep(4)
                                break
                                
                            else:
                                print(f'{contestants[i]} guessed wrong!')
                                time.sleep(3)
                                break
                            
                    if ai_diff.lower() == 'hard':
                        guess = sorted_guesses_copy[index]
                        index -= 1
                    if puzzle.count('_') <= 6:
                            print(f'{contestants[i]} tried to solve the puzzle!')
                            random.randint(0,1)
                            time.sleep(3)
                            if random.randint(0,1) == 0:
                                print(f'{contestants[i]} solved the puzzle!')
                                print(f'The puzzle was {phrase}')
                                round_win("CPU2")
                                next_round = True
                                time.sleep(4)
                                break
                                
                            else:
                                print(f'{contestants[i]} guessed wrong!')
                                time.sleep(3)
                                break
                    if money_cpu2 >= 250:
                        index = -1
                    
                    if guess in vowels:
                        if money_cpu2 < 250:
                         continue
                        
                    print(f'CPU 2 guesses: {guess}')
                    time.sleep(3)
                    if guess in consonants:
                        remove_from_copy(guess)
                        occurrences = phrase.count(guess) 
                        if occurrences == 0:
                            print("Letter not found in puzzle!")
                            print()
                            time.sleep(3)
                            break
                        
                        position = -1
                        for occurence in range(occurrences):
                            position = phrase.find(guess, position + 1)
                            
                            money_cpu2 += wheel
                            if position < len(puzzle):
                                puzzle[position] = guess
                    
                    if guess in vowels:
                        if money_cpu2 < 250:
                            print('CPU 2 tried to guess a vowel but doesnt have enough money!')
                            time.sleep(1.3)
                            continue
                        else:
                            print(f'CPU 2 bought vowel {guess}')
                            remove_from_copy(guess)
                            money_cpu2 -= 250 
                            time.sleep(3)
                            occurrences = phrase.count(guess) 
                            if occurrences == 0:
                                print("Letter not found in puzzle!")
                                print()
                                time.sleep(3)
                                break
                            
                            position = -1
                            for occurence in range(occurrences):
                                position = phrase.find(guess, position + 1)
                                
                                if position < len(puzzle):
                                    puzzle[position] = guess
                
                
                
                if next_round == False:
                    print("No one solved the puzzle, the round goes on!")
                    time.sleep(3)
                    continue 


    round += 1
time.sleep(3)
os.system('cls')
print('Game over!!')
print(f"Your score is {score_player}") 
print(f"CPU 1 score is {score_cpu1}")
print(f"CPU 2 score is {score_cpu2}")

with open('wheel_of_fortune_data.txt', 'w', encoding='utf-8') as file:
  file.write(f"Player score = {score_player}\n") 
  file.write(f"CPU 1 score = {score_cpu1}\n")
  file.write(f"CPU 2 score = {score_cpu2}\n")

def restart():
  import ME021_python_project_Chaus_Denys
  ME021_python_project_Chaus_Denys.main()

if __name__ == "__main__":

  while True:
    play_again = input("Play again? (y/n) ")
    if play_again == 'y' or play_again == 'yes':
       restart()
    else:
       print("Thanks for playing!")  
       sys.exit()        
