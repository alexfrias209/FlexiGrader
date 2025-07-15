print("Welcome to my Project named Work Logger.\n")
print("I am this projects developer.\n")
print("This is designed to log hours worked per each day,week, and month.\n")
print("I will use the minimum wage of the state you input for this example.\n")
user_goal_tf = input("Would you like to set a goal for the amount of money made in a month? \n")
t_f = False

if user_goal_tf.lower() == 'yes':
    t_f = True
else:
    t_f == False

if t_f == True:
    print("(Please be sure to not enter the $.)")
    user_goal = int(input("How much money would you like to make in a month?\n"))
elif t_f == False:
    print("No goal was set\n")


state =input("Please enter your state: \n")

f = open("66052_6453934_6743227.txt","r", encoding="cp1252")
foundstate = False

for myrow in f:
    if state in myrow:
        row = myrow.strip().split("\t")
        if state == row[0]:
            foundstate = True
            state_rate = row[1].find("$")
            minimum = row[1][state_rate+1:6]
print("Minimum wage is set at:",minimum)
minimum_wage = float(minimum)

if t_f == True:
    user_hours = int(user_goal/minimum_wage)
    print("You need to reach a total of around,",user_hours,"hours in order to reach your goal")


name = input("Please enter the employee's name:")

days_of_week =["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
days={"Monday":1,"Tuesday":2,'Wednesday':3,'Thursday':4,"Friday":5,'Saturday':6,'Sunday':7}
week = 1

sum = 0
hours_today = 0
for i in range(1, 5):
    for j in range(0, len(days_of_week)):
        print('On Week ', i,  "| Day: ", days_of_week[j])
        while True:
            hours_today = (input("How many hours did you work today "))
            if hours_today == '':
                continue 
                
            sum += int(hours_today)
            break
if sum >= 100:
    print("\nMight be a good idea to take it easy and rest")
elif sum >= 150:
    print("\nYOU NEED TO RELAX AFTER ALL THAT WORK!!!")
else:
    print("\nJob well done")

total_wage = (minimum_wage * sum )
if t_f ==True:
    if total_wage <= user_goal:
        print("\nAwww sadly you didn't meet your goal of $",user_goal)

    elif total_wage >= user_goal:
        print("\nCongratulations you have met your goal for the month, your goal was set at: $",user_goal)

print("\nThe total wage", name,"have made in the whole month is: $", total_wage)

