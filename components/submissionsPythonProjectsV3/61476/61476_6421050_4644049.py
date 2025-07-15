#Combining different aspects of the Python project
import csv
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

Your_name = input("Write your name: ")
keep_on_going = "Yes"

while keep_on_going == "Yes":
    print(f"""
    Welcome {Your_name} to Mr.Quiz!
    What would you like to do?
    1. View a histogram of a specific quiz?
    2. Create a file for your class's quizzes?
    """)

    option = int(input("Enter a number for one of the options (Ex. '1'): "))

    def option_1(option):
        quiz = int(input('Which quiz grades would you like to access? (Ex. 1)\n'))
        file_name = input('Enter your file name (It has to be an existing file):')
        csv_file_name = file_name + ".csv"


        print(f'You have chosen quiz {quiz}. Here is your histogram:')

        quizgrades = []
        quizgradesint = []
        rng = [0,50,60,70,80,90,100]

        def get_data_for_x_axis(quiz):                                              #getting values for the x axis values
            with open("61476_6421052_6674366.csv", 'r') as csvfile:#openening the file
                student_grade = csv.reader(csvfile, delimiter = ',')                #reading the csv file identifying commas as separators

                for row in student_grade:                                           #getting indivual rows from the file
                    quizgrades.append(row[quiz])                                    #getting values from each row to create a list of quiz grades respectively


            quizgrades.pop(0)  #removing the word "quiz" from the list "quizgrades"

            for i in range(len(quizgrades)):         # turning strings into numbers
                quizgradesint.append(int(quizgrades[i]))  

            quizgradesint.sort()
            return quizgradesint    #ouput of function


        x = get_data_for_x_axis(quiz)

        # plt.hist()
        plt.hist(x, rng, color='darkblue', edgecolor='orange')

        plt.title(f"Quiz {quiz} grades")
        plt.xlabel("Student scores")
        plt.ylabel("# of students")

        plt.show()



    def option_2(option):
        print("Follow the following prompts:")

        class_data = {}

        Name_inputs = ["Names","names","Name", "name"] #list of possible inputs for the Name column

        while True:
            column_name = input("Enter a name for a column(ex. 'Name' or 'Quiz 1' or type 'exit' to finish): ") #ask teacher for names of columns
            if column_name == "exit":
                break
            elif len(column_name) <= 10:
                if column_name in Name_inputs: #check if this is the name column
                    values = input(f"Enter names for a {column_name} separated by commas (Ex Mark,James,Sarah,...): ")
                    splitvalues = values.split(',')

                else: #if it isn't in the name column then it will be a integer input
                    values = input(f"Enter grades for {column_name} separated by commas (Ex 100,85,70,...): ")
                    splitvalues = values.split(',')
                    splitvalues = [int(i) for i in splitvalues]
            elif len(column_name) >= 10:
                continue


            class_data[column_name] = splitvalues

        data_frame = pd.DataFrame(class_data)

        file_name = input("Enter a name for your file: ")
        csv_file_name = file_name + ".csv"

        data_frame.to_csv(csv_file_name, index=False)

        print(f"CSV file '{csv_file_name}' has been created.")

        print(class_data)

    if option == 1:
        print("1")
        option_1(option)
    elif option == 2:
        print("2")
        option_2(option)
    else:
        print("You entered the wrong input, try again")

    keep_on_going = input("Would you like to continue? (enter Yes or No): ")
else:
    print("""
    Thank you for using Mr.Quiz!
    We are here for all your histogram
    and quiz score logging needs, see you soon!""")