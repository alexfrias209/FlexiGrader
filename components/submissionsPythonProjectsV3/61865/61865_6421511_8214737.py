#defines a function: keeps it organized 
def add_contact():
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    phone = input("Enter the phone number: ")
    
    with open("61865_6421512_1359478.txt", "a") as file:
        file.write(f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\n")
    print("Contact added successfully!")

def view_contacts():
    with open("61865_6421512_1359478.txt", "r") as file:
        contacts = file.read()
        print(contacts)

def search_contact():
    search_name = input("Enter the name to search for: ")
    with open("61865_6421512_1359478.txt", "r") as file:
        contacts = file.read()
        if search_name in contacts:
            start = contacts.find(f"Name: {search_name}")
            end = contacts.find("\n\n", start)
            if start != -1:
                print(contacts[start:end])
        else:
            print(f"Contact with name '{search_name}' not found.")

def update_contact():
    search_name = input("Enter the name of the contact to update: ")
    with open("61865_6421512_1359478.txt", "r") as file:
        contacts = file.read()
        if search_name in contacts:
            new_name = input("Enter the new name: ")
            new_email = input("Enter the new email: ")
            new_phone = input("Enter the new phone number: ")
            
            updated_contact = f"Name: {new_name}\nEmail: {new_email}\nPhone: {new_phone}\n"
            contacts = contacts.replace(contacts[contacts.find(f"Name: {search_name}"):contacts.find("\n\n", contacts.find(f"Name: {search_name}"))], updated_contact)
            
            with open("61865_6421512_1359478.txt", "w") as file:
                file.write(contacts)
            print("Contact updated successfully!")
        else:
            print(f"Contact with name '{search_name}' not found.")

def delete_contact():
    search_name = input("Enter the name of the contact to delete: ")
    with open("61865_6421512_1359478.txt", "r") as file:
        contacts = file.read()
        if search_name in contacts:
            start = contacts.find(f"Name: {search_name}")
            end = contacts.find("\n\n", start) + 2
            contacts = contacts[:start] + contacts[end:]
            
            with open("61865_6421512_1359478.txt", "w") as file:
                file.write(contacts)
            print("Contact deleted successfully!")
        else:
            print(f"Contact with name '{search_name}' not found.")

def main():
    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break #exits the while loop; exits the program when users chooses to exit address book 
        else:
            print("Invalid choice. Please try again.")

#prevents code from running when modules are imported: runs main code
if __name__ == "__main__":
    main()
