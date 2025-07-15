#Intro to my code

print("Hello, User! This is an application where you will be able to upload files from games that you have played or are currently playing to check your progress for those games.")

#Code to allow the user to upload a file


def upload_file():
    file_name = input("Enter the name of the file: ") # change print option
    with open(file_name, "a") as file: # change w to a
        content = input("Enter the content of the file: ")
        file.write(content)
    print(f"File '{file_name}' has been uploaded.")

def display_file_content():
  file_name = input("Enter exact name of file: ")
  try:
    with open(file_name,"r") as file:
      content = file.read()
      print(f"Contents\n{content}")
  except FileNotFoundError:
    print(f"The file {file_name} does not exist")


#Code for profile menu option

def profile_menu():
    while True:
        sub_profile = input(f"Please select an option from the following choices for Profile: {Activities}, {Favorite_Games}, {Achievements}, or 'back' to go back: ").strip()

        if sub_profile == "back":
            break

        if sub_profile == Activities:
            print("Welcome to your Activities.")
            file_upload = input("Do you want to upload a file (yes/back)? ").strip().lower()
            if file_upload == "yes":
                upload_file()
        elif sub_profile == Favorite_Games:
            print("Here is a list of your favorite games.")
            fil_upload = input("Do you want to upload a file (yes/back)? ")
            if filed_upload == "yes":
                upload_file()
        elif sub_profile == Achievements:
            print("Here is a list of all your achievements.")
            file_upload = input("Do you want to upload a file (yes/back)? ").strip().lower()
            if file_upload == "yes":
                upload_file()
        else:
            print("Option is invalid, please choose a valid option")

#Code for library menu option

def library_menu():
    while True:
        sub_library = input(f"Please select an option from the following choices for Library: {All_Games}, {DLC}, or 'back' to go back: ").strip()

        if sub_library == "back":
            break

        if sub_library == All_Games:
            print("Here is a list of all your games.")
            file_upload = input("Do you want to upload a file (yes/back)? ").strip().lower()
            if file_upload == "yes":
                upload_file()
        elif sub_library == DLC:
            print("Here is a list of all your DLC.")
            file_upload = input("Do you want to upload a file (yes/back)? ").strip().lower()
            if file_upload == "yes":
                upload_file()
        else:
            print("Option is invalid, please choose a valid option")

#Variables being defined

Profile = "Profile"
Library = "Library"
Activities = "Activities"
Favorite_Games = "Favorite Games"
Achievements = "Achievements"
All_Games = "All Games"
DLC = "DLC"

#Simplified code that uses the defined functions above

while True:
    menu = input(f"Please select an option from the following choices: {Profile}, {Library}, View or 'exit' to quit: ").strip()

    if menu == "exit":
        break

    if menu == Profile:
        profile_menu()
    elif menu == Library:
        library_menu()
    elif menu == 'View':
        display_file_content()
    else:
        print("Menu option is invalid, please choose a valid option")
