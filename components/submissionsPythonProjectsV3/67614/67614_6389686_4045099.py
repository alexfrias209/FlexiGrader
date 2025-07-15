while True:
    import csv

    print('\033[1m' + "\nWelcome to recommendation for Appliance/Smart Device" + '\033[0m') # '\033[1m' and '\033[0m' makes the print statement bold
    print('\033[1m' + 'Search features for best recommendation' + '\033[0m')
    print()
    # separates the appliances, brand, year price, and model
    def recommendation(lines, recommendations_found):   
        lines[0].strip().lower()
        brand = lines[1].strip().lower()
        year = int(lines[2].strip())
        price = float(lines[3].strip())
        model = lines[4].strip()
    # -if statement to print if the input is 'none' or a brand or integer
        if (
            (user_brand == 'none' or user_brand == brand) and
            (user_year == 'none' or user_year <= year) and
            (user_price == 'none' or user_price >= price)
        ):
            print(f"You might consider this model: {brand} - model {model}: priced at ${price:.2f} made in {year}")
            recommendations_found[0] = True
    # list of the items in the file
    available_appliances = ['refrigerator', 'phone', 'machine washer', 'stove']
    print('\033[1m' + "Press:" + '\033[0m'
        "\n1 for Refrigerator," 
        "\n2 for Phone," 
        "\n3 for Machine Washer,"
        "\n4 for Stove")
    # loop that will continue for ever until an input based on the if-else statement is true
    while True:
        user_appliance_choice = input("Enter your choice: ")
        if user_appliance_choice.isnumeric() and 1 <= int(user_appliance_choice) <= 4:
            user_appliance = available_appliances[int(user_appliance_choice) - 1]
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")

    user_brand = input("\nRefrigerator (LG, Samsung, GE)"
                       "\nPhone (Samsung, Apple, Nokia)"
                       "\nMachine Washer (Samsung, LG, Whirlpool)"
                       "\nStove (Whirlpool, Bosch, GE, LG)"
                       "\n('none' if no preference): "
                       '\033[1m' + "\nEnter brand: " + '\033[0m').lower()

    # loop that will continue for ever until an input based on the if-else statement is true
    while True:
        user_year = input('\033[1m' + "\nEnter preferred and above year (or 'none' if no preference): " + '\033[0m').lower()
        if (user_year.isnumeric() and len(user_year) == 4) and int(user_year) <= 2023 or user_year == 'none':
            user_year = int(user_year) if user_year.isnumeric() else 'none'
            break
        else:
            print("\nInvalid input. Please enter a valid 4-digit year or 'none'.")
    # loop that will continue for ever until an input based on the if-else statement is true
    while True:
        user_price = input('\033[1m' + "\nWhat is your maximum price (or 'none' if no preference): " + '\033[0m').lower()
        if user_price.replace('.', '', 1).isnumeric() or user_price == 'none': #checks if it's a number
            user_price = float(user_price) if user_price.replace('.', '', 1).isnumeric() else 'none' #If it is a number then convert it to float
            break
        else:
            print('\033[1m' + "\nInvalid input. Please enter a valid price or 'none'." + '\033[0m')

    filename = '67614_6389687_8182736.csv'
    recommendations_found = [False]
    # introduces the file
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        csvFile = csv.reader(file)
        next(csvFile)  
        for lines in csvFile:      # if-statement for the user_appliances in the file 
            if lines[0].strip().lower() == user_appliance:
                recommendation(lines, recommendations_found)
    # if false, which means it didn't go through then prints 
    if not recommendations_found[0]:
        print("Sorry, no matches were found with your criteria.")
    continue_code = input('\033[1m' + '\nDo you want to continue (yes/no)? ' + '\033[0m')
    if continue_code == 'yes':
        continue
    elif continue_code == 'no':
        break
