import random
import csv
import os

# Initialize variables to keep track of the current and previous scores
current_score = 0
previous_score = 0

# Load the previous score from a file (if it exists)
try:
    with open('previous_score.txt', 'r') as file:
        previous_score = int(file.read())
except FileNotFoundError:
    # If the file doesn't exist, set the previous score to 0
    previous_score = 0

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the CSV file
csv_file_path = os.path.join(script_dir, "60978_6422301_2170628.csv")

# Load the CSV file containing image links and color choices
questions = []

try:
    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip the header row if it exists

        for row in reader:
            # Check if the row has at least 3 elements (image link, correct answer, and choices)
            if len(row) >= 3:
                questions.append({'image_link': row[0], 'correct_answer': row[1], 'choices': row[2:]})
            else:
                print(f"Skipping invalid row: {row}")

except FileNotFoundError:
    print(f"CSV file not found: {csv_file_path}")

# Shuffle the questions to present them in random order
random.shuffle(questions)

# Quiz loop
for index, question in enumerate(questions):
    image_link = question['image_link']
    correct_answer = question['correct_answer']
    choices = question['choices']

    print(f"Question {index + 1}:")
    print(f"Previous Score: {previous_score}")
    print(f"Current Score: {current_score}")
    print(f"Guess the color of the image at {image_link}:")

    # Display multiple choice options
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")

    user_choice = input("Enter the number of your choice: ")

    if user_choice.isnumeric():
        user_choice = int(user_choice)
        if 1 <= user_choice <= len(choices):
            user_answer = choices[user_choice - 1]

            if user_answer == correct_answer:
                print("Correct!\n")
                current_score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}\n")
        else:
            print("Invalid choice. Please enter a valid option.\n")
    else:
        print("Invalid input. Please enter a number.\n")

# Display the final score
print("Quiz finished!")
print(f"Your final score is: {current_score}")

# Save the current score as the previous score for the next gameplay
with open('previous_score.txt', 'w') as file:
    file.write(str(current_score))

