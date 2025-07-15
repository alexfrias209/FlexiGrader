import random

# Define the maze and correct paths for each question
questions = [
    {
        'question': "Question #1: What is the brain of the car?",
        'options': ["A.) ECU", "B.) Engine", "C.) Battery", "D.) Clutch"],
        'correct_option': random.choice(['A'])
    },
    {
        'question': "Question #2: What is the skull of the car",
        'options': ["A.) Engine", "B.) Fuse Box", "C.) Gasket", "D.) Transmission"],
        'correct_option': random.choice(['B'])
    },
    {
        'question': "Question #3: I am the glue that sticks everything together or the spine of a car?",
        'options': ["A.) Lugnut", "B.) Whell", "C.) Transmission", "D.) Drivetrain"],
        'correct_option': random.choice(['D'])
    },
    {
        'question': "Question #4:" "I am the spianl fluid of the car?",
        'options': ["A.) Steering wheel", "B.) Lube", "C.) Power Steering fluid", "D.) sway bar"],
        'correct_option': random.choice(['C'])
    },
    {
        'question': "Question #5: What are the pockets of the car?",
        'options': ["A.) Glovebox", "B.) cup holder", "C.) compartment", "D.) trunk"],
        'correct_option': random.choice (['C'])
    },
{
        'question': "Question #6: What is the shoe of the car?",
        'options': ["A.) wheel", "B.) tier", "C.) road", "D.) chaisis"],
        'correct_option': random.choice(['B'])
    },
    {
        'question': "Question #7: What is the hat of the car",
        'options': ["A.) roof", "B.) rack", "C.) There is no hat", "D.) bike"],
        'correct_option': random.choice(['C'])
    },
    {
        'question': "Question #8: I am the the nevers that connect the spine to the powerplant of the car?",
        'options': ["A.) Engine", "B.) Flywhell", "C.) Transmission", "D.) Drivetrain"],
        'correct_option': random.choice(['C'])
    },
    {
        'question': "Question #9:" "I am the mouth of the car?",
        'options': ["A.) vent", "B.) grill", "C.) inatke", "D.) hood"],
        'correct_option': random.choice(['A'])
    },
    {
        'question': "Question #10: I am the study process of a car?",
        'options': ["A.) modifications", "B.) tune", "C.) maintence", "D.) dyno"],
        'correct_option': random.choice (['D'])
    },
    # Add more questions if needed
]

# Player starts at the first question
current_question = 0


while current_question < len(questions):
    current = questions[current_question]
    print("\n", current['question'])
    for option in current['options']:
        print(option)

    move = input("Enter your choice (A/B/C/D): ").upper()

    if move == current['correct_option']:
        print("Congratulations! You chose the correct answer.")
        current_question += 1  # Move to the next question
    else:
        print(f"Sorry, that's not the right question. The correct option is {current['correct_option']}. Move on")
        current_question += 1  
print("Congratulations! You have completed the quiz.")