webpage_topic = input("Enter the project's webpage topic: ")
webpage_description = input("Enter the project's webpage description: ")
print("Welcome to My Food Project")
customer_name = input("Your Name: ")  
developer_name = input("Developer Name: ")
part_description = "This part helps you choose your food and dining preferences."

if "food" in webpage_topic.lower() and "order" in webpage_description.lower():
    print(f"Hello, {customer_name}! Your project on '{webpage_topic}' related to food ordering sounds like it could be valid for ME 021.")
else:
    print(f"Hello, {customer_name }! Your project on '{webpage_topic}' may not be directly related to ME 021.")


goal = input("1. Please describe the big-picture problem that your ME 021 project is addressing (be succinct): ")

inputs_outputs = input("2. Write down the specific objectives that this project will achieve (inputs and outputs): ")

data_needed = input("3. Please specify the data that this project would need: ")

meeting_with_ta = input("4. Have you met with (course TA) to discuss the project? (Yes or No): ")

if goal and inputs_outputs and data_needed and meeting_with_ta:
    print("Thank you for providing the information. Your responses have been recorded.")
else:
    print("Please make sure to answer all four questions.")



print(f"Developer: {developer_name}")
print(f"Part Description: {part_description}")

neatedList = [
    ["Burger", "234 calories", 22],
    ["Pizza", "285 calories", 10],
    ["Taco", "156 calories", 6],
    ["Sushi", "93 calories", 12],
    ["French Fries", "365 calories", 4]
]

total_calories = 0
total_price = 0
chosen_foods = []

while True:
    print("\nChoose from the following options:")
    print("1. Choose Food")
    print("2. Choose Ingredients")
    print("3. Dining Preferences")
    print("4. Show Receipt and Exit")

    user_choice = input("Enter the number of your choice: ")

    if user_choice == "1":
        food_choice = input("Choose your food (e.g., pizza, sushi, tacos): ")
        print(f"You chose {food_choice}. Enjoy your meal!")

        chosen_item = None
        for item in neatedList:
            if food_choice.lower() == item[0].lower():
                chosen_item = item
                break

        if chosen_item:
            food_name, calories, price = chosen_item[0], chosen_item[1], chosen_item[2]
            calorie = int(calories.split()[0])
            total_calories += calorie
            total_price += price
            chosen_foods.append((food_name, calorie, price))

        else:
            print("Food item not found in the list.")

    elif user_choice == "2":
        ingredient_choice = input("Choose an ingredient (e.g., cheese, avocado, chicken): ")
        print(f"You chose {ingredient_choice}. Get creative with your dishes!")

    elif user_choice == "3":
        dining_choice = input("Dine in or dine out? (Type 'in' or 'out'): ")
        if dining_choice.lower() == 'in':
            print("You chose to dine in. Enjoy the cozy atmosphere!")
        elif dining_choice.lower() == 'out':
            print("You chose to dine out. Explore some great restaurants!")

    elif user_choice == "4":
        print("Here is your receipt:")
        print("Food          | Calories | Price")
        for food, calories, price in chosen_foods:
            print(f"{food:13} | {calories} cal  | ${price:.2f}")
        print(f"Total Calories: {total_calories} cal")
        print(f"Total Price: ${total_price:.2f}")
        print("Exiting the program. Thank you for using.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")


exit_program = False

while not exit_program:

    user_choice = input("Enter the number of your choice: ")

    if user_choice == "1":
        food_choice = input("Choose your food (e.g., pizza, sushi, tacos): ")

    elif user_choice == "2":
        ingredient_choice = input("Choose an ingredient (e.g., cheese, avocado, chicken): ")

    elif user_choice == "3":
        dining_choice = input("Dine in or dine out? (Type 'in' or 'out'): ")

    elif user_choice == "4":
        receipt_filename = "receipt.txt"
        with open(receipt_filename, 'w') as receipt_file:
            receipt_file.write("Here is your receipt:\n")
            receipt_file.write("Food          | Calories | Price\n")
            for food, calories, price in chosen_foods:
                receipt_file.write(f"{food:13} | {calories} cal  | ${price:.2f}\n")
            receipt_file.write(f"Total Calories: {total_calories} cal\n")
            receipt_file.write(f"Total Price: ${total_price:.2f}\n")

        print(f"Receipt has been saved to {receipt_filename}. Exiting the program. Thank you for using.")
        exit_program = True  

    else:
        print("Invalid choice. Please choose a valid option.")



