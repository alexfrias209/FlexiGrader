import csv
# start by importing file 
csv_file = 'quiz_results.csv'

def save_quiz_results(quiz_name, results): 
    with open(csv_file, mode='a', newline='') as file: #opening the file
        writer = csv.writer(file)
        writer.writerow([quiz_name, results]) #in order to update my scores

personality_tests = {
    "Which Superpower is Best for You?": {
        "Flight": 0,
        "Super Strength": 0,
        "Telepathy": 0,
        "Invisibility": 0
    },
    "Which Disney Character Are You?": {
        "Mickey Mouse": 0,
        "Donald Duck": 0,
        "Goofy": 0,
        "Belle": 0
    },
    "Which Friends Character Are You?": {
        "Rachel": 0,
        "Ross": 0,
        "Monica": 0,
        "Joey": 0
    }, 
}

print("Welcome to Personality Quiz Homepage! \nChoose which action you want to take!")

def main_menu():
    print("\nMain Menu:")
    print("1. Personality Quiz")
    print("2. Exit")

    choice = input("\nEnter your choice (1/2):")

    if choice == "1":
        personality_quiz_menu()
    elif choice == "2":
        print('Goodbye.')
    else:
        print("Please choose from the list.")
    
def personality_quiz_menu():
    print("\nPersonality Quiz Menu:")
    print("1. Which Superpower is Best for You?")
    print("2. Which Disney Character Are You?")
    print("3. Which Friends Character Are You?")
    print("4. Back to the Main Menu")
    
    choice = input("\nEnter your choice (1/2/3/4)")
    if choice == "1":
        print("\nYou chose: Which Superpower is Best for You?")
        Superpower_menu()
    elif choice == "2":
        print("\nYou chose: Which Disney Character Are You?")
        Disney_menu()
    elif choice == "3":
        print("\nYou chose: Which Friends Character Are You?")
        Friends_menu()
    elif choice == "4":
        print("\nYou chose: Back to the Main Menu")
        main_menu()
    else:
        print("Please choose from the list.")
        
def Superpower_menu():
    print("Welcome to the 'Which Superpower is Best for You?' Quiz!")
#create dictionary to use key at the end
    superpowers = {   
        "Flight": 0,
        "Super Strength": 0,
        "Telepathy": 0,
        "Invisibility": 0  
    }

    for power in superpowers:
        answer = input(f"\nAre you scared of heights? (yes/no): ").lower()
        if answer == "yes":
            superpowers["Super Strength"] += 1
            superpowers["Telepathy"] += 1
            superpowers["Invisibility"] += 1
        elif answer == "no":
            superpowers["Flight"] += 1
            
        answer = input(f"Are you an introvert? (yes/no): ").lower()
        if answer == "yes":
            superpowers["Invisibility"] += 1
        elif answer == "no":
            superpowers["Super Strength"] += 1
            superpowers["Telepathy"] += 1
            superpowers["Flight"] += 1
            
        answer = input(f"Are you active? (yes/no): ").lower()
        if answer == "yes":
            superpowers["Super Strength"] += 1
        elif answer == "no":
            superpowers["Telepathy"] += 1
            superpowers["Invisibility"] += 1
            superpowers["Flight"] += 1
        break
            
    best_superpower = max(superpowers, key=superpowers.get)#use key statement to sort the highest valued answered (which is the result)

    print(f"Based on your answers, the best superpower for you is: {best_superpower}!")
    save_quiz_results("Which Superpower is Best for You?", best_superpower)

def Disney_menu():
    print("Welcome to the 'Which Disney Character Are You?' Quiz!")

    disney = {
        "Mickey Mouse": 0,
        "Donald Duck": 0,
        "Goofy": 0,
        "Belle": 0
    }
    
    questions = [
        "Q1: How would your friends describe you?",
        "Q2: What is your favorite color?",
        "Q3: What do you do on your free time?",
        "Q4: What's your ideal vacation spot"
    ]

    options = [
        ["Short fused", "Optimistic", "Clumsy", "Kind"],
        ["Red", "Blue", "Yellow", "Green"],
        ["Read", "Hang out with friends", "Dance", "Act"],
        ["Beach", "Mountains", "City", "Forest"]
    ]

    answers = {
        "Mickey Mouse": [2, 1, 3, 4],
        "Donald Duck": [1, 2, 4, 3],
        "Goofy": [3, 4, 2, 1],
        "Belle": [4, 3, 1, 2]
    }

    for i, question in enumerate(questions): #used for loop to pair questions with options in the output
        print(question)
        for j, option in enumerate(options[i]): #enumerate is best used since it will output the first line with the first question
            print(f"{j + 1}. {option}")

        response = int(input("Enter the number of your choice (1-4): "))

        for character, score in disney.items():
            disney[character] += answers[character][response - 1]

    result = max(disney, key=disney.get)

    print("You are... ", result, "!")
    save_quiz_results("Which Disney Character Are You?", result)
    
def Friends_menu():
    print("Welcome to the 'Which Friends Character Are You?' Quiz!")

    friends = {
        "Rachel": 0,
        "Ross": 0,
        "Monica": 0,
        "Joey": 0
    }
    
    questions = [
        "Q1: What is your dream job?",
        "Q2: What is your favorite color?",
        "Q3: What do you do on your free time?",
        "Q4: What's your ideal vacation spot"
    ]

    options = [
        ["Paleontologist", "Fashion Buyer", "Chef", "Actor"],
        ["Blue", "Green", "Orange", "Red"],
        ["Read", "Hang out with friends", "Dance", "Act"],
        ["The Bahamas", "Las Vegas", "A Museum", "Paris"]
    ]

    answers = {
        "Rachel": [2, 1, 3, 4],
        "Ross": [1, 2, 4, 3],
        "Monica": [3, 4, 2, 1],
        "Joey": [4, 3, 1, 2]
    }

    for i, question in enumerate(questions):
        print(question)
        for j, option in enumerate(options[i]):
            print(f"{j + 1}. {option}")

        response = int(input("Enter the number of your choice (1-4): "))


        for character, score in friends.items():
            friends[character] += answers[character][response - 1]


    result = max(friends, key=friends.get)

    print("You are... ", result, "!")
    save_quiz_results("Which Friends Character Are You?", result)

if __name__ == "__main__":
    main_menu()
