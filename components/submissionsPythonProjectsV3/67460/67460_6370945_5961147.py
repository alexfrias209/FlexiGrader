#Welcome user
#This helps you get averages in your class

print('Hello. Welcome to my project Gradebook.')

print('Where teachers can input student grades for various sbjects, calculate averages, and retrieve student performance')

print('Please put numbers instead of letters, thank you.')
students = []
grades = []

studentry = True
while studentry == True:
  if input('Is there a student you want to add? (y/n) ') == 'y':
    students.append (input('What is the student\'s name? '))
  else:
    studentry = False

# gin = grade input
def gin():
  for i in range(len(students)):
    try:
      grade = float(input('Enter grade for '+ str(students[i])+":"))
      print('Keep putting numbers in. Good job!')
      grades.append(grade)
      print(f'{students[i]} Recieve a grade of {grades[i]}')
    except ValueError: 
      print('Do NOT put letters, in only numbers. Thank you.You         need to restart. You put in a letter and decimal number.')
      exit()
gin()


total_scores = sum(grades)
total_studs = len(students)
avg =  total_scores / total_studs

print("The average of the students is ", round(avg, 2))

# You have finsihed the code
# This is the gradbook porject