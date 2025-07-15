import pandas
constellations = pandas.read_csv("constellations.csv")
stars = pandas.read_csv("stars.csv")
eight = pandas.read_csv("eight.csv")

########
######## FUNCTIONS RELATED TO THIRD USER PROMPT #########
########
        
#function for find a star
def starSearch(option3token = 0):
    eighty = eight["Constellation"].tolist() #get the full 88 constellations from eight
    constList = constellations["Constellation"].tolist() #get all the constellations from constellations (this line is borrowed from the conta function)
    while True:
        if option3token == 0: #i did this so that navigating the menus feels a little more dynamic
            constellation = input("\nIf you know the name of a constellation, enter it here!\n(If you don't, enter 'idk' to get a list, or 'exit' to return to main menu): ").title()
        elif option3token >= 0:
            constellation = input("\nIf you know the name of another constellation, enter it here!\n(If you don't, enter 'idk' to get a list, or 'exit' to return to main menu): ").title()
        
        if constellation in eighty:
            if constellation in constList:
                stars_in_constellation = stars[stars['Constellation'] == constellation]
                print(stars_in_constellation)
                print(f"\nThe stars in {constellation} have been written to {constellation}.csv")
                stars_in_constellation.to_csv(str(constellation)+".csv")
                """
                print(f"\nStars in the constellation {constellation}:\n")
            #iterate over stars_in_constellation
                for index, row in stars_in_constellation.iterrows():
                    name = row['Name']
                    meaning = row['Meaning']
                    desig = row['Designation']
                    spectral = row['Spectral']
                    radius = row['Radius']
                    mass = row['Mass']
                    temp = row['Temperature']
                    distance = row['Distance']
                    age = row['Age']
                    app = row['Apparent']
                    absM = row['Absolute']
                    lum = row['Luminosity']
                    color = row['Color']
                    size = row['Class']
            #This series of if and elif branches provides accurate descriptions of the stars that will be printed.
                    #I was going to try to make this more concise but it is fine in my opinion...
                    if not pandas.isna(row['Name']) and not pandas.isna(row['Meaning']): #check if the has a name and its name has a meaning
                        print(f"Star Name: {name}\nBayer Designation: {desig}")
                        print(f"{name} means '{meaning}'.")
                        print(f"Radius: {radius} R☉\nMass: {mass} Suns\nSpectral class: {spectral}, {color} {size}\nSurface temperature: {temp} Kelvin\n{name} is estimated to be {age} million years old.")

                    elif not pandas.isna(row['Name']) and pandas.isna(row['Meaning']) and "*" not in row['Name']: #check if the star just has a name that isn't sgr a*
                        print(f"Star Name: {name}, Designation: {desig}")
                        print(f"{name} does not have an agreed upon meaning.")
                        print(f"Radius: {radius} R☉\nMass: {mass} Suns\nSpectral class: {spectral}, {color} {size}\nSurface temperature: {temp} Kelvin\n{name} is estimated to be {age} million years old.")

                    elif pandas.isna(row['Name']) and pandas.isna(row['Meaning']): #check to see if the star has a name, print designation
                        print(f"Star Name: {desig} (this star does not have a proper name)")
                        print(f"Radius: {radius} R☉\nMass: {mass} Suns\nSpectral class: {spectral}, {color} {size}\nSurface temperature: {temp} Kelvin\n{desig} is estimated to be {age} million years old.")

                    elif "*" in row['Name']: #check to see if the star is actually sagittarius a* (a black hole)
                        print(f"{desig} is a {spectral}, estimated to be {age} million years old.")
                        print(f"{name} has a radius of {radius} R☉ and a mass of {mass} M☉.")
                        print(f"Distance: {distance} Ly from Earth, located in the center of the Milky Way galaxy.")

                    else:
                        print("\nSomething went wrong providing these star names... (internal program error)\n") #if file is messed up then the program still works
                        
                    print(f"Luminosity: {lum} times that of the Sun.\nDistance: {distance} Ly from Earth.\nApparent magnitude: {app}\nAbsolute magnitude: {absM}\n")      
                    
                    starSearch(option3token+1)
                """
            else:
                print(f"\nWe're so sorry! =(\nYou entered {constellation}, a constellation that isn't in the Super Star Catalog!\nThere are only 41 constellations in this catalog...")   
                starSearch(option3token+1)

        elif constellation == "  ":
            print("\nYou found a secret! The only star that isn't in any constellation is the Sun!") #this only happens if the user enters two spaces
            return
        elif constellation == "Idk":
            constFixed = ', '.join(map(str, constList)) #this is borrowed from the conta function as well
            print(f"\nIt's okay to forget! Here's all of the constellations that are recorded in this catalog:\n\n{constFixed[:-6]} and {constFixed[-5:]}.") #
            cont = input("\nEnter anything to continue, or 'exit' to return to the main menu: " ).title()
            if cont == "Exit":
                return
            else:
                starSearch()

        elif constellation == "Exit":
            print("\nExiting to main menu.")
            return

        else:
            print(f"{constellation} is not a valid constellation. Are you sure you spelled it right?")
