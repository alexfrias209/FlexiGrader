import random

# Function to simulate a delivery by the computer
def computer_delivery():
    return random.randint(1, 6)

# Main game loop
runs_scored = 0
wickets_lost = 0
computer_runs_scored  0
computer_wickets_lost = 0

print("Welcome to Finger Cricket!")
print("You are batting. Choose your shot (1-6) or enter 0 to quit.")
print("You have 5 wickets in hand.")

while wickets_lost < 5:
    user_choice = int(input("Your choice: "))
    if user_choice < 0 or user_choice > 6:
        print("Invalid choice. Game Over.")
        print("")
        break
    
    computer_delivery_result = computer_delivery()
    print(f"Computer's choice: {computer_delivery_result}")
    
    if user_choice == computer_delivery_result:
        print("You're out!")
        print("")
        wickets_lost += 1
    else:
        runs_scored += user_choice
        print("")

    if wickets_lost >= 5:
        print("All your wickets are down. Your innings is over.")
        print("")
        break

print(f"You scored {runs_scored} runs.")

print("Now, you need to chase the computer's score.")
print(f"The computer scored {runs_scored} runs.")

while computer_wickets_lost < 5 and computer_runs_scored < runs_scored:
    computer_delivery_result = computer_delivery()
    user_choice = int(input("Your choice: "))

    if user_choice < 0 or user_choice > 6:
        print("Invalid choice. Game Over.")
        print("")
        break

    print(f"Computer's choice: {computer_delivery_result}")

    if user_choice == computer_delivery_result:
        print("Computer is out!")
        print("")
        computer_wickets_lost += 1
    else:
        computer_runs_scored += computer_delivery_result

print(f"Computer scored {computer_runs_scored} runs.")

if runs_scored > computer_runs_scored:
    print("Congratulations! You won!")
elif runs_scored < computer_runs_scored:
    print("You lost. Better luck next time.")
else:
    print("It's a tie!")

print("Thanks for playing Finger Cricket!")