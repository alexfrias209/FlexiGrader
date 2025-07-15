import random

def game(): # This entire statement gives me a random number between 1-1000
    score = 0
    blah = True
    while blah == True: # You will be able to play/guess ten times
        print("Will the next number be Higher or Lower? :)")
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        print("Current Number:", num1)
        response = input("Higher or Lower: ").strip().lower() # User inputs either Higher or Lower

        if (num1 < num2 and response == "higher") or (num1 > num2 and response == "lower"): # This depends on the random numbers given 
            print("You Win!")
            score += 1 # The more you guess correctly, you get one point each time
            print("The Next Number was", num2)
        else:
            print("Game Over! The Next Number was", num2)
            print("Your final score is:", score)
            return score # Prints the score 


print("Welcome to the game of Higher or Lower! Guess correctly to achieve a high score!") # Intro/ Welcoming to the game
game() # This function is for the top part 
print("Thank You for Playing :)")

    
