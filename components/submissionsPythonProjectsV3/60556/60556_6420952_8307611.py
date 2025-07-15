
# buzzfeed type quiz
import os 
Quizes = ['Car quiz','Computer quiz','Phone quiz']
def intro(User): # my definition function
    print(f"Welcome to My ME021 project {User}!\nMy name is {coder}, and my project is a quiz similar to buzz feed quizes.")
    print(f"This Buzzfeed quiz required me to make .txt files that includes the questions and answers to the questions.")
    print(f"For the you (the user) the quiz will have you answer each problem then it will tell you if your are 'correct' or 'incorrect'\nIf incorrect it will state the correct answer.")
    print(f"{User} good luck in the tests and thank you so much for participating!!! BEWARE:(ALL Answers should be A,B,C, or D)")
    print(f"The quizes you can choose from are {Quizes}")
coder = 'XXXXXXX'
User = input('Please enter your username to access the quizes[at least 1 character]:')
os.system('clear') #clears terminal 
if len(User) >= 1: #makes sure the user inputed anything for their name. 
    intro(User)
else:
    print("Please run the code once agian and enter a valid input(any character input will work, DONT leave blank)")
    
Quizes = ['Car quiz','Computer quiz','Phone quiz']#the sub quizes in this quiz

quiz_type = input('what quiz would you like to do?')#need to know what quiz the user wants to do
while quiz_type not in Quizes: # this creates a endless loop until the user types one of the 3 options
    print("invalid choice, Please try again")
    quiz_type = input('what quiz would you like to do?')
else: #this breaks the loop once they select one of the quizes
    print(f'youve selected {quiz_type}')

def quiz(quiz_type): #this is the templat for my quizes, this allows me to restart with whatever quiz i wanted. 
    answers = {
        "Phone quiz": ['B', 'C', 'A', 'B', 'C', 'D', 'A', 'B'],
        "Computer quiz": ['B', 'A', 'C', 'C', 'B', 'D', 'C', 'A'], # quiz answer keys
        "Car quiz": ['A', 'B', 'A', 'B', 'B', 'C', 'D', 'B']
    }
    
    questions = [] #sets questions equal to a empty list so the txt file will fill this later 
    
    with open(f"{quiz_type}.txt", 'r') as file: # whith open means it opens the file then with already closes the file itself
        for line in file:# focuses on lines in the file
            questions.append(line.strip().split('\t')) # stris off all unneeded charachters and splits them by tab 
    
    counter = 0# use this later to count the amount of questions answered
    score = 0 #sets score to nothing so the code can increase the number per answer you answer correctly
    
    os.system('clear')# clears terminal
    
    for iteration in range(len(questions)): # this repeats as many times as i have lines of questions and answers
        print(f"{questions[iteration][0]}")  # Print the question
        answer = input('Please enter your answer here: ') #grabs users answer
        answer = answer.upper()# allows you to answer lowercase letters aswell.
        while answer == '' or len(answer) > 1 or (answer not in ['A', 'B', 'C', 'D','a','b','c','d']): #limits you to only answer A, B, C, or D and checks to make sure you answered the problem
            print("unacceptable input please enter a acceptable input!!!") 
            answer = input('Please enter your answer here: ')# if you did not answer it forces you to answer until you do
        
        if answer == answers[quiz_type][iteration]: # checks your answer in the answer key 
            print(f'The last answer "{answer}" was Correct!') #you got it right
            counter += 1 # counts that question
            score += 1
        else:
            print(f'{answer} was incorrect, the answer was {answers[quiz_type][iteration]}') # you got it wrong the correct answer was...
            counter += 1# counts that question

        if counter == 8: # if you answered 8 questions display this question
            print(f"Congratulations {User} you scored {score}/8!")
            finished = input("Congrats on finishing the Quiz, type 1 to quit and type 2 to go back and try another quiz\n\nEnter your choice here: ")
            if finished == "1":
                os.system('clear')
                break # kills the code if you dont want to do any other quizes
                
            else:
                quiz_type = input('Car quiz,Computer quiz,Phone quiz\nwhat quiz would you like to do?\n:')#need to know what quiz the user wants to do
                while quiz_type not in Quizes: # this creates a endless loop until the user types one of the 3 options
                    print("invalid choice, Please try again")# tells the user the input was wrong
                    quiz_type = input('Car quiz,Computer quiz,Phone quiz\nwhat quiz would you like to do?\n:')# regrabs the input 
                else: #this breaks the loop once they select one of the quizes
                    print(f'youve selected {quiz_type}')# tells them what they selected
                    quiz(quiz_type) #restarts the quiz to their input




if len(quiz_type) >= 4: # runs the quiz if you inputed a quiz
    quiz(quiz_type) # call the def
    