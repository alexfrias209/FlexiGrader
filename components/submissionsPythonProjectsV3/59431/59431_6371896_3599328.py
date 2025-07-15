print("Welcome to the Task Scheduler!")
print("This project allows you to manage your tasks and deadlines.")

# Initialize an empty list to store tasks
task_list = []

# Main program loop
while True:
    print("\nSelect an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Edit a task")
    print("4. Delete a task")
    print("5. Exit")

    # Get user's choice
    user_choice = input("Enter your choice (1/2/3/4/5): ")

    if user_choice == '1':
        # Add a task
        task_name = input("Enter the task name: ")
        task_description = input("Enter task description: ")
        task_deadline = input("Enter task deadline (yyyy-mm-dd): ")
        task = {
            "Name": task_name,
            "Description": task_description,
            "Deadline": task_deadline,
            "Completed": False
        }
        task_list.append(task)
        print("Task added successfully!")

    elif user_choice == '2':
        # View tasks
        print("\n--- Task List ---")
        for index, task in enumerate(task_list):
            status = "Completed" if task["Completed"] else "Not Completed"
            print(f"{index + 1}. {task['Name']} ({status}) - Deadline: {task['Deadline']}")
            from datetime import datetime, date
            deadline_date = datetime.strptime(task['Deadline'], '%Y-%m-%d').date()
            current_date = date.today()
            time_difference = deadline_date - current_date

            # Display the priority based on the time difference
            if time_difference.days < 0:
                priority = "Overdue"
            elif time_difference.days == 0:
                priority = "Today"
            else:
                priority = f"{time_difference.days} days left"
            print(f"   Priority: {priority}")

    elif user_choice == '3':
        # Edit a task
        task_index = int(input("Enter the task number to edit: ")) - 1
        if 0 <= task_index < len(task_list):
            new_name = input("Enter the new task name: ")
            new_description = input("Enter the new task description: ")
            new_deadline = input("Enter the new task deadline (yyyy-mm-dd): ")
            task_list[task_index]["Name"] = new_name
            task_list[task_index]["Description"] = new_description
            task_list[task_index]["Deadline"] = new_deadline
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    elif user_choice == '4':
        # Delete a task
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(task_list):
            del task_list[task_index]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    elif user_choice == '5':
        # Exit the program
        print("Thank you for using the Task Scheduler!")
        break

    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5).")
