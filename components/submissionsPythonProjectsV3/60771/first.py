import pandas
constellations = pandas.read_csv("constellations.csv")
stars = pandas.read_csv("stars.csv")
eight = pandas.read_csv("eight.csv")


########
######## FUNCTIONS RELATED TO FIRST USER PROMPT (Learn about constellations) ########
########
        
# F&%#$ this function in particular
        #Nevermind it's so good now!! =D
     
#list all of the constellations   
def conta():
    constList = constellations["Constellation"].tolist() #get all the constellations from constellations 
    constFixed = ', '.join(map(str, constList)) #turn list into uhh uhh uhh sentence with cool commas
    print("\nHere is a list of all the constellations within the catalog:\n", constFixed[:-6], " and ", constFixed[-5:]) #this index method works only if the last element is 5 characters
    contaChoice = input("\nWhich do you want to learn about?: ").title() #i love the title command
    if contaChoice in constList: #see if the user spelled it right ig
        constRow = constList.index(contaChoice)
        constRowInfo = constellations.iloc[constRow, :]
        #print meaning of constellations
        if constRowInfo['Zodiac'] != "0": #for zodiacal constellations
            print(f"\nThe constellation {constRowInfo['Constellation']} is a zodiacal constellation that corresponds to the months {constRowInfo['Zodiac']}. The name {constRowInfo['Constellation']} means '{constRowInfo['ConstName']}'." )
        elif constRowInfo['Zodiac'] == "0": #for non-zodiacal constellations
            print(f"\nThe constellation {constRowInfo['Constellation']} means '{constRowInfo['ConstName']}'.")
        print(f"There are {constRowInfo['CatAmount']} stars in the constellation {constRowInfo['Constellation']} recorded in this catalog.")
        contaExit = input(f"\nDo you want to know the stars or return to other topics?\n1. Stars in {constRowInfo['Constellation']}\n2. Return to main menu\n(1/2): ")
    else:
        contaExit = "3"
    if contaExit == "1":
        print()
        relay(contaChoice) #call relay function with the same user input from conta(), this will list the stars in the chosen constellation
    elif contaExit == "2":
        print()
    elif contaExit == "3":
        print("\nYou might have made a typo!")
        conta()
    else:
        print("Sorry! That was not a valid number...")

        
#list stars within a constellation
def relay(constellation=""):
    stars['Name'] = stars['Name'].fillna(stars['Designation'])
    if not constellation:
        relayChoice = input("\nWhich constellation do you want to know the stars of?: ").title()
        result = relay(relayChoice)
        if result in constellations['Constellation'].tolist():
            relay(result)
        elif result == "No":
            print("Returning to main menu.")
            return
        else:
            print("You might have made a typo! Try again.")
            relay()
    else:
        if constellation in constellations['Constellation'].tolist():
                relay_starsDF = stars[stars['Constellation'] == constellation]
                relay_stars = relay_starsDF['Name'].tolist()
                print(f"\nThese are the cataloged stars in the constellation {constellation}:")
                for star in relay_stars:
                    print(f"{star}")
                buffer = input("\nDo you want to learn more names of stars in this constellation? (yes/no): ").lower()
                if buffer == "yes":
                    relay()
                elif buffer == "no" or buffer == "exit":
                    print("\nReturning to the main menu...")
                else:
                    print("\nYou might have made a typo! That's alright, returning to the main menu anyway...")
        elif constellation in eight['Constellation'].values and constellation not in constellations.values:
            print(f"\nWe're so sorry! =(\nYou entered {constellation}, a constellation that isn't in the Super Star Catalog!\nThere are only 41 constellations in this catalog...")   
        else:
            print("b")