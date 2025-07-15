# Initialize empty lists to store tasks and events
#The code starts by creating two empty lists, tasks and events,
# to store tasks and events, respectively
tasks = []
events = []

# Welcome message
#After initializing the lists, a welcoming message is displayed,
# introducing the "Time Management App Project" developed by Armando Sanchez
# and providing a brief description of the project's purpose
print("Welcome to the Time Management App Project!")

print("Description: This project helps you manage your time efficiently.")

while True:
    # Main menu
    #A main menu is presented with three options, allowing users to select
    # between Task Management, Schedule Management, and exiting the application.
    print("\nMain Menu:")
    print("1. Task Management")
    print("2. Schedule Management")
    print("3. Exit")

    # Get user's choice
    choice = input("Enter your choice (1/2/3): ")

    # Process user's choice
    if choice == '1':
        # Task Management submenu
        #If the user selects option 2 (Schedule Management),
        # a submenu is presented with choices for viewing today's schedule,
        # adding an event, listing events, or returning to the main menu.
        print("\nTask Management Menu:")
        print("1. Add a Task")
        print("2. List Tasks")
        print("3. Delete a Task")
        print("4. Go back to Main Menu")
        task_choice = input("Enter your choice (1/2/3/4): ")

        if task_choice == '1':
            print("You chose to add a task.")
            # Implement task addition logic here
            task_name = input("Enter the task name: ")
            tasks.append(task_name)
            print(f"Task '{task_name}' added successfully!")

        elif task_choice == '2':
            print("You chose to list tasks.")
            # Implement task listing logic here
            if not tasks:
                print("No tasks to display.")
            else:
                print("Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif task_choice == '3':
            print("You chose to delete a task.")
            # Implement task deletion logic here
            if not tasks:
                print("No tasks to delete.")
            else:
                print("Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                task_index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= task_index < len(tasks):
                    deleted_task = tasks.pop(task_index)
                    print(f"Task '{deleted_task}' deleted successfully!")
                else:
                    print("Invalid task number.")

        elif task_choice == '4':
            print("Going back to the Main Menu.")

        else:
            print("Invalid choice.")

    elif choice == '2':
        # Schedule Management submenu
        print("\nSchedule Management Menu:")
        print("1. View Today's Schedule")
        print("2. Add an Event")
        print("3. List Events")  # Added option to list events
        print("4. Go back to Main Menu")
        schedule_choice = input("Enter your choice (1/2/3/4): ")

        if schedule_choice == '1':
            print("You chose to view today's schedule.")
            # Implement schedule viewing logic here
            if not events:
                print("No events scheduled for today.")
            else:
                print("Today's Schedule:")
                for event_name, event_time in events:
                    print(f"{event_time}: {event_name}")

        elif schedule_choice == '2':
            print("You chose to add an event.")
            # Implement event addition logic here
            #Choosing to view today's schedule currently displays events
            # scheduled for today, if any events are stored in the events list.
            # If no events are found, a message informs the user.
            event_name = input("Enter the event name: ")
            event_time = input("Enter the event time (HH:MM AM/PM): ")
            events.append((event_name, event_time))
            print(f"Event '{event_name}' at {event_time} added successfully!")

        elif schedule_choice == '3':
            print("You chose to list events.")
            # Implement event listing logic here
            if not events:
                print("No events to display.")
            else:
                print("Events:")
                for event_name, event_time in events:
                    print(f"{event_time}: {event_name}")

        elif schedule_choice == '4':
            print("Going back to the Main Menu.")

        else:
            print("Invalid choice.")

    elif choice == '3':
        print("Exiting the Time Management App. Goodbye!")
        break

    else:
        print("Invalid choice.")
#The code provides a text-based menu-driven interface for managing tasks and events.
# It allows users to add, list, and delete tasks, as well as add, list, and view
# events for today.



