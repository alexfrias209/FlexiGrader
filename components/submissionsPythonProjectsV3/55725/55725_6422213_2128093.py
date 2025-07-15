
print("Welcome to the Car quiz!!! There will be a series of question you have to answer by looking at the image displayed. Goodluck!")
import random

# Define the questions and answers 
quiz_questions = [
    {
        "question": "What car brand does this logo belong to?",
        "image_url": "data:image/jpeg;base64,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",
        "choices": ["Toyota", "Ford", "Chevrolet", "Honda"],
        "correct_answer": "Chevrolet",
    },
    {
        "question": "What car is being shown'?",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRAqPqvKIPTVbkr3ydFMyeNj1DjciE1V695QDyvc9FxwfUxZk-3iJzFoj0-15F4Zz_2Gg&usqp=CAU",
        "choices": ["Toyota Camry", "Ford Focus", "BMW 3 Series", "Honda Civic"],
        "correct_answer": "Toyota Camry",
    },
    {
        "question": "What car brand does this logo belong to'?",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRAqPqvKIPTVbkr3ydFMyeNj1DjciE1V695QDyvc9FxwfUxZk-3iJzFoj0-15F4Zz_2Gg&usqp=CAU",
        "choices": ["Ford", "Hyundai", "BMW", "Honda"],
        "correct_answer": "BMW",
    },
    {
        "question": "What car is being shown'?",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRAqPqvKIPTVbkr3ydFMyeNj1DjciE1V695QDyvc9FxwfUxZk-3iJzFoj0-15F4Zz_2Gg&usqp=CAU",
        "choices": ["Jeep Wrangler", "Subaru WRX", "Chevrolet Silverado", "Toyota Camry"],
        "correct_answer": "Jeep Wrangler",
    },
    {
        "question": "What care brand does this logo belong to'?",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRAqPqvKIPTVbkr3ydFMyeNj1DjciE1V695QDyvc9FxwfUxZk-3iJzFoj0-15F4Zz_2Gg&usqp=CAU",
        "choices": ["Hyundai", "GMC", "Tesla", "BMW"],
        "correct_answer": "Tesla",
    },
    {
        "question": "What car is being shown'?",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRAqPqvKIPTVbkr3ydFMyeNj1DjciE1V695QDyvc9FxwfUxZk-3iJzFoj0-15F4Zz_2Gg&usqp=CAU",
        "choices": ["Chevrolet Corvette", "Ford Mustang", "Toyota Supra", "Cadillac Escalade"],
        "correct_answer": "Toyota Supra",
    },
    {
        "question": "What care brand does this logo belong to'?",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRAqPqvKIPTVbkr3ydFMyeNj1DjciE1V695QDyvc9FxwfUxZk-3iJzFoj0-15F4Zz_2Gg&usqp=CAU",
        "choices": ["Dodge", "Subaru", "Audi", "Mercades"],
        "correct_answer": "Mercades",
    },
    {
        "question": "What car is being shown'?",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRAqPqvKIPTVbkr3ydFMyeNj1DjciE1V695QDyvc9FxwfUxZk-3iJzFoj0-15F4Zz_2Gg&usqp=CAU",
        "choices": ["Ferrari la Ferrari", "GMC Yukon", "Honda Civic", "Dodge Charger"],
        "correct_answer": "Honda Civic",
    },
    {
        "question": "What care brand does this logo belong to'?",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRAqPqvKIPTVbkr3ydFMyeNj1DjciE1V695QDyvc9FxwfUxZk-3iJzFoj0-15F4Zz_2Gg&usqp=CAU",
        "choices": ["Ferrari", "Nissan", "Audi", "Mercades"],
        "correct_answer": "Ferrari",
    },
    {
        "question": "What car is being shown'?",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRAqPqvKIPTVbkr3ydFMyeNj1DjciE1V695QDyvc9FxwfUxZk-3iJzFoj0-15F4Zz_2Gg&usqp=CAU",
        "choices": ["Chevrolet Silverado", "Ford Excursion", "Tesla Model 3", "Dodge Charger"],
        "correct_answer": "Chevrolet Silverado",
    },

]

# Shuffle order of questions
random.shuffle(quiz_questions)

# Initialize the score
score = 0

# Function to display a question and get the user's answer
def ask_question(question_data):
    print(question_data["question"])
    print(f"Options: {', '.join(question_data['choices'])}")
    
    user_answer = input("Your answer: ")
    if user_answer.lower() == question_data["correct_answer"].lower():
        print("Correct!\n")
        return 1
    else:
        print(f"Incorrect. The correct answer is {question_data['correct_answer']}.\n")
        return 0

# Iterate through the questions and ask them
for i, question in enumerate(quiz_questions, start=1):
    print(f"Question {i} / {len(quiz_questions)}")
    score += ask_question(question)

# Display the final score
print(f"You got {score} out of {len(quiz_questions)} questions correct!")

