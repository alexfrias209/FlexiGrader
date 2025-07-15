import random #used to generate random letter to guess
import string #used for string functions
import time #used to keep a timer on how long each round takes

#function to pick a random letter for the game
def get_random_letter():
    return random.choice(string.ascii_lowercase)

def addLeaderBoard(leaderboard, name):
    #leaderboard.append(time) #adds time to leaderboard

    leaderboard = sorted(leaderboard) #sorts leaderboard from shortest time to longest time

    f = open("leaderboard.txt", "w")
    for i in range(len(leaderboard)):
        f.write(name +  " - " + str(leaderboard[i]) + ' seconds \n')
    f.close()


#Main function
def main():
    print("Welcome to the Alphabet Letter Guesser Game!")
    leaderboard = []
    name = input('Enter your name: ')

    #while loop to play game and check if user wants to continue with another round after the current round is over
    #will continue to run until the loop is told to break
    while True:
        chosen_letter = get_random_letter() #uses get_random_letter() function to get a random letter to be guessed in the game
        correct = False #used for next while loop to continue to input guesses until correct guess is made, which will turn the boolean to True
        start_time = time.time() #starts timer

        #while loop to continously ask for user input for guesses until the guess matches the random chosen letter
        while not correct:
            user_guess = input("Guess a letter: ").lower() #player is asked too guess a letter

            if ((int(time.time() - start_time)) >= 15) and user_guess == chosen_letter:
                print("You got it but the time has run out!")
                print(f"The correct letter was '{chosen_letter}'.")
                break

            elif ((int(time.time() - start_time)) >= 15) and user_guess != chosen_letter:
                print("The time has run out!")
                print(f"The correct letter was '{chosen_letter}'.")
                break
            
            print(str(int(time.time() - start_time)) + " seconds have past")
            
            #Makes sure that the players inputs a valid letter
            if user_guess not in string.ascii_lowercase:
                print("Please enter a valid letter.")

            #If the guess matches the chosen letter then you have completed the game and the time is ended
            elif user_guess == chosen_letter:
                end_time = time.time() #ends timer
                total = int(end_time - start_time)
                print(f"Congratulations! You guessed the correct letter '{chosen_letter}'.")
                print(f"You took " + str(total) + " seconds!" )

                leaderboard.append(total)
                addLeaderBoard(leaderboard, name)
                correct = True

            elif user_guess < chosen_letter: #your guess is too low
                print("Your guess is lower in the alphabet. Guess higher")

            else: #your guess is too high
                print("Your guess is higher in the alphabet. Guess lower")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()

        if play_again != 'yes'.lower():
            print("Thanks for playing!")
            break

#checks whether the script is being run as the main program
if __name__ == "__main__": 
    main()