import pandas
import matplotlib.pyplot as plt
stars = pandas.read_csv("stars.csv")

########
######## FUNCTIONS RELATED TO STARS BASED ON THEIR CHARACTERISTICS ########
########

#set parameters for star search
def findaStar(findChar=None):
    Chara = ['Radius', 'Mass', 'Temperature', 'Distance', 'Age', 'Apparent', 'Absolute', 'Luminosity']
    Alex = ['Color', 'Class', 'Name'] #create two separate lists; int/float columns and string columns
    Charalex = Chara + Alex
    Charalex = ', '.join(map(str, Charalex)) #sorry hansong idk what map is
    for column in Chara:
        stars[column] = stars[column].astype(str).str.replace(',', '') #iterate over every cell and remove commas
        #stars[column] is all of the data within a column
    stars[Chara] = stars[Chara].apply(pandas.to_numeric) #pandas function that turns every cell into an int or a float
    findChar = input(f"\nHere's some commonly known star traits: {Charalex}.\nEnter a characteristic you would like to search for: ").title()
    if findChar == "Exit":
        print("\nReturning to main menu...")
        return
    if findChar in Chara: #if returning from staro(), enter user input
        if findChar == "Radius":
            radii = float(input("Enter a solar radius (R☉): "))
            scale = input(f"Is this star 'bigger' or 'smaller' than this {findChar}?: ").lower()
            staro(comparison=scale,Radius=radii)
        elif findChar == "Mass":
            masses = float(input("Enter a solar mass (M☉): "))
            scale = input(f"Is this star 'heavier' or 'lighter' than this {findChar}?: ").lower()
            staro(comparison=scale,Mass=masses)
        elif findChar == "Temperature":
            tempK = float(input("Enter a surface temperature (K): "))
            scale = input(f"Is this star 'hotter' or 'cooler' than this {findChar}?: ").lower()
            staro(comparison=scale,Temperature=tempK)
        elif findChar == "Distance":
            dist = float(input("Enter a distance (Ly): "))
            scale = (input(f"Is this star 'closer' or 'farther' than this {findChar}?: ")).lower()
            staro(comparison=scale,Distance=dist)
        elif findChar == "Age":
            ageM = float(input("Enter an age (Myr): "))
            scale = input(f"Is this star 'older' or 'younger' than this {findChar}?: ").lower()
            staro(comparison=scale,Age=ageM)
        elif findChar == "Apparent":
            app = float(input("Enter an apparent magnitude: "))
            scale = input(f"Is this star 'brighter' or 'dimmer' than this {findChar}?: ").lower()
            staro(comparison=scale,Apparent=app)
        elif findChar == "Absolute":
            absM = float(input("Enter an absolute magnitude: "))
            scale = input(f"Is this star 'brighter' or 'dimmer' than this {findChar}?: ").title()
            staro(comparison=scale,Absolute=absM) #use .title() because this is identical to app, otherwise they would get mixed up
        elif findChar == "Luminosity":
            lumin = float(input("Enter a luminosity: "))
            scale = input(f"Does this star produce 'more' or 'less' energy than this {findChar}?: ").lower()
            staro(comparison=scale,Luminosity=lumin)
#
    elif findChar in Alex:
        if findChar == "Color":
            calor = input("Enter a star color: ").title()
            staraStr(color=calor)
        elif findChar == "Class":
            starClass = stars['Class'].unique().tolist()
            starClass = ', '.join(map(str, starClass))
            print(f"\nStar classes in the catalog: {starClass}.\n")
            classes = input("Enter a star class: ").title()
            staraStr(clas=classes)
        elif findChar == "Name":
            pass
#
    else:
        print("Sorry! You either entered a number or made a typo...\nIt's really important that you don't because I'm not good at coding. =)")
        a = input("\nEnter anything to try again, or 'exit' to return to main menu: ").title()
        if a == "Exit":
            print("\nReturning to main menu...")
            return
        else:
            findaStar()
print()


