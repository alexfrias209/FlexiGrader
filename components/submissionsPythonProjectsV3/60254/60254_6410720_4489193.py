import random


menu_items = {
    "Breakfast": ["Scrambled Eggs", "Pancakes", "Cereal", "Bagel"],
    "Lunch": ["Sandwich", "Salad", "Pizza", "Burger", "Soup"],
    "Dinner": ["Steak", "Chicken Breast", "Loaded Nachos", "Spaghetti", "Pizza"],
    "Dessert": ["Ice Cream", "Cake", "Cookies"],
    "Drink": ["Water", "Milk","coffee", "Soda", "Tea", "Boba"],
} #This is a list of menu items for each type
menu_reactions = ["YUM", "Nice", "Delectable", "Delicious", "Tasty"]
weekly_menu = {}
while True: #This starts the loop, while the code is running
    print("\nWelcome to the UC Merced Pavilion!")
    print("1. Generate a menu for the day")
    print("2. View generated menus")
    print("3. Exit")

    choice = input("Please select an option (valid options are 1/2/3): ")

    if choice == '1': #this part creates the menu
        meal_type = input("Please enter your type of meal (Breakfast/Lunch/Dinner/Drinks/Desserts): ")
        day = input("And the day you are looking for is? ")
        if meal_type in menu_items:
            menu_item = random.choice(menu_items[meal_type])
            if day not in weekly_menu:
                weekly_menu[day] = {}
            weekly_menu[day][meal_type] = menu_item
            print(f"The meal on {day} during {meal_type} is: {menu_item}, Enjoy! ")
        else:
            print("You have chosen an invalid meal type, please choose again ")
    elif choice == '2': #This part lets you view previous menus if there are any
        if not weekly_menu:
            print("No menu has been generated yet. So please create one! ") #no menu generated= no viewed menu
        else:
            print("\nHere are the previously generated menus: ")
            reaction = random.choice(menu_reactions)
            for day, meals in weekly_menu.items():
                for meal_type, menu_item in meals.items():
                    print(f"For {day}, {meal_type} = {menu_item}, {reaction}")
                    reaction = random.choice(menu_reactions) 
    elif choice == '3': #this part saves the previous menus as a file
        with open('menu.txt', 'w') as menu_file:
            for day, meals in weekly_menu.items():
                menu_file.write(day + '\n')
                for meal_type, menu_item in meals.items():
                    menu_file.write(f"{meal_type}: {menu_item}\n")
        print("Your menu(s) have been saved, have a nice day! :)")
        break #Break from this loop

    else:
        print("Invalid option. Please choose option 1, 2 or 3")