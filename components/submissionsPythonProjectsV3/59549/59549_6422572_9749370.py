import csv

def recommendation(lines):
    try: 
      if bearings == lines[0].strips() and truck == lines[1].strip() and deck == line[2].strips() and wheels == line[3].strips() and price > int(lines[4])  :
      print("You should try this", lines)
        return 
    except: 
        return 


def get_bearings():
    print("\nPlease enter the bearings: ")
    options = ["REDs", "bones swiss ceramic", "Andale Blues Bearings", "Bronson Speed Co "]
    for idx, option in enumerate(options, 1): 
        print(f"{idx}. {option}")

    choice = input("Enter prefered bearings (1-4): ")
    if 1 <= int(choice) <=4: 
        return options [int(choice) - 1]
    else:
        print("Invalid choice")
        quit()

def get_trucks():
    print("\nPlease enter the bearings: ")
    options = ["Venture", "Independent", "Aces", "Thunder "]
    for idx, option in enumerate(options, 1): 
        print(f"{idx}. {option}")

    choice = input("Enter prefered trucks (1-4): ")
    if 1 <= int(choice) <=4: 
        return options [int(choice) - 1]
    else:
        print("Invalid choice")
        quit()

def get_deck():
    print("\nPlease enter the deck: ")
    options = ["Baker", "Powell Peralta", "Zero", "Creature"]
    for idx, option in enumerate(options, 1): 
        print(f"{idx}. {option}")

    choice = input("Enter prefered deck (1-4): ")
    if 1 <= int(choice) <=4: 
        return options [int(choice) - 1]
    else:
        print("Invalid choice")
        quit()

def get_wheels():
    print("\nPlease enter the wheels: ")
    options = ["Spitfire", "Orbs", "Powell Peralta", "Ricta Framework Sparx"]
    for idx, option in enumerate(options, 1): 
        print(f"{idx}. {option}")

    choice = input("Enter prefered wheels (1-4): ")
    if 1 <= int(choice) <=4: 
        return options [int(choice) - 1]
    else:
        print("Invalid choice")
        quit()

def get_prices():
    print("\nPlease enter the price: ")
    options = ["$130", "$311", "$200", "$145"]
    for idx, option in enumerate(options, 1): 
        print(f"{idx}. {option}")

    choice = input("Enter prefered price (1-4): ")
    if 1 <= int(choice) <=4: 
        return options [int(choice) - 1]
    else:
        print("Invalid choice")
        quit()


print("Hello welcome to 'Skateboard recommendations" )

bearings = input("Please enter the bearings: ")
trucks = input("please enter trucks: ")
deck = input("Please enter the deck: ")
wheels = input("Please enter the wheels: ")
prices = input("What is your maximum price: ")

with open('jo/boarss.csv', mode = 'r') as files:
    csvFile = csv.reader(file)
    nesr(csvFile)
    for lines in csvFile:
        recommendation(lines)