#provies list of stars based on parameters >= and <=
def staro(comparison,Radius=0,Mass=0,Temperature=0,Distance=0,Age=0,Apparent=0,Absolute=0,Luminosity=0):
    StarE = ['Radius', 'Mass', 'Temperature', 'Distance', 'Age', 'Apparent', 'Absolute', 'Luminosity']
    Alex = ['Color', 'Class', 'Name']

    for column in StarE:
        stars[column] = stars[column].astype(str).str.replace(',', '') #iterate over every cell and remove commas
    stars[StarE] = stars[StarE].apply(pandas.to_numeric) #change all the values back to int and floats
    print() #developer note: this function (staro) is the first that absolutely needs to be optimized
    stars['Name'] = stars['Name'].fillna(stars['Designation']) #replace all stars with no names with their designation

#stars.plot.bar(x="Name",y="Radius")
    names = stars['Name']
    distance = stars['Distance']
    apparent_magnitude = stars['Apparent']
       #ankhGraph.plot.bar(x="Name",y="Radius") #plot ankhGraph

    #1 STARS BY RADIUS
    if comparison == "bigger": #comparison is the input from findaStar(); comparison=scale
        ankh = stars[stars['Radius'] >= Radius] #make new dataframe only including stars that meet the parameters for radius
        ankh = ankh.sort_values(by='Radius') #edit the dataframe, sorting by its value and chosen parameter (>=, <=)
        for index, row in ankh.iterrows(): #iterate over the new dataframe and print all of the values
            print(f"Name: {row['Name']}, Radius: {row['Radius']} solar radii")
        ankh_random = stars.sample(n=5, random_state=11)  #select 5 random stars; use stars instead of ankh to prevent ValueError
        ankhRB = ankh.tail(5) #select the 5 biggest stars; ankh[Trait, Parameter], ex. RB for "Radius: Biggest"
        ankhGraph = pandas.concat([ankhRB, ankh_random]) #combine the two dataframes
        plt.figure(figsize=(12, 8)) #set size of graph
        plt.scatter(ankhGraph['Name'], ankhGraph['Radius'], s=ankhGraph['Radius'] * 2, c="blue", alpha=0.8) #create graph with parameters
        plt.xticks(rotation=90)  #rotate x-axis labels for readability

    elif comparison == "smaller": #repeat the process for every variable twice; >= and <=
        ankh = stars[stars['Radius'] <= Radius]
        ankh = ankh.sort_values(by='Radius')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Radius: {row['Radius']} solar radii")
        ankh_random = stars.sample(n=5, random_state=12) #6 has VY canis majoris
        ankhRS = ankh.head(5)
        ankhGraph = pandas.concat([ankhRS, ankh_random])
        plt.figure(figsize=(10, 8))
        plt.scatter(ankhGraph['Name'], ankhGraph['Radius'], s=ankhGraph['Radius'] * 10, c="blue", alpha=0.8)
        plt.xticks(rotation=90)
#
    #2 STARS BY MASS
    elif comparison == "heavier":
        ankh = stars[stars['Mass'] >= Mass]
        ankh = ankh.sort_values(by='Mass')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Mass: {row['Mass']} solar masses")
        ankh_random = stars.sample(n=5, random_state=3)
        ankhMH = ankh.tail(5)
        ankhGraph = pandas.concat([ankhMH, ankh_random])
        ankhGraph.plot(kind='bar', x='Name', y='Mass', figsize=(10, 8))
        plt.ylabel('Mass (solar masses)')

    elif comparison == "lighter":
        ankh = stars[stars['Mass'] <= Mass]
        ankh = ankh.sort_values(by='Mass')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Mass: {row['Mass']} solar masses")
        ankh_random = stars.sample(n=5, random_state=1)
        ankhML = ankh.head(5)
        ankhGraph = pandas.concat([ankhML, ankh_random])
        ankhGraph.plot(kind='bar', x='Name', y='Mass', figsize=(10, 8))
        plt.ylabel('Mass (solar masses)')
