import re
import matplotlib.pyplot as plt
import time
def repeat_input(prompt, *answers, Number = False):
    x = True
    while x:
        y = input(f'{prompt} ')
        if Number:
            try:
                return int(y)
            except ValueError:
                print("That is not a number")
                time.sleep(1)   
        elif y.lower() in answers:
            x = False
            return y
        else:
            print("\nThat is not an answer. \nPlease try again \n")
            time.sleep(1)   

def reading(Studentname,x = False):
    if Studentname == "N/A" and x:
        for line in gradefile:
            print(line)
    else: 
        for line in gradefile:
            Buffer = re.findall(f'{Studentname}:, ', line)
            if Buffer:
                return(line)



x = "yes" 

#Allows you to do everything over agian if theres still something you have to do
while x.lower() == "yes": 


                ### Input "test". I have a example class called "test" ###

    class_select = input("What class are you looking for? ")
    class_select = f"{class_select}66879_6403336_6971077.txt" #Makes a new class with "Gradebook.txt" at the end so it doesnt get mixed up with other files

   #asks what you want
    Check_or_Add = repeat_input("Are you adding or checking something? \n (Checking or adding)\n ", "checking","adding")


    if Check_or_Add.lower() == "adding":
        Student_or_assignment = repeat_input("Are you adding a new student or assignment? \n(Student or Assignment?)\n ","student","assignment")
        #adding a new student
        if Student_or_assignment.lower() == "student":

                with open(class_select, "a") as gradefile:

                    numofstudent = repeat_input("How many student are you adding?", Number=True)
                    for i in range(numofstudent):
                        name = input("What is the name of the stduent? ")
                        gradefile.write(f'{name}:,\n')

        #adding a new assigment and grade
        elif Student_or_assignment.lower() == "assignment":
            try:
                with open(class_select, "r+") as gradefile:
                    lines = gradefile.readlines()
                    gradefile.seek(0)  # Reset the file position to the beginning

                    assign_name = input("What is the assignment's name? ")
                    total_points = repeat_input("How many point is the assignment worth? ", Number=True)


                    for line in lines:
                        Work = {}
                        student_data = line.strip().split(" ")
                        print(student_data[0])
                        assign_grade = repeat_input("What is their grade? ",Number=True)

                        #Calc the grade for assignment
                        assign_grade = (assign_grade/total_points) * 100


                        Work[assign_name] = assign_grade

                    # Append the new assignment and grade to the line
                        student_data.append(str(Work).strip("{ }"))
                        updated_line = " ".join(student_data)
                        gradefile.write(updated_line + "%" + "," + "\n") 

            except FileNotFoundError:
                print("The class,",class_select ,"could not be found")
    


    elif Check_or_Add.lower() == "checking":
        try:
            with open(class_select, "r") as gradefile:
                
                ### Input "Tom". I have a example student name Tom
                
                Studentname = input("What is the studnet name? ")
                Student_line = reading(Studentname)
    
                #Gets the score from each assignment 
                try:
                    components = Student_line.split(",")
                except AttributeError:
                    print("Could not find student")
                    continue
                print(Student_line)
                assignment_values = []
                for component in components:
                    if '%' in component:
                        # Use regular expressions to extract the percentage values
                        assignment_match = re.search(r'(\d+\.\d+)%', component)
                        if assignment_match:
                            assignment_values.append(float(assignment_match.group(1)))

                #Calc the gpa for the student
                Student_overall_grade = sum(assignment_values) / len(assignment_values)
                if Student_overall_grade > 90.0:
                    letter_grade = "A"
                elif Student_overall_grade < 90 and Student_overall_grade > 80:
                    letter_grade = "B"
                elif Student_overall_grade < 90 and Student_overall_grade > 70:
                    letter_grade = "C"
                elif Student_overall_grade < 70 and Student_overall_grade > 60:
                    letter_grade = "D"
                else:
                    letter_grade = "F"
                
                print(f"The stduent's overall class grade is {Student_overall_grade}% or a {letter_grade}")
                #Graph the grade over time
                

                x_axis = list(range(1, len(assignment_values) + 1)) #creates the x axis by making a list based off the amount of assignments
                
                plt.plot(x_axis, assignment_values, linestyle='dashed',linewidth = 1, marker='o', markerfacecolor='blue')
                plt.ylim(0,101) 
                plt.xlabel('amount of assignment') 
                plt.ylabel('grade for assignment') 
                plt.title(f"{Studentname}'s GPA") 
                time.sleep(1)
                plt.show() 




        except FileNotFoundError:
            print("The class,",class_select ,"could not be found")
            continue
    
    #Allows you to type again
    Command_redo = True
    while Command_redo:
        x = repeat_input("Is there still something you want to do? \n(Use /help to show more commands)\n \nYes or No \n","yes","no","/help","/add class","/read class")

        if x.lower() == "/help":
            print("Here are some commands \n/add class \n/read class \n \n(Note this will only work if you are ask if you still want to do something) ")
            continue

        elif x.lower() == "/add class":
            new_class = input("\nWant to add new class? \nYes or No ")

            #Makes a new class with "Gradebook.txt" at the end so it doesnt get mixed up with other files
            if new_class.lower() == "yes":
                class_select = input("\nwhat is the class name? ")
                class_name = f"{class_select}66879_6403336_6971077.txt"
                gradefile = open(class_name,"w")
                gradefile.close()

        elif x.lower() == "/read class":
            Fullclassread = str(class_select)
            #Opens the file and reads the whole thing
            with open(Fullclassread, "r") as gradefile:
                print(reading("N/A",True)) #without the extra print() it doesnt print the whole file
        else:
            Command_redo = False


print("Goodbye")