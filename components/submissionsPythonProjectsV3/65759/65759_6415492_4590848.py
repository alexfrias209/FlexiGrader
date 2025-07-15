import random #random number generator import
import matplotlib.pyplot as plt #graph for the probability and outcome

#all the dice sides
dice_12 = {
     1: ("  / \   ",
        " /   \  ",
        "/  1  \ ",
        "\     / ",
        " \   /  ",
        "  ───   "),
     2: ("  / \   ",
        " /   \  ",
        "/  2  \ ",
        "\     / ",
        " \   /  ",
        "  ───   "),
     3: ("  / \   ",
        " /   \  ",
        "/  3  \ ",
        "\     / ",
        " \   /  ",
        "  ───   "),
     4: ("  / \   ",
        " /   \  ",
        "/  4  \ ",
        "\     / ",
        " \   /  ",
        "  ───   "),
     5: ("  / \   ",
        " /   \  ",
        "/  5  \ ",
        "\     / ",
        " \   /  ",
        "  ───   "),  
     6: ("  / \   ",
        " /   \  ",
        "/  6  \ ",
        "\     / ",
        " \   /  ",
        "  ───   "),
     7: ("  / \   ",
        " /   \  ",
        "/  7  \ ",
        "\     / ",
        " \   /  ",
        "  ───   "),
     8: ("  / \   ",
        " /   \  ",
        "/  8  \ ",
        "\     / ",
        " \   /  ",
        "  ───   "),
     9: ("  / \   ",
        " /   \  ",
        "/  9  \ ",
        "\     / ",
        " \   /  ",
        "  ───   "),
     10: ("  / \   ",
        " /   \  ",
        "/ 10  \ ",
        "\     / ",
        " \   /  ",
        "  ───   "),
     11: ("  / \   ",
        " /   \  ",
        "/ 11  \ ",
        "\     / ",
        " \   /  ",
        "  ───   "),
     12: ("  / \   ",
        " /   \  ",
        "/ 12  \ ",
        "\     / ",
        " \   /  ",
        "  ───   ")
}

dice_20 = {
     1: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│  1  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     2: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│  2  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     3: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│  3  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     4: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│  4  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     5: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│  5  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     6: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│  6  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     7: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│  7  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     8: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│  8  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     9: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│  9  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     10: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│ 10  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     11: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│ 11  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     12: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│ 12  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     13: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│ 13  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     14: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│  14 | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     15: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│ 15  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     16: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│ 16  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     17: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│ 17  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     18: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│ 18  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     19: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│ 19  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
     20: ("  / \   ", 
         " /   \  ", 
         "/     \ ", 
         "│ 20  | ", 
         "|     | ", 
         " \   /  ", 
         "  \ /   "),
}

dice_10 = {
     1: ("  / \   ",
        " /   \  ",
        "/  1  \ ",
        "─────── "),
     2: ("  / \   ",
        " /   \  ",
        "/  2  \ ",
        "─────── "),
     3: ("  / \   ",
        " /   \  ",
        "/  3  \ ",
        "─────── "),
     4: ("  / \   ",
        " /   \  ",
        "/  4  \ ",
        "─────── "),
     5: ("  / \   ",
        " /   \  ",
        "/  5  \ ",
        "─────── "), 
     6: ("  / \   ",
        " /   \  ",
        "/  6  \ ",
        "─────── "),
     7: ("  / \   ",
        " /   \  ",
        "/  7  \ ",
        "─────── "),
     8: ("  / \   ",
        " /   \  ",
        "/  8  \ ",
        "─────── "),
     9: ("  / \   ",
        " /   \  ",
        "/  9  \ ",
        "─────── "),
     10: ("  / \   ",
        " /   \  ",
        "/ 10  \ ",
        "─────── ")
}

