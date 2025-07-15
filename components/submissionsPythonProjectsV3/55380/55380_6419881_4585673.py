print('Welcome to the Financial Aid Calculator')
print('This calculator estimates your cost of attendance of schools in the University of California system')
print('Answer the following questions to estimate your cost of attendance')
print("Cost of attendance is calculated on the 2023-2034 academic year using the Universities' websites" )
print()
print()

# List of the Universities which the user can choose from
print("Here is a list of all the Universities of California")
print("1. UC Berkeley")
print("2. UC Davis")
print("3. UC Irvine")
print("4. UCLA")
print("5. UC Merced")
print("6. UC Riverside")
print("7. UC San Diego")
print("8. UC Santa Barbara")
print("9. UC Santa Cruz")

# Dictionary that matches universities to a user input integer
campuses = {
    1: "UC Berkeley",
    2: "UC Davis",
    3: "UC Irvine",
    4: "UCLA",
    5: "UC Merced",
    6: "UC Riverside",
    7: "UC San Diego",
    8: "UC Santa Barbara",
    9: "UC Santa Cruz",
    }

# This function is used to pull information from the text file given a specific row and column
def text_file(row,column):
    with open('55380_6419882_5601743.txt', 'r') as text:
        line = text.readlines()
        school = line[row].split()
        cost = school[column]
        return(cost)

# User inputs school to determine the tuition
university = int(input("What University of California will you be attending. Input the number next to the university name: "))


# Prints the university chosen by the user
if university in campuses:
    print("You choose", campuses[university])
    print()
    print()
    tuition = int(text_file(university,1))

# Determines if housing and food should be added to the cost of attendance
for i in range(1,100):
    on_campus = input('Will you be living on campus? (yes/no) ')
    if on_campus == 'yes':
        print('You chose YES to living on campus ')
        housing = int(text_file(university,2))
        break
    elif on_campus == 'no':
        print('You chose NO to living on campus ')
        housing = 0
        break
    else:
        print('Sorry I do not understand your response please try typing just yes or no')
print()
print()

# Cost of books, supplies, transportation, and personal expenses based off the school that the user chose
books_and_supplies = int(text_file(university,3))
transportation = int(text_file(university,4))
expenses = int(text_file(university,5))

# Determines if health insurance cost should be added to the cost of attendance
for i in range (1,100):
    health = input('Do you have your own health insurance? (yes/no) ')
    if health == 'yes':
        print('Great! You have your own health insurance. ')
        insurance = 0
        break
    elif health == 'no':
        print('No worries, your school will be provided with health insurance. ')
        insurance = int(text_file(university,6))
        break
    else:
        print('Sorry I do not understand your response please try typing just yes or no')
print()
print()

# Determines the amount of Financial Aid
for i in range(1,100):
    aid = input('Are you receiving any Financial Aid? (yes/no) ')
    if aid == 'yes':
        aid = float(input('How much aid are you receiving from Financial Aid? (enter integers only with no commas) '))
        print(f'You are receiving ${aid:.0f} from these Financial Aid')
        break
    elif aid == 'no':
        print('You are not receiving money from Financial Aid ')
        aid = 0
        break
    else:
        print('Sorry I do not understand your response please try typing just yes or no')
print()
print()

# Determines the amount of Scholarships
for i in range(1,100):
    scholarships = input('Do you have any scholarships, grants, or other types of financial help? (yes/no) ')
    if scholarships == 'yes':
        scholarships = float(input('How much aid are you receiving from these scholarships? (enter integers only with no commas) '))
        print(f'You are receiving ${scholarships:.0f} from these scholarships')
        break
    elif scholarships == 'no':
        print('You are not receiving aid from scholarships ')
        scholarships = 0
        break
    else:
        print('Sorry I do not understand your response please try typing just yes or no')
print()
print()

# Stores the total cost of attedence
total = tuition + housing + books_and_supplies + transportation + expenses + insurance - aid - scholarships

# Breaks down the cost of attendance
print(f'Here is your cost of attendance estimate')
print(f'Tuition: ${tuition}')
print(f'Food and Housing: ${housing}')
print(f'Books and Supplies: ${books_and_supplies}')
print(f'Transportation: ${transportation}')
print(f'Personal Expenses: ${expenses}')
print(f'Health Insurance: ${insurance}')
print(f'Financial Aid: -${aid:.0f}')
print(f'Scholarships: -${scholarships:.0f}')
print(f'Total Cost: ${total:.0f}')
#layout of individual costs

print()
print(f'Your total cost of college for this semester will be ${total:.0f}')
print('Rerun this code a few times to compare the prices of each school')
print('Check your file explorer app and look for a text file named "Compare".')
print('This file will contain information of each school you chose')

# This creates a new text file which keeps track of the output each time the code is run
with open("55380_6419882_5601743.txt", "a") as compare:
    compare.write(f"{campuses[university]}: ${total}")
    compare.write("\n")






