# Initialize user_choice as a global variable
user_choice = None

# Function to display the welcome message
def welcome_message():
    print("Welcome to My Python Project!\n")
    print("Roommate selection can be a hassle, so here are a few options to choose from.\n")

# Function to present the user with choices for different topics
def choose_roommate():
    global user_choice  # Declare user_choice as a global variable
    print("Choose your roommate based on the following topics:")
    print("1. Interests and Hobbies")
    print("2. Study Habits")
    print("3. Sports Enthusiasm")
    print("4. Lifestyle Preferences")
    print("5. Food Habits")
    print("6. None (exit)")

    topic_choice = input("Please enter the number corresponding to your topic choice: ")

    if topic_choice == "1":
        print("You have chosen 'Interests and Hobbies'.")
        print("Select a roommate with similar interests.")
        print("1. Steph Curry (Basketball fan)")
        print("2. Kyrie Irving (Music lover)")
        print("3. Patrick Mahomes (Outdoor enthusiast)")
        print("4. None (exit)")
        user_choice = input("Please enter the number corresponding to your choice: ")

        # ... (Roommate selection based on interests)
        # You can implement the logic for roommate selection based on interests here.

    elif topic_choice == "2":
        print("You have chosen 'Study Habits'.")
        print("Select a roommate with similar study habits.")
        print("1. Steph Curry (Dedicated student)")
        print("2. Kyrie Irving (Night owl)")
        print("3. Patrick Mahomes (Balanced study routine)")
        print("4. None (exit)")
        user_choice = input("Please enter the number corresponding to your choice: ")

        # ... (Roommate selection based on study habits)
        # You can implement the logic for roommate selection based on study habits here.

    elif topic_choice == "3":
        print("You have chosen 'Sports Enthusiasm'.")
        print("Select a roommate with a similar passion for sports.")
        print("1. Steph Curry (Basketball fanatic)")
        print("2. Kyrie Irving (Casual sports fan)")
        print("3. Patrick Mahomes (Football enthusiast)")
        print("4. None (exit)")
        user_choice = input("Please enter the number corresponding to your choice: ")

        # ... (Roommate selection based on sports enthusiasm)
        # You can implement the logic for roommate selection based on sports enthusiasm here.

    elif topic_choice == "4":
        print("You have chosen 'Lifestyle Preferences'.")
        print("Select a roommate with a compatible lifestyle.")
        print("1. Steph Curry (Early riser)")
        print("2. Kyrie Irving (Night owl)")
        print("3. Patrick Mahomes (Active lifestyle)")
        print("4. None (exit)")
        user_choice = input("Please enter the number corresponding to your choice: ")

        # ... (Roommate selection based on lifestyle preferences)
        # You can implement the logic for roommate selection based on lifestyle preferences here.

    elif topic_choice == "5":
        print("You have chosen 'Food Habits'.")
        print("Select a roommate with similar food preferences.")
        print("1. Steph Curry (Vegetarian)")
        print("2. Kyrie Irving (Vegan)")
        print("3. Patrick Mahomes (Carnivore)")
        print("4. None (exit)")
        user_choice = input("Please enter the number corresponding to your choice: ")

        # ... (Roommate selection based on food habits)
        # You can implement the logic for roommate selection based on food habits here.

    elif topic_choice == "6":
        user_choice = "None"
    else:
        print("Invalid choice")
        user_choice = None

# Rest of the code remains the same
def send_message(roommate):
    while True:
        message = input(f"Enter a message to {roommate} (type 'exit' to exit): ")
        if message.lower() == 'exit':
            break
        with open(f'{roommate}_messages.txt', 'a') as message_file:
            message_file.write(f'You: {message}\n')

def main():
    welcome_message()
    choose_roommate()  # Call choose_roommate to set user_choice

    if user_choice:
        while True:
            print(f"What would you like to do with {user_choice}?")
            print("1. View roommate's profile")
            print("2. Send a message")
            print("3. Exit")

            action_choice = input("Enter the number of your choice: ")

            if action_choice == "1":
                print(f"Here is the profile of {user_choice}:")
                # Add roommate profile details here
            elif action_choice == "2":
                send_message(user_choice)
            elif action_choice == "3":
                print("Exiting roommate actions.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
    else:
        print("No roommate selected. Goodbye!")

if __name__ == '__main__':
    main()