dice_8 = {
     1: ("  / \   ",
        " /   \  ",
        "/  1  \ ",
        "─────── "),
     2: ("  / \   ",
        " /   \  ",
        "/  2  \ ",
        "─────── "),
     3: ("  / \   ",
        " /   \  ",
        "/  3  \ ",
        "─────── "),
     4: ("  / \   ",
        " /   \  ",
        "/  4  \ ",
        "─────── "),
     5: ("  / \   ",
        " /   \  ",
        "/  5  \ ",
        "─────── "), 
     6: ("  / \   ",
        " /   \  ",
        "/  6  \ ",
        "─────── "),
     7: ("  / \   ",
        " /   \  ",
        "/  7  \ ",
        "─────── "),
     8: ("  / \   ",
        " /   \  ",
        "/  8  \ ",
        "─────── ")
}

dice_4 = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice_6 = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

#modularizing
def pattern_print_dice(dice_side_pats):
    for row in dice_side_pats:
        print(row)

def user_choice_dice_maker(number_sides, dice_side_pats, value):
    pattern_with_value = [line.replace("x", str(value)) for line in dice_side_pats]
    custom_dice = {
        f"result {value}": pattern_with_value,
    }
    return custom_dice

def read_saved_rolls(): #file
    with open("SavedRolls.txt", "r") as file:
        rolls = file.readlines()
    return rolls

def roll_types_sort(rolls):
    sorting_catagor_dice = {}
    for roll in rolls:
        divided_comp_roll = roll.strip().split(":")
        if len(divided_comp_roll) == 2:
            dice_type, value = divided_comp_roll[0].strip(), int(divided_comp_roll[1].strip())
            if dice_type not in sorting_catagor_dice:
                sorting_catagor_dice[dice_type] = []
            sorting_catagor_dice[dice_type].append(value)
    return sorting_catagor_dice

def plot_probability_distribution(sorting_catagor_dice): #graph portion
    for category, rolls in sorting_catagor_dice.items():
        number_sides = max(rolls)
        outcome = list(range(1, number_sides + 1))
        probabilities = [rolls.count(i) / len(rolls) for i in outcome]

        plt.bar(outcome, probabilities)
        plt.title(f"distributed prob dicetype: ({category})")
        plt.xlabel("heres the outcome =^w^=")
        plt.ylabel("y axis of probability")
        plt.show()

def word_menu():
    print("Haii :3 My name is Maria, welcome to my project\nmy project is gonna have different dice you can pick and will spin one of them for you,\nwhich will then save the value before asking if you wanna spin again or pick another dice or if you're all done!")
    print()
    print("okie so ima need u to choose some options for me!\n")
    print("1. Lotta sides!!! (big dice!)")  # first choices
    print("2. Meh average sides (medium dice) ¯\_(ツ)_/¯")
    print("3. Just a wittle bit (smol dice) 👉👈")
    print("4. Personalized dice?")
    print("5. See previous rolls")
    print("6. Probability graph checker?\n")

while True: #while loop start
    word_menu()
    type_dice = input("okay now pick!: ") #detailed choices here
    print()

    dice = []
    base = 1 #number of dice is constantly 1 bc you're only rolling one dice at a time
    total = 0

    if type_dice == "1": #d12 and d20 here
        print("Okie dokie artichokie! pick ya dice :D")
        print("1. D12")
        print("2. D20")
        lotta_dice = input("lemme get ya number!\n")

        if lotta_dice == "1": #d12
            print("D12? if u say so!\n")
