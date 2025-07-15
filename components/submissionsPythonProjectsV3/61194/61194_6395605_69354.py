import random
print ('Welcome to the coin toss game! Whoever wins 3 times first wins! \n')\

computer_score= 0
user_score= 0
coin= ["Heads" , "Tails"]

def check_the_winner(user_guess, computer_call):
    if(user_guess == "Heads" and computer_call == "Heads"):
        print('It was heads! You guessed it!')
        return "User"
    elif(user_guess == "Tails" and computer_call == "Tails"):
        print('It was tails! You guessed it!')
        return "User"
    elif(user_guess == "Heads" and computer_call == "Tails"):
        print ('It was tails! Sorry you did not guess it.')
        return "Computer"
    elif(user_guess == "Tails" and computer_call == "Heads"):
        print ('It was heads! Sorry you did not guess it.')
        return "Computer"


while(computer_score != 3 and user_score != 3):
    while True:
        user_guess= input('Flip a coin! Heads or Tails?: \n')
        if(user_guess == "Heads" or user_guess == "Tails"):
            break
        else:
            print ('Sorry that is not a valid input, please enter "Heads" or "Tails."')

    computer_call= random.choice(coin)

    print('Your guess: ', user_guess)
    print('Coin flip result: ', computer_call)
    result= check_the_winner(user_guess, computer_call)
    if (result == "User"):
        user_score += 1
    elif (result == "Computer"):
        computer_score += 1
    print ('Your score: ', user_score, 'Computer: ', computer_score)

print('Game over! Thank you for playing!')
    

    
        
