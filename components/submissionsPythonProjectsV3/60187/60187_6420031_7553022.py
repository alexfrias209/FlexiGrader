

def main():
    #Introduction to the program
    print("Recipe suggestor finder")
    print("What type of meat do you have?")
    print("1. Carne Asada  2.Chicken  3.Lengua")

    #selected item
    meat = 0
    veg = 0
    extra = 0

    #menus for the types of ingredients
    meatChoice = ["Carne Asada", "Chicken", "Lengua"]
    vegChoice = ["Cilantro", "Onions", "Tomatoes", "Lettuce"]
    extraChoice = ["salsa", "cheese","granos"]
    meal = ["tacos",  "quesidillas", "pozole",]

    #prompts the user to input which type of meat they have
    meat = checkNum(meatChoice)

    #asks for type of vegetable
    print("What kind of vegetable/fruit do you have?")
    print("1. Cilantro  2.Onions  3.Tomatoes  4.Lettuce")
    
    #prompts user to input which type of vegetable they have
    veg = checkNum(vegChoice)

    #asks for other inredients user may have
    print("What else do you have?")
    print("1. salsa,  2.Cheese,  3.granos")
    
    #prompts user to input any extra ingredient that is listed
    extra = checkNum(extraChoice)

    #tells what kind of food can be made based on their input
    print("You can make " + meal[extra-1] + " with " + meatChoice[meat-1] + ", " + vegChoice[veg-1] + ", and " + extraChoice[extra-1])

def checkNum(options):
    wrongNum = True
    while (wrongNum):
        #Creates the prompt for which numbers the user is allowed to input
        print("Enter your chocie (", end="")
        for i in range(len(options)):
            print(i+1,end="/")
        num = int(input("): "))
        
        #Loops through the menu to check if the number that was inputted is valid
        for i in range(len(options)):
            if (num != (i+1)):
                wrongNum = True
            
            else:
                wrongNum = False
                break
    
        if(wrongNum == False):
            break
        print("Invalid input. Please try again.")

    #returns the item the user selected
    return num

main()
