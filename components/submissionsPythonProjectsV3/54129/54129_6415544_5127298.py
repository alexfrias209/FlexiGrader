
# introduction # 
print("\nWelcome to online Rock Paper Scissors!!\nDeveloped by blah!\n\nMay the odds be in your favor..Goodluck!\n")

user_name = input("Enter your name: ")
print("Welcome,",user_name)

# random pick for AI #
import random
 
# game results output # 
def Game():
        comp = random.randint(1,3)
        winner = "\nCongradulations! You WIN!!!"
        loss = "\nYou lost. Better luck nect time!"
        tie = "\nYou got lucky..It's a draw."

# stating game play choices #
        choice = int(input("Enter a number 1- 3 to choose your play\n1. Rock\n2. Paper\n3. Scissors\nI'll take my luck with: "))
        list = [comp,choice]
 
# game play chosen by user #
        if choice == 1:
            playerChoice = "Rock"
            print("\nYou chose:", playerChoice)
        if choice == 2:
            playerChoice = "Paper"
            print("\nYou chose:", playerChoice)
        if choice == 3:
            playerChoice = "Scissors"
            print("\nYou chose:", playerChoice)
 
 
# AI's random chosen #
        if comp == 1:
            compChoice = "Rock"
            print("\nAI chose:", compChoice)
        if comp == 2:
            compChoice = "Paper"
            print("\nAI chose:", compChoice)
        if comp == 3:
            compChoice = "Scissors"
            print("\nAI chose:", compChoice)

# possible options and results # 
        if list == [1,1]:
            print("\nYou got lucky..It's a draw.")
            return "draw"
        elif list == [1,2]:
            print("\nCongradulations! You WIN!!!")
            return "win"
        elif list == [1,3]:
            print("\nYou lost. Better luck next time!")
            return "lost"
        elif list == [2,1]:
            print("\nYou lost. Better luck next time!")
            return "lost"
        elif list == [2,2]:
            print("\nYou got lucky..It's a draw.")
            return "draw"
        elif list == [2,3]:
            print("\nCongradulations! You WIN!!!")
            return "win"
        elif list == [3,1]:
            print("\nCongradulations! You WIN!!!")
            return "win"
        elif list == [3,2]:
            print("\nYou lost. Better luck next time!")
            return "lost"
        elif list == [3,3]:
            print("\nYou got lucky..It's a draw.")
            return "draw"
        else:
            print("Invalid option. Please choose a listed number.")


# starting scoreboard of 0 #
win = 0
lost = 0
draw = 0


while True:

    # Score board #
    print("\nWins =", win)
    print("Losses =", lost)
    print("Draws =", draw, "\n")


    result = Game()
    if result == "win":
        win += 1
    if result == "draw":
        draw += 1
    if result == "lost":
        lost += 1


    again = input("\nPlay again? Y/N\n")
    if again.upper() == "Y":
        continue
    else:
        file = open('final_score.txt', 'a')
        file.write(user_name + " scored " + str(win) + "\n")
        file.close()
    
        print("\nThanks for playing!!")

    # Read and print the contents of the file
        with open('final_score.txt', 'r') as file:
            contents = file.read(win)
            name = user_name
            print(user_name + ',' + ' your final score is: ' + str(win))
    
        break
