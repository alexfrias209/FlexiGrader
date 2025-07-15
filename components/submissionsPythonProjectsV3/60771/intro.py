intro_token = 0
from first import *
from second import *
from third import *
from search import *

######## INTRO FUNCTIONS (If these don't work then nothing will)########
#introduce user to the program
def introduction():
    print("   ✦       ✦       ✦       ✦       ✦       ✦       ✦       ✦       ✦       ✦")
    print("✧      ✧       ✧       ✧       ✧       ✧       ✧       ✧       ✧       ✧       ✧")
    print("This is the Super Star Catalog, a small database containing information on stars and constellations.")
    print("✧      ✧       ✧       ✧       ✧       ✧       ✧       ✧       ✧       ✧       ✧")
    print("   ✦       ✦       ✦       ✦       ✦       ✦       ✦       ✦       ✦       ✦")
    print("Here you can learn about:\n1. Constellations ⁂\n2. Characteristics of stars ⭑\n3. Stars in a constellation ✰\n4. Find a star ⭒")

#provide main menu to user
def menu(): #this is the most important function lole
    global intro_token #global variable now in the function
    if intro_token < 1: #dynamic introduction
        introduction()
        intro_token += 1
        choice = input("\nWhat would you like to learn about? (1/2/3/4): ")
    elif intro_token >= 1:
        choice = input("\nWhat else would you like to learn about?\n1. Constellations ⁂\n2. Characteristics of stars ⭑\n3. Stars in a constellation ✰\n4. Find a star ⭒\n (1/2/3/4): ")
#option 1: information on constellations
    if choice == "1": #relay and conta GOAT debate
        relayConta = int(input("\nDo you want to learn about the constellations of the stars within them?\n1. Names of constellations\n2. Stars of a specific constellation\n3. Return to other topics\n(1/2/3): "))
        if relayConta == 1:
            conta()
            menu()
        elif relayConta == 2:
            relay()
            menu()
        elif relayConta == 3:
            menu()
        else:
            print("Sorry, but that wasn't a valid number! (If it was even a number...)")
            menu()
#option 2: information on the characteristics of stars
    elif choice == "2":
        wendigo = input("\nDo you want to learn about the characteristics of stars or search for stars?\n1. Star characteristics\n2. Plot all stars in catalog in HR format\n3. Return to other topics\n(1/2/3): ")
        if wendigo == "1":
            aspect_file = "aspect.txt" #store .txt in variable
            characteristics, aspect_descriptions = readAspect(aspect_file)
            while True:
                print() #whitespace for legibility
                listCharacteristics(characteristics)  #function to list characteristics, each characteristic is called in argument
                char_choice = input("\nEnter the name of the characteristic you want to learn about: ").title() #ask for a characteristic; capitalize input
                if char_choice.lower() == "exit": #user has option to break loop here
                    break
                elif char_choice in aspect_descriptions:
                    print()
                    getAspect(char_choice, aspect_descriptions) #print the description of the inputted description
#this is the answer
                    exo_choice = input("\nDo you want to learn about the other characteristics of stars? (yes/no): ") #just a buffer so the user is not bombarded by text immediately
                    if exo_choice.lower() == "yes":
                        continue #This works because ummmm
                    if exo_choice.lower() in ["exit", "no"]:
                        return menu()
                else:
                    print(f"\nSorry! {char_choice} wasn't a valid choice. What you entered either wasn't the correct number, or a number at all...")
        elif wendigo == "2":
            print("Plotting a Hertzsprung-Russell Diagram of the Super Star Catalog...")
            mainSequence()
            menu()
        elif wendigo == "3":
            menu()
        else:
            print("\nAre you sure you entered in a number? It's okay if you didn't. Returning to main menu...\n")
            menu()
#option 3: enter a constellation and get detailed information on stars
    elif choice == "3":
        starSearch()
        menu()
#option 4: enter the name of a star
    elif choice == "4":

        findaStar()
        menu()
    elif choice == "5":
        leave = input("Are you sure you want to exit the catalog?: ").lower()
        if leave == "yes":
            print("\n             ✦       ✦       ✦       ✦       ✦       ✦       ✦")
            print("          ✧      ✧       ✧       ✧       ✧       ✧       ✧       ✧")
            print("             ✦       ✦       ✦       ✦       ✦       ✦       ✦")
            print("                  Thanks for using the Super Star Catalog!")
            print("             ✦       ✦       ✦       ✦       ✦       ✦       ✦")
            print("          ✧      ✧       ✧       ✧       ✧       ✧       ✧       ✧")
            print("             ✦       ✦       ✦       ✦       ✦       ✦       ✦")
            aqz=input("نُجْوُم")
            quit()
        else:
            menu()
    else:
        print(f"\nSorry! {choice} wasn't a valid choice. What you entered either wasn't the correct number, or a number at all...")
        menu()