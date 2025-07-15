options = []
# main function which will store the iformation on the waitlist
while True:
    print("Select from the following options")
    print("1. Add name to wait list")
    print("2. Remove name from wait list")
    print("3. Pay Fee")
    print("4. View Waitlist")
    print("5. Exit")

    choice = input("Enter your choice: ")
# loop to keep showing the menu to the user even after a choice/Users/maxfu/Desktop/Artifical Intelligence/Research/Autograder/Semester_2/submissionsPythonProjects/55989/55989_6421744_3129037.txt has been selected
    if choice == '1':
        option = input("Enter your first and last name: ")
        options.append({"option": option, "payed": False})
        # options.append function opens main function "options" and uses the value that was just insertet in the line above and then switches it to false to start off
        print(f"'{option}' has been added to the wait list.")
# prints our inserted value for "option" which would be a name and then has the following statenebt after
    elif choice == '2':
        if not options:
            print("There is currently no one in the wait list.")
# if there is nothing in the main list function for "options" then a mssg is printed telling user that there is nothing there
        else:
            option_number = int(input("Enter your place in line to remove from waitlist: "))
            if 1 <= option_number <= len(options):
# option_number asks to insert number value of what place the person is in line
# if statement then checks to see if inserted value is valid which would be from minimum of 1 to the length of the options list
                removed_option = options.pop(option_number - 1)
# pop() function removes option from the original options list using the equation option_number 'which we stated before' -1 
                
                print(f"'{removed_option['option']}' has been removed from the wait list.")
# retrieves specific "option" value from the removed_option list and then marks it as removed
            else:
                print("Invalid option number. Please try again.")

    elif choice == '3':
        if not options:
            print("Wait list is empty.")
        else:
            option_number = int(input("Enter place in line to mark as payed: "))
# asks for number in the line 
            if 1 <= option_number <= len(options):
                options[option_number - 1]["payed"] = True
# if number in line is valid then fuunction sets whatever number user gave and sets the selection set to true that they did pay since they all automatically start off as not true for not paying
                print(f"{option} marked as payed.")

    elif choice == '4':
        print("\nView wait list:")
        for index, option_info in enumerate(options, start=1):
# for the options main list, enumerate keeps track of list in order to go over and it starts with the first one being value 1
            status = "Ready" if option_info["payed"] else "Not Ready"
# opens option_info list which is the list of all people in waitlist and checks to see if they have the payed or not payed mark yet
# if not payed then there is a mssg next to the name in the list saying ready or not ready based on payment status
            print(f"{index}. {option_info['option']} - {status}")
# basically what I just said 

    elif choice == '5':
        print("Exiting the jumper app. Till next time fam!")
        break
    else:
        print("Invalid selection. Try again?")
