print("ME021_Python_Project_Moua_Karah")

print("Welcome to the app Adventuring!")
print("Start by choosing a place to do a fun activity!")
print()

# This is the first step to finding an activity to do
city = ["Merced", "Fresno", "San Francisco", "Monterey", "Los Angeles"]
print("Please choose a city:")
print('1.',city[0])
print('2.',city[1])
print('3.',city[2])
print('4.',city[3])
print('5.',city[4])
print()

choice = input("Enter your choice (1/2/3/4/5):")
print()
# if/else statements
price = ["$10.00", "$20.00", "$30.00", "$40.00", "$50.00"]
if choice == "1":
    print("Merced price range options:")
    print("a.", price[0])
    print("b.", price[1])
    print("c.", price[2])
    print("d.", price[3])
    print("e.", price[4])
elif choice == "2":
    print("Fresno price range options:")
    print("a.", price[0])
    print("b.", price[1])
    print("c.", price[2])
    print("d.", price[3])
    print("e.", price[4])
elif choice == "3":
    print("San Francisco price range options:")
    print("a.", price[0])
    print("b.", price[1])
    print("c.", price[2])
    print("d.", price[3])
    print("e.", price[4])
elif choice == "4":
    print("Monterey price range options:")
    print("a.", price[0])
    print("b.", price[1])
    print("c.", price[2])
    print("d.", price[3])
    print("e.", price[4])
else:
    print("Los Angeles price range options:")
    print("a.", price[0])
    print("b.", price[1])
    print("c.", price[2])
    print("d.", price[3])
    print("e.", price[4])
print()

# This is the second step
# Another if/else statement
choose = input("Choose your price range (a/b/c/d/e):")
if choose == "a":
    print("You chose to do a", price[0], "activity")
elif choose == "b":
    print("You chose to do a", price[1], "activity")
elif choose == "c":
    print("You chose to do a", price[2], "activity")
elif choose == "d":
    print("You chose to do a", price[3], "activity")
else:
    print("You chose to do a", price[4], "activity")
print()

# Third step
# Now performing a while loop
while True:
    print("Select an indoor or outdoor activity:")
    print("i. indoor activity")
    print("o. outdoor activity")
    select = input()
    if select == "i":
        print("You selected to do an indoor activity")
        print("1. Movies",
              "2. Escape room",
              "3. Paint class",
              "4. Dinner",
              "5. Art Gallery")
        print()
        decide = input("Decide which activity (1/2/3/4/5):")
        if decide == "1":
            print("Movies")
        elif decide == "2":
            print("Escape room")
        elif decide == "3":
            print("Paint class")
        elif decide == "4":
            print("Dinner")
        else:
            print("Art Gallery")
        break
    else:
        print("You selected to do an outdoor activity")
        print("1. Picnic",
              "2. Floating lantern festival",
              "3. Stargazing",
              "4. Hiking",
              "5. Amusement Park")
        print()
        decide = input("Decide which activity (1/2/3/4/5):")
        if decide == "1":
            print("Picnic")
        elif decide == "2":
            print("Floating lanter festival")
        elif decide == "3":
            print("Stargazing")
        elif decide == "4":
            print("Hiking")
        else:
            print("Amusement Park")
        break
print()

print("You've successfully chose an activity to do!")

