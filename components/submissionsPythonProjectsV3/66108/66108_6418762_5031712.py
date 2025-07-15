# Starting to input the city activity names
import os
import csv

def load_activities_from_csv(city_activities, city_name, user_preferences):
  activities = []
  if not os.path.exists(city_activities):
    return activities
  with open(city_activities, mode='r', newline='') as file:
    file = csv.reader(file, delimiter=',')
    print(f"Recommended activites in {city_name}:")

    for row in file:
      if row[0].strip() == city_name and row[2].strip() == user_preferences:
        activities.append(row[1].strip())
        print(row[1].strip())
  return activities


def recommend_activities(activities, user_preferences):
  category = user_preferences['category'].lower()
  outdoor_preference = user_preferences['outdoor'].lower() == "yes"

  return [
      activity for activity in activities
      if category in activity['category'].lower() and (
          outdoor_preference and "outdoor" in activity['category'].lower())
  ]


# Empty to-do list
to_do_list = []


# Display the to-do list
def display_list():
  print("To-Do List:")
  for index, task in enumerate(to_do_list, start=1):
    print(f"{index}. {task}")


def main():
  user = input("What is your name: ")
  city_activities = 'city_activities.csv'
  print("Welcome to your traveling journey!")
  city_name = input("Enter a city of your choosing!: ").lower()
  user_preferences = input("inside or outside? ").lower()
  # user_preferences = {
  #     'category': input("What kind of activity would you prefer?: "),
  #     'outdoor': input("Would you like to be recommended an outdoor activity? (Yes/No): "),
  # }

  activities = load_activities_from_csv(city_activities, city_name,
                                        user_preferences)
  to_do_list = []
  while True and len(activities) != 0:
    decision = input("Would you like to add any activities? ")
    if decision == "no":
      break
    elif decision == "yes":
      pass
    else:
      print("invalid choice")
      continue
    activity = input("What activity would you like to do?: ")
    if activity in activities:
      print(f"You have chosen {activity}")
      to_do_list.append(activity)
      activities.remove(activity)
      print(activities)
    else:
      print("Not an option")

  print("Things saved", to_do_list)


if __name__ == "__main__":
  main()

# Empty to-do list
to_do_list = []


# Display the to-do list
def display_list():
  print("To-Do List:")
  for index, task in enumerate(to_do_list, start=1):
    print(f"{index}. {task}")


# loop
while True:
  print("\nOptions:")
  print("1. Add a task")
  print("2. View tasks")
  print("3. Mark a task as completed")
  print("4. Quit")

  choice = input("Enter your choice (1/2/3/4): ")

  if choice == '1':
    task = input("Enter the adventure you would want to do: ")
    to_do_list.append(task)
    print(f"Added '{task}' to the adventure list.")

  elif choice == '2':
    if not to_do_list:
      print("Your to-do list is empty. Enter more tasks!")
    else:
      display_list()

  elif choice == '3':
    if not to_do_list:
      print(
          "Your to-do list is empty. Put more adventures to your list to mark as completed!"
      )
    else:
      display_list()
      task_index = int(input("Enter the task you want to mark as completed: "))
      if 1 <= task_index <= len(to_do_list):
        completed_task = to_do_list.pop(task_index - 1)
        print(f"You have done '{completed_task}' task!")
      else:
        print("Invalid task index. Please try again!")

  elif choice == '4':
    print("Goodbye! I hope you enjoyed your stay!")
    break

  else:
    print("Invalid choice. Please enter a valid option (1/2/3/4).")