#
    #3 STARS BY TEMPERATURE
    elif comparison == "hotter":
        ankh = stars[stars['Temperature'].round().astype(int) >= Temperature]
        ankh = ankh.sort_values(by='Temperature')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Temperature: {row['Temperature']} K")
        ankh_random = stars.sample(n=5, random_state=2)
        ankhTH = ankh.tail(5)
        ankhGraph = pandas.concat([ankhTH, ankh_random])
        ankhGraph.plot(kind='bar', x='Name', y='Temperature', figsize=(10, 8))
        plt.ylabel('Temperature (K)')

    elif comparison == "cooler":
        ankh = stars[stars['Temperature'].round().astype(int) <= Temperature]
        ankh = ankh.sort_values(by='Temperature')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Temperature: {row['Temperature']} K")
        ankh_random = stars.sample(n=5, random_state=6)
        ankhTC = ankh.head(5)
        ankhGraph = pandas.concat([ankhTC, ankh_random])
        ankhGraph.plot(kind='bar', x='Name', y='Temperature', figsize=(10, 8))
        plt.ylabel('Temperature (K)')
#
    #4 STARS BY DISTANCE FROM EARTH
    elif comparison == "farther":
        ankh = stars[stars['Distance'] >= Distance]
        ankh = ankh.sort_values(by='Distance')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Distance: {row['Distance']} Ly")
        ankh_random = stars.sample(n=5, random_state=3)  #select 5 random stars; use stars instead of ankh to prevent ValueError
        ankhDF = ankh.tail(5)
        ankhGraph = pandas.concat([ankhDF, ankh_random])
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.scatter(ankhGraph['Distance'], ankhGraph['Name'], s=10, c="white", alpha=0.8)
        ax.set_xlabel('Distance (Ly)')
        ax.set_facecolor("black")

    elif comparison == "closer":
        ankh = stars[stars['Distance'] <= Distance]
        ankh = ankh.sort_values(by='Distance')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Distance: {row['Distance']} Ly")
        #ankh_random = stars.sample(n=5, random_state=7)  #select 5 random stars; use stars instead of ankh to prevent ValueError
        ankhDF = ankh.head(20)
        #size = 10 ** (-apparent_magnitude) * 5
        ankhGraph = pandas.concat([ankhDF])
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.scatter(ankhGraph['Distance'], ankhGraph['Name'], s=10, c="white", alpha=0.8)
        ax.set_xlabel('Distance (Ly)')
        ax.set_facecolor("black")
#
    #5 STARS BY AGE
    elif comparison == "older":
        ankh = stars[stars['Age'] >= Age]
        ankh = ankh.sort_values(by='Age')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Age: {row['Age']} Myr")
        ankh_random = stars.sample(n=5, random_state=4)
        ankhAO = ankh.tail(5)
        ankhGraph = pandas.concat([ankhAO, ankh_random])
        ankhGraph.plot(kind='bar', x='Name', y='Age', figsize=(10, 8))
        plt.ylabel('Age (Myr)')
    elif comparison == "younger":
        ankh = stars[stars['Age'] <= Age]
        ankh = ankh.sort_values(by='Age')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Age: {row['Age']} Myr")
        ankh_random = stars.sample(n=5, random_state=5)
        ankhAY = ankh.head(5)
        ankhGraph = pandas.concat([ankhAY, ankh_random])
        ankhGraph.plot(kind='bar', x='Name', y='Age', figsize=(10, 8))
        plt.ylabel('Age (Myr)')
#
    #6 STARS BY APPARENT MAGNITUDE
    elif comparison == "brighter":
        ankh = stars[stars['Apparent'] <= Apparent]
        ankh = ankh.sort_values(by='Apparent')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Apparent Magnitude: {row['Apparent']}")
        ankh_random = stars.sample(n=5, random_state=5)
        ankhAPMB = ankh.head(5)
        ankhGraph = pandas.concat([ankhAPMB, ankh_random])
        ankhGraph.plot(kind='bar', x='Name', y='Apparent', figsize=(10, 8))
        plt.ylabel('Apparent Magnitude')

    elif comparison == "dimmer":
        ankh = stars[stars['Apparent'] >= Apparent]
        ankh = ankh.sort_values(by='Apparent')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Apparent Magnitude: {row['Apparent']}")
        ankh_random = stars.sample(n=5, random_state=7)
        ankhAPMD = ankh.tail(5)
        ankhGraph = pandas.concat([ankhAPMD, ankh_random])
        ankhGraph.plot(kind='bar', x='Name', y='Apparent', figsize=(10, 8))
        plt.ylabel('Apparent Magnitude')
