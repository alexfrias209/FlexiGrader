import random

def person_choose(challenging, you_choose):
    if challenging == "easy":
        option = ["rock", "paper", "scissors"]
        return random.choice(option)
    elif challenging == "hard":
        victory_choice = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        return victory_choice[you_choose]

def your_choice():
    while True:
        you_choose = input("Choose any of your choice: Rock, Paper, or Scissors: ").lower()
        if you_choose in ["rock", "paper", "scissors"]:
            return you_choose
        else:
            print("Wrong option. Choose Rock, Paper, or Scissors.")

def choose_winner(you_choose, Person_option):
    if you_choose == Person_option:
        return "It's a tie!", 0
    elif(you_choose == "rock" and Person_option == "scissors") or (you_choose == "paper" and Person_option == "rock") or (you_choose == "scissors" and Person_option == "paper"):
        return "You win!", 1
    else:
        return "Person wins!", -1

def update_score(you_choose, Person_option, your_update, Person_update): 
    print(f"Your recent update score: {your_update} Person's score: {Person_update}")
    print(f"You chose {you_choose}. Person chose {Person_option}.")
    overall, victory = choose_winner(you_choose, Person_option)
    
    if victory == 1:
        your_update +=1
    elif victory == -1:
        Person_update +=1
        
    print(overall)    
    return overall, your_update, Person_update

your_update = 0
Person_update = 0

while True:
        file = input(f"Do you want to play in a file? (yes/no): ").lower()
        if file not in ["yes", "no"]:
            print("Wrong option. Select a different option.")
            continue
        elif file == "yes":
                with open("59566_6417289_9083822.txt","r") as f:
                    for file_choice in f:
                        print(file_choice)
        elif file == "no":
            you_choose = your_choice()
            challenging = input("Choose challenging level (easy/hard): ").lower()
            if challenging not in ["easy", "hard"]:
                print("Wrong option challenging level. Enter another option.")
                continue
            Person_option = person_choose(challenging, you_choose)
            print(f"Person chose {Person_option}.")

            overall, your_update, Person_update = update_score(you_choose, Person_option, your_update, Person_update)
        
        play_another_round = input("Do you want to play another round? (yes/no): ").lower()
        if play_another_round != "yes":
            print("Exiting")
            break

with open('59566_6417291_6948211.txt', 'w') as file:
    file.write("Person, your_choice\n")
    file.write(f"Your recent update score: {your_update}, Person's score: {Person_update}\n")
