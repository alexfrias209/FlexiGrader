import time

# Define the scenarios for each level
scenarios = [
    [
        "\nLake Yosemite",
        "You find yourself at Lake Yosemite. Your goal is to make it back to your dorm.",
        [
            "A.) Swim across the lake",
            "B.) Walk around the lake",
            "C.) Walk around the world",
            "D.) Sit and Wait"
        ]
    ],
    [
        "\nRoad to Campus",
        "You have made it to the entrance of Lake Yosemite. What is your next move?",
        [
            "A.) Go into the fields",
            "B.) Walk down the path",
            "C.) Run on the road",
            "D.) Wait for a car"
        ]
    ],
    [
        "\nMissing: Keys, CatCard, Phone",
        "You have made it to campus but forgot your backpack in one of your classes. What's your next move?"
        "(Your backpack has items like your phone, CatCard, and Keys)",
        [
            "A.) Call your friends to let you in the dorm",
            "B.) Go to all your classes starting with the last",
            "C.) Wait for someone to open the dorm for you",
            "D.) Go find your friends"
        ]
    ],
    [
        "\nFind My Roommate",
        "You found yourself in your classroom, and your friend has your bag. You're still missing your CatCard. What's your next move?",
        [
            "A.) Go home for the weekend",
            "B.) Spend the night in your friend's dorm",
            "C.) Ask your friend where they are at",
            "D.) Call your roommate"
        ]
    ],
    [
        "\nNew Beginnings Statue",
        "Your roommate with your CatCard is at the New Beginnings statue. What's your next move?",
        [
            "A.) Get your CatCard",
            "B.) Stay with Friend",
            "C.) Wait for your roommate",
            "D.) Get food"
        ]
    ],
    [
        "\nDorm Time",
        "You're heading to your dorm after a lot of walking. What do you do?",
        [
            "A.) Homework",
            "B.) Shower",
            "C.) Sleep",
            "D.) Stay up late gaming (League, Apex, Smash Bros)"
        ]
    ]
]

# Initialize game variables
correct_answers = ["B", "C", "B", "D", "A", "B"]
best_time = float("inf")
death_counter = 0

print("\nWelcome to the UCM Maze Game!")

for level, (level_name, level_description, level_options) in enumerate(scenarios):
    print(level_name)
    print(level_description)
    print("Options:")
    for option in level_options:
        print(option)

    start_time = time.time()
    move = input("Enter your choice (A/B/C/D): ").upper()

    if move == correct_answers[level]:
        print("Congratulations! You chose the correct path.")
    else:
        print("You went down the wrong path.")
        death_counter += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    if elapsed_time < best_time:
        best_time = elapsed_time

    print(f"Your best time: {best_time:.2f} seconds")
    print(f"Death Counter: {death_counter}")

    if level < len(scenarios) - 1:
        choice = input("Would you like to continue to the next level (YES/NO): ").upper()
        if choice != "YES":
            break
    else:
        print("Congratulations! You have successfully completed the maze!")

# Save the total death counter to a text file
with open("total_death_counter.txt", "w") as file:
    file.write(f"Total Death Counter: {death_counter}")
