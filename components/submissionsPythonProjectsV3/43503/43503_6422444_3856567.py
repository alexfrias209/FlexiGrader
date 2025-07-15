# I welcome the user
print()
print('This project is meant to help undergraduate students find research opportunities based on their interests.',
      'The student will choose from a list that contains different research departments.',
      'You will choose the department that you are interested in doing research for. Based on questions,',
      'this project will give you information on research available at UC Merced and give links to corresponding faculty.')

print()
prin('Displayed below is a bar graph that demonstrates all the research opportunities based on departments at UCM')

#this dispays the pie chart of majors at UC Merced by department
#must have matplotlib to open chart or else will have error
#can uncomment until next # to run rest of code, without chart 

##opens up file to pie chart
##from matplotlib import pyplot as plt
##
##plt.style.use("fivethirtyeight")
##
##slices = [5,7,3]
##labels = ['Natural Science', 'Engineering', 'Social Science and Humanities']
##
##plt.pie(slices, labels = labels, wedfeprops={'edgecolor': 'black'})
##
##plt.tite("Research at UC Merced")
##plt.tight_layout()
##plt.show()
###


#this presents 3 departments at UCM and asks user to choose
print('The departments of research at UCM are:',
      '\n 1.Natural sciences',
      '\n 2.Engineering',
      '\n 3.Social Sciences, Humanities, and Arts')
print ()

department = int(input('What department of research are you interested in? Choose 1,2, or 3 '))
print()


#imports csv file with all categories 
import csv

with open('43503_6422445_4166082.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    next(csvFile)
    print('These are the topics of research for this department: ')
    for lines in csvFile:
        if (department == 1):
            print(lines[0])
        if (department == 2):
            print(lines[1])
        if (department == 3):
            print(lines[2])
        


sub_department = int(input('What topic are you interested in? '))
#this look displace final result which is to show user the categories of research 
with open('43503_6422445_4166082.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    next(csvFile)
    print('These are the research specialties availible at UC Merced for this topics: ')
    for cat in csvFile:
        if (department == 1) and (sub_department == 1):
            print(cat[3])
            
        if (department == 1) and (sub_department == 2):
            print(cat[4])
           
        if (department == 1) and (sub_department == 3):
            print(cat[5])
            
        if (department == 1) and (sub_department == 4):
            print(cat[6])
            
        if (department == 1) and (sub_department == 5):
            print(cat[7])
            
        if (department == 2) and (sub_department == 1):
            print(cat[8])
            
        if (department == 2) and (sub_department == 2):
            print(cat[9])
            
        if (department == 2) and (sub_department == 3):
            print(cat[10])
            
        if (department == 2) and (sub_department == 4):
            print(cat[11])
            
        if (department == 2) and (sub_department == 5):
            print(cat[12])
            
        if (department == 2) and (sub_department == 6):
            print(cat[13])
            
        if (department == 2) and (sub_department == 7):
            print(cat[14])
            
        if (department == 3) and (sub_department == 1):
            print(cat[15])
            
        if (department == 3) and (sub_department == 2):
            print(cat[16])
            
        if (department == 3) and (sub_department == 3):
            print(cat[17])







      