import csv

def get_price_range():
    print("\nPlease choose one of the following options:")
    options = ["$500-$1000", "$1000-$1500", "$1500-$2000", "more than $2000"]
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    choice = input("Enter your choice (1-4): ")
    if 1 <= int(choice) <= 4:
        return options[int(choice) - 1]
    else:
        print("Invalid choice.")
        quit()

def get_weather_preference():
    print("\nDo you want to go to a place that is:")
    options = ["cold", "hot", "rainy"]
    # for idx, option in enumerate(options, 1):
    #     print(f"{chr(96 + idx)}. {option}")
    for idx, option in enumerate(options, 1):
      print(f"{idx}. {option}")
  
    choice = input("Enter your choice (1-3): ")
    if 1 <= int(choice) <= 3:
      return options[int(choice) - 1]
    else:
      print("Invalid choice.")
      quit()
    # choice = input("Enter your choice (a-c): ")
    # if choice in ['a', 'b', 'c']:
    #     return options[ord(choice) - 97]
    # else:
    #     print("Invalid choice.")
    #     quit()

def get_time_period():
    print("\nHow long would you like to stay:")
    options = ["one week", "one month", "more than one month"]
    for idx, option in enumerate(options, 1):
      print(f"{idx}. {option}")
  
    choice = input("Enter your choice (1-3): ")
    if 1 <= int(choice) <= 3:
      return options[int(choice) - 1]
    else:
      print("Invalid choice.")
      quit()

def get_people_count():
    print("\nHow many people will be going:")
    options = ["one", "2", "3", "4 or more"]
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    choice = input("Enter your choice (1-4): ")
    if 1 <= int(choice) <= 4:
        return options[int(choice) - 1]
    else:
        print("Invalid choice.")
        quit()

def recommendation(price_range, weather, time, people):
    with open('67875_6408048_7616452.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            if all([
                price_range == line[2].strip(),
                weather == line[3].strip(),
                time == line[4].strip(),
                people == line[5].strip()
            ]):
                print(f"You should vacation at {line[0]}, {line[1]}")

print("Welcome to the Vacation Selector \nChoose what best relates to you and relax")
price_range = get_price_range()
weather = get_weather_preference()
time = get_time_period()
people = get_people_count()
recommendation(price_range, weather, time, people)