#
    #7 STARS BY ABSOLUTE MAGNITUDE
    elif comparison == "Brighter":
        ankh = stars[stars['Absolute'] <= Absolute]
        ankh = ankh.sort_values(by='Absolute')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Absolute Magnitude: {row['Absolute']}")
        ankh_random = stars.sample(n=5, random_state=8)
        ankhAO = ankh.head(5)
        ankhGraph = pandas.concat([ankhAO, ankh_random])
        ankhGraph.plot(kind='bar', x='Name', y='Absolute', figsize=(10, 8))
        plt.ylabel('Absolute Magnitude')
    elif comparison == "Dimmer":
        ankh = stars[stars['Absolute'] >= Absolute]
        ankh = ankh.sort_values(by='Absolute')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Absolute Magnitude: {row['Absolute']}")
        ankh_random = stars.sample(n=5, random_state=9)
        ankhAO = ankh.tail(5)
        ankhGraph = pandas.concat([ankhAO, ankh_random])
        ankhGraph.plot(kind='bar', x='Name', y='Absolute', figsize=(10, 8))
        plt.ylabel('Absolute Magnitude')
#
    #8 STARS BY ENERGY OUTPUT
    elif comparison == "more":
        ankh = stars[stars['Luminosity'] >= Luminosity]
        ankh = ankh.sort_values(by='Luminosity')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Luminosity: {row['Luminosity']} L☉")
        ankh_random = stars.sample(n=5, random_state=13)
        ankhLM = ankh.tail(5)
        ankhGraph = pandas.concat([ankhLM, ankh_random])
        ankhGraph.plot(kind='bar', x='Name', y='Luminosity', figsize=(10, 8))
        plt.ylabel('Luminosity (relative to Sol)')

    elif comparison == "less":
        ankh = stars[stars['Luminosity'] <= Luminosity]
        ankh = ankh.sort_values(by='Luminosity')
        for index, row in ankh.iterrows():
            print(f"Name: {row['Name']}, Luminosity: {row['Luminosity']} L☉")
        ankhLL = ankh.head(10)
        ankhLL.plot(kind='bar', x='Name', y='Luminosity', figsize=(10, 8))
        plt.ylabel('Luminosity (relative to Sol)')
#
    else:
        print("\nYou entered the wrong parameter or made a typo! The parameters should be bigger, smaller; brighter, dimmer, etc...")
        findaStar(findChar="")
#
    graph = input("\nWould you like to plot a graph? (yes/no): ")
    if graph == "yes":
        plt.show()
        menuLoop = input("\nDo you want to search for more stars? Enter yes, or anything to continue, or 'exit' to return to main menu: ").title()
        if menuLoop in StarE or menuLoop in Alex or menuLoop == "Yes":
            findaStar()
        elif menuLoop == "Exit":
            print("\nRedirecting...")
            return
        else:
            print("\nOops! That was probably a typo, returning to main menu...")
            return
    elif graph == "no":
        pass
    else:
        pass

#provies list of stars based on color and class (size)
def staraStr(color="",clas=""):    
    stars['Color'] = stars['Color'].fillna('')
    stars['Class'] = stars['Class'].fillna('')
        
    if color in stars['Color'].values:
        colorStars = stars[stars['Color'].str.contains(color, na=False)]
        for index, row in colorStars.iterrows():
            print(f"Name: {row['Name']}, Color: {row['Spectral']}, {row['Color']}")

    elif clas in stars['Class'].values:
        classStars = stars[stars['Class'].str.contains(clas, na=False)]
        for index, row in classStars.iterrows():
            print(f"Name: {row['Name']}, Class: {row['Color']} {row['Class']}")

    else:
        print("No stars were found. Are you sure you entered a color or class that stars actually have?")
    findaStar()

def starName(name=""):
    pass