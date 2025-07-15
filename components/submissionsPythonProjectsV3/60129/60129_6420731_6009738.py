# Sample list of potential roommates
potential_roommates = [
    {"name": "Alice", "age": 25, "smoke": False, "animals": False},
    {"name": "Bob", "age": 30, "smoke": True, "animals": False},
    {"name": "Charlie", "age": 22, "smoke": False, "animals": True},
    {"name": "David", "age": 27, "smoke": True, "animals": True}
]

# Ask user for their information
user_name = input("What is your name? ")
user_age = int(input("How old are you? "))
user_smoke = input("Do you smoke (yes/no)? ").lower() == "yes"
user_animals = input("Do you have animals (yes/no)? ").lower() == "yes"

# Initialize variables for matching roommate
matching_roommate = None

# Iterate through potential roommates
for roommate in potential_roommates:
    if (
        abs(user_age - roommate["age"]) <= 5 and
        (user_smoke == roommate["smoke"] or user_animals == roommate["animals"])
    ):
        matching_roommate = roommate
        break

# Check if a matching roommate was found
if matching_roommate:
    print(f"We found a potential roommate for you: {matching_roommate['name']}")
else:
    print("Sorry, we couldn't find a suitable roommate for you.")