#random number generator
            dice.append(random.randint(1, 12)) #random.randint is what generates the random number within the range
            for die in range(base):
                for line in dice_12.get(dice[die]):
                    print(line)
            for die in dice:
                total += die
            with open("SavedRolls.txt", "a") as file: # makes or opens file of saved rolls
                file.write("D12: " + str(total) +"\n")


        elif lotta_dice == "2": #D20
            print("D20? may the odds ever be in your favor!\n")
            dice.append(random.randint(1, 20)) 
            for die in range(base):
                for line in dice_20.get(dice[die]):
                    print(line)
            for die in dice:
                total += die
            with open("SavedRolls.txt", "a") as file: # makes or opens file of saved rolls
                file.write("D20: " + str(total) +"\n")


    elif type_dice == "2": #d8 and d10 here
            print("Mhm I see! Can u tell me more?")
            print("1. D8")
            print("2. D10")
            mid_dice = input("So what'll it be?\n")

            if mid_dice == "1": #D8
                print("D8? Hmm, okay u do u boo!👻\n")
                dice.append(random.randint(1, 8)) 
                for die in range(base):
                    for line in dice_8.get(dice[die]):
                        print(line)
                for die in dice:
                    total += die
                with open("SavedRolls.txt", "a") as file:
                    file.write("D8: " + str(total) +"\n")


            elif mid_dice == "2": #d10
                print("You want d10? Solid choice for a solid dice 😎👍\n")
                dice.append(random.randint(1, 10)) 
                for die in range(base):
                    for line in dice_10.get(dice[die]):
                        print(line)
                for die in dice:
                    total += die
                with open("SavedRolls.txt", "a") as file:
                    file.write("D10: " + str(total) +"\n")


    elif type_dice == "3": #d4 and d6 here
            print("You chose Minimal sides? Must be some board game🥱😴")
            print("1. D4")
            print("2. D6")
            minimal_choice = input("alrighty whatcha want?\n ")

            if minimal_choice == "1": #D4
                print("Awww D4? its so smol =>w<=!!!\n")
                dice.append(random.randint(1, 4)) 
                for die in range(base):
                    for line in dice_4.get(dice[die]):
                        print(line)
                for die in dice: 
                    total += die
                with open("SavedRolls.txt", "a") as file:
                    file.write("D4: " + str(total) +"\n")


            elif minimal_choice == "2": #D6
                print("D6? Good ol'reliable🤠!!!\n")
                dice.append(random.randint(1, 6)) 
                for die in range(base):
                    for line in dice_6.get(dice[die]):
                        print(line)
                for die in dice:
                    total += die
                with open("SavedRolls.txt", "a") as file:
                    file.write("D6: " + str(total) +"\n")
    

    elif type_dice == "4":
        num_sides = int(input("how many sides are on the custom dice?:"))
        print()
        #make all previous dice sides a choice for the user to customize
        user_dice_preference = [
            ("┌─────────┐",
             "│         │",
             "│    x    │",
             "│         │",
             "└─────────┘"),

            ("  / \   ",
             " / x \  ",
             "/     \ ",
             "─────── "),

            ("  / \   ", 
             " /   \  ", 
             "/     \ ", 
             "│  x  | ", 
             "|     | ", 
             " \   /  ", 
             "  \ /   "),

            ("  / \   ",
             " /   \  ",
             "/  x  \ ",
             "\     / ",
             " \   /  ",
             "  ───   ")
        ]

        print("which pattern would u want to pair with it :O?\n")
        for i, pattern in enumerate(user_dice_preference): #helps know what choice the userpicks
            print(f"{i + 1}.")
            pattern_print_dice(pattern)
            print()

        chosen_pattern = int(input("please put the number of the pattern that u want:D"))
        print()
        if 1 <= chosen_pattern <= len(user_dice_preference):
            value = random.randint(1, num_sides)
            custom_dice = user_choice_dice_maker(num_sides, user_dice_preference[chosen_pattern - 1], value)

            print("Nice dice you got there! ^u^ \n")
            for side, pattern in custom_dice.items():
                print(f"{side}:")
                pattern_print_dice(pattern)

            dice.append(value)
            total = value

            with open("SavedRolls.txt", "a") as file:
                file.write(f"User invented D{num_sides}: {value}\n")


    elif type_dice == "5": #previous roll recall file
            print("Showing previous rolls made:\n")
            with open("SavedRolls.txt", "r") as file:
                prior_rolling = file.readlines()
                for roll in prior_rolling:
                    print(roll)

    elif type_dice == "6":  #graphs for the saved results
        print("please wait as i grab crayons to color in the probability graphs...")
        rolls = read_saved_rolls()
        dice_categories = roll_types_sort(rolls)
        plot_probability_distribution(dice_categories)

    play_again = input("Do wanna spin again/pick another dice? please respond with y/n\n") #while loop end here
    
    if play_again != "y":
        print("Oh okay! Well thanks for stoppin by ig 👋👋👋!")
        break