print("Welcome to the Food Order Manager")
developer_name = input("Your Name: ")
part_description = "This part helps you customize your food order."

print(f"Developer: {developer_name}")
print(f"Part Description: {part_description}")

while True:
    print("\nChoose from the following options:")
    print("1. Select Condiments")
    print("2. Dining Preferences (Table Selection)")
    print("3. To-Go Bag (For Eating Out)")
    print("4. Exit")

    user_choice = input("Enter the number of your choice: ")

    if user_choice == "1":
        condiments = []  
        while True:
            condiment = input("Select a condiment (e.g., ketchup, mustard, mayo) or 'done' to exit: ")
            if condiment.lower() == 'done':
                break
            else:
                condiments.append(condiment)
        print(f"You selected the following condiments: {', '.join(condiments)}")

    elif user_choice == "2":
        dining_choice = input("Dine in or dine out? (Type 'in' or 'out'): ")
        if dining_choice.lower() == 'in':
            table_selection = input("Select a table (e.g., 'Table 1', 'Table 2', 'Booth 3'): ")
            print(f"You selected table: {table_selection}. Enjoy your meal at the table!")
        elif dining_choice.lower() == 'out':
            print("You chose to eat out. Getting a to-go bag.")

    elif user_choice == "3":
        print("Getting a to-go bag for your order.")

    elif user_choice == "4":
        print("Exiting the program. Thank you for using the Food Order Manager.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")

        exit_program = False

while not exit_program:
    user_choice = input("Enter the number of your choice: ")

    if user_choice == "1":
        food_choice = input("Choose your food (e.g., pizza, sushi, tacos): ")

    elif user_choice == "2":
        ingredient_choice = input("Choose an ingredient (e.g., cheese, avocado, chicken): ")

    elif user_choice == "3":
        dining_choice = input("Dine in or dine out? (Type 'in' or 'out'): ")

    elif user_choice == "4":
        receipt_filename = "60708_6411038_4853530.txt"
        with open(receipt_filename, 'w') as receipt_file:
            receipt_file.write("Here is your receipt:\n")
            receipt_file.write("Food          | Calories | Price\n")
            for food, calories, price in chosen_foods:
                receipt_file.write(f"{food:13} | {calories} cal  | ${price:.2f}\n")
            receipt_file.write(f"Total Calories: {total_calories} cal\n")
            receipt_file.write(f"Total Price: ${total_price:.2f}\n")

        print(f"Receipt has been saved to {receipt_filename}. Exiting the program. Thank you for using.")
        exit_program = True  
        break  

    else:
        print("Invalid choice. Please choose a valid option.")




receipt_filename = "receipt.txt"
receipt_content = []

while True:

    user_choice = input("Enter the number of your choice: ")

    if user_choice == "1":
        condiments = []  
        while True:
            condiment = input("Select a condiment (e.g., ketchup, mustard, mayo) or 'done' to exit: ")
            if condiment.lower() == 'done':
                break
            else:
                condiments.append(condiment)
        print(f"You selected the following condiments: {', '.join(condiments)}")

    elif user_choice == "2":
        dining_choice = input("Dine in or dine out? (Type 'in' or 'out'): ")
        if dining_choice.lower() == 'in':
            table_selection = input("Select a table (e.g., 'Table 1', 'Table 2', 'Booth 3'): ")
            print(f"You selected table: {table_selection}. Enjoy your meal at the table!")
        elif dining_choice.lower() == 'out':
            print("You chose to eat out. Getting a to-go bag.")

    elif user_choice == "3":
        print("Getting a to-go bag for your order.")

    elif user_choice == "4":
        receipt_filename = "receipt.txt"
        receipt_content = []

        with open(receipt_filename, 'w') as receipt_file:
            receipt_file.write("Food Order Receipt\n")
            receipt_file.write(f"Ordered by: {developer_name}\n")
            receipt_file.write("Ordered Items:\n")
            for food, calories, price in chosen_foods:
                receipt_content.append(f"{food:13} | {calories} cal  | ${price:.2f}")
            receipt_file.write("\n".join(receipt_content))
            receipt_file.write(f"\nTotal Calories: {total_calories} cal")
            receipt_file.write(f"Total Price: ${total_price:.2f}")

        print(f"Receipt has been saved to {receipt_filename}. Exiting the program. Thank you for using.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")


file_name = "receipt.txt"
 
try:
    with open(file_name, 'r') as file:
        file_contents = file.read()
        print(file_contents)

except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
except IOError:
    print(f"An error occurred while reading the file '{file_name}'.")


















































