# begin by introducing the user to the server
print("Welcome to the Fall Semester of 2023 of my public health class!")
print("I will be your instructor.")
print("Yes, Attendence is required and it counts towards your grade.")
print()
#Show them an example of how the data will be shown.
#2D lists = a list of lists
print("This is how I will share data, but with larger data of course")
names = ["Student names"]
course = ["Class name"]
days = ["Weekday: Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
data = [names,course,days]
print(data)
print()
print()
# allow the user to choice how they take attendence
print("How will you like attendance to be taken?")
attendence = ["Roll call during class","Determine who is present through the seating chart.", "Do in-class activities"]
print("1", attendence [0])
print("2", attendence [1])
print("3", attendence [2])
#Keep repeating the question if no one responds with while loops
choice = ""
while len(choice)==0:
    choice = input("Please enter your choice here.(1/2/3):")
print()
# allow the user to choose their prefer activity
if attendence == "3":
    print("Please select the activity you want to complete in class")
    activity = ["In-class Quizzes", "worksheets", "Group Assignment", "Discussion Questions"]
    print("e", activity [0])
    print("i", activity [1])
    print("o", activity [2])
    print("u", activity [3])
    activity = input("Please enter yur choice here. (e/i/o/u):")
print()
# allow user to choose when they want to do their activity
print("Please select when you want attendence to be taken?")
time = ["Beginning of class", "Middle of class", "End of class"]
print("A", time [0])
print("B", time [1])
print("C", time [2])
print()
#Keep repeating the question if no one responds with while loops
choice = ""
while len(choice)==0:
    choice = input("Please enter your choice here.(A/B/C):")
print()

#Let users come to you and ask to see their attendance rate
print("Because I am keeping track of attendance, come to me to see your attendance rate")
name = input("Hello, what is your name?: ")
day = input("What day will you like to see? ")

print("Hello "+name)
print("Sounds good. You would like to see "+str(day)+" of 2023")

# provide the user with their choices and the data table
while True:
    if attendence == "1" and "A":
        print("You have selected to take attendence with roll call at the beginning of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
    
    if attendence == "1" and "B":
        print("You have selected to take attendence with roll call in the middle of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()

        
    if attendence == "1" and "C":
        print("You have selected to take attendence with roll call at the end of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
        
    if attendence == "2" and "A":
        print("You have selected to take attendence with the seating chart at the beginning of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
    
    
    if attendence == "2" and "B":
        print("You have selected to take attendence with the seating chart in the middle of class.")
        print()
    
        
    if attendence == "2" and "C":
        print("You have selected to take attendnece with the seating chart at the end of class.")
        print()
    
    
    if attendence == "3" and "e" and "A":
        print("You have selected to take attendence by doing an in-class quiz at the beginning of clsss.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
   
    
    if attendence == "3" and "e" and "B":
        print("YOu have selected to take attendence by doing an in-class quiz in the middle of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
  
    
    if attendence == "3" and "e" and "C":
        print("You have selected to take attendence by doing an in-class quiz at the end of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
 
    if attendence == "3" and "i" and "A":
        print("You have selected to take attendence by doing a worksheet at the beginning of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
   
    if attendence == "3" and "i" and "B":
        print("You have selected to take attendence by doing a worksheet in the middle of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
   
    if attendence == "3" and "i" and "C":
        print("You have selected to take attendence by doing a worksheet at the end of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
   
    if attendence == "3" and "o" and "A":
        print("You have selected to take attendence by doing a group assignment at the beginning of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()

        break
    if attendence == "3" and "o" and "B":
        print("You have selected to take attendence by doing a group assignment in the middle of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
   
    if attendence == "3" and "o" and "C":
        print("You have selected to take attendence by doing a group assignment at the end of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
   
    if attendence == "4" and "u" and "A":
        print("You have selected to take attendence by answering a discussion question at the beginning of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
   
    if attendence == "4" and "u" and "B":
        print("You have selected to take attendence by answering a discussion question in the middle of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()
   
    if attendence == "4" and "u" and "C":
        print("You have selected to take attendence by answering a discussion question at the end of class.")
        print()
        print("Thank you for participating and you will be able to see the class results.")
        print()

    import csv
    with open(r"./61879_6422059_434448.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
        print()
        import matplotlib.pyplot as plt
        x_axis = ['','Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday']
        y_axis = ['0', '14', '12', '6', '9', '16']
        plt.bar(x_axis, y_axis)
        plt.title('Public health class attendance histogram', fontsize = 14, weight = "bold")
        plt.xlabel('Activity')
        plt.ylabel("percentage")
        plt.show()
        break