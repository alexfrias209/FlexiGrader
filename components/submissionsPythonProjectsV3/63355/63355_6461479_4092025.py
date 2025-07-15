import random
history = []
def NumberGuesser():

    # Game loop until number is found
    while True:
        if (len(history) != 0):
            for i, attemps in enumerate(history):
                print('Game {}: {} attempts'.format(i+1, history[i]))
        output_num = random.randint(1, 10)
        #Total attempts in games history then display 
        randomTarget(output_num)
        nextRound = input('Do you want to play again? Y/N: '); 
        if nextRound.upper() != 'Y':
            break 
#The game is now ended
#Number Guessing Range
def randomTarget(target):
    currentAttemps = 0
    print('A random number has been chosen from 1 to 10. ')
    while True: 
        guess = input('What is the number? (1-10): ')
        guess = int(guess)
        currentAttemps += 1
        #adds an attempt after each game is finished
        #guessing ranges 
        if guess != target:
            distance = abs(guess - target)
            if distance > 5:
                print('Very cold')
            elif distance >= 4 and distance <= 5:
                print('Cold')
            elif distance >= 2 and distance <= 3:
                print('Hot')
            elif distance == 1: 
                print('Very Hot')
        else: 
            print('Hooray! You guess the number from (1-10) in {} attempts.'.format(currentAttemps))
            history.append(currentAttemps)
            break
NumberGuesser()