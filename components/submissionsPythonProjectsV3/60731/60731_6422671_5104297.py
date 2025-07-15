print('yo')
print('Marvel Quiz: Test Your Knowledge on the MCU')
def run_quiz():
    questions = [
        "1. Did Tony Stark die in the MCU on October 17th, 2023? (a) yes (b) no",
        "2. Did Thor's hammer, Mjolnir, break in the MCU? (a) yes (b) no",
        "3. Was Spider-Man introduced in the MCU in 'Captain America: Civil War'? (a) yes (b) no",
        "4. Who attacked Tony Stark in the desert? (a) The Ten Rings (b) HYDRA (c) AIM",
        "5. Did Thanos win in Infinity War? (a) yes (b) no",
        "6. Did Star Wars and Marvel do an MCU crossover? (a) yes (b) no",
        "7. Who stole the vibranium from Wakanda? (a) Red Skull (b) Klaw (c) Killmonger",
        "8. Who killed Thanos? (a) Iron Man (b) Captain America (c) Thor",
        "9. Who is Wanda's brother? (a) Pietro Maximoff (b) Clint Barton (c) Sam Wilson",
        "10. What is Deadpool's name? (a) Logan Howlett (b) Wade Wilson (c) Peter Parker",
        # Add more questions here...
    ]

    # Correct answers
    answers = ["a",  # Answer for Question 1
               "a",  # Answer for Question 2
               "a",  # Answer for Question 3
               "a",  # Answer for Question 4
               "a",  # Answer for Question 5
               "b",  # Answer for Question 6
               "b",  # Answer for Question 7
               "c",  # Answer for Question 8
               "a",  # Answer for Question 9
               "b",  # Answer for Question 10
               # Add more answers here...
               ...]

    score = 0

    for question, correct_answer in zip(questions, answers):
        response = input(question + " ").lower()

        if response == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", correct_answer)

    print("Your Score:", score, "out of", len(questions))
    
    # Ask the user if they want to restart the quiz
    restart = input("Do you want to restart the quiz? (yes/no) ").lower()
    if restart == "yes":
        run_quiz()

# Run the quiz
run_quiz()
