#BIRTHDAY REMINDER

from datetime import datetime # datetime is imported to create a datetime object in this case the birthdates.


birthdays = {} #empty dictionary to have users input friends birthdates

print('\nWelcome to Birthdays Reminder') #these are print statements that will be displayed at the beggining of the program.
print('\nPlease choose one of the following options: ')

def add_birthday(): #This line defines a function named add_birthday. Functions in Python are blocks of code that perform specific tasks.
    name = input("Enter the name of the person: ") # users will input a name and this name will be stored in the variable 'name'.
    bday = input("Enter their birthday (YYYY/MM/DD): ") #users will input a birthdat and it will bes tored in the variable 'bday'.
    birthdays[name] = bday #this line adds an entry to the 'birthdays' dictionary. The persons name is the key adn their birthday is the value.
    print(f"{name}'s birthday ({bday}) has been added to the list.") #print statement that confirms the name and birthday of person has been added to the list. 

def check_upcoming_birthdays(): #defines the function
    today = datetime.today().date() #This line retrieves the current date using the "datetime" module
    upcoming_birthdays = [] #empty list to store upcoming birthdays

    for name, birthday in birthdays.items(): #it iterates through each name and corresponding birthday in the "birthdays" dictionary.
        birthdate = datetime.strptime(birthday, '%Y/%m/%d').date() #this line converts the string representation of a birthday to a date object.
        if birthdate.month == today.month and birthdate.day > today.day: #this conditional statement checks if the birthdate month matches the current month and if the day of the birthdate is greater than the current day.
            upcoming_birthdays.append((name, birthday)) #name and birthday are appended to the upcoming_birthdays list as a truple. 

    if upcoming_birthdays: #if there are upcoming birthdays it enters a block and prints a message        
        for name, birthday in upcoming_birthdays:
            print(f"{name}'s birthday is on {birthday}")
    else: #no upcoming birthdays it prints a message
        print("\nNo upcoming birthdays in this month.")


def days_until_birthday(birthdate): #calculates the number of days remaining until a specific birthday
    today = datetime.now().date() #this line retrieves the current date using 'datetime' module. datetime.now() returns the current date amd time and .date() extracts only the date portion.
    next_birthday = birthdate.replace(year=today.year) #This line calculates the date of the next birthday by repalcing the year component of the 'birthdate' with the current year.

    if next_birthday < today: #this conditional statement checks if the calculated 'next_birthday' is earlier than the current date.
        next_birthday = next_birthday.replace(year=today.year + 1) #if the birthday has already occurred in the current year, the code enters this block

    days_remaining = (next_birthday - today).days #This line calculates the difference in days between the next_birthday and the current date using the .days attribute of the resulting timedelta object.

    return days_remaining #The function returns the days_remaining value, which is the number of days until the specified birthdate

if __name__ == "__main__": #construct that checks whether the script is being run directly (as the main program) or imported as a module.
        
    while True: #The while True loop ensures that the menu is repeatedly displayed until the user chooses to exit (option 4), allowing the user to perform multiple actions in the same session
        print("\nMenu:") #print statemnts that will give the user options to choose from : prints a list of options to select from.
        print("1. Add a Birthday")
        print("2. Check Upcoming Birthdays")
        print("3. Check days remaining until birthday")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_birthday()
        elif choice == "2":
            check_upcoming_birthdays()
        elif choice == "3":
            birthdate_str = input("Enter friend's birthdate (YYYY/MM/DD): ") #prompts the user to enter a birthdate in the from of YYY/MM/DD and stores input as a string variable.
            birthdate = datetime.strptime(birthdate_str, "%Y/%m/%d").date() # datetime.strptime() function pars the string and converts it into a date object. The .date() method is used to extract only the date part, excluding the time.
            remaining_days = days_until_birthday(birthdate) #calculates the number of days remianing until bday
            if remaining_days == 0: #If the number of days is zero the brthday is today
                print("Happy birthday! 🎉")
            else:
                print(f"Days remaining until your friend's next birthday: {remaining_days}")
        elif choice == "4":
            print("Goodbye!")
            break #The break statement immediately exits the while loop, effectively terminating the progrgam.
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
