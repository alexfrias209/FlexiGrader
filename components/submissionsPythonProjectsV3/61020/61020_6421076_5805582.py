

output_file = open('61020_6421078_256923.txt', 'w')



thing = open('61020_6421077_3080796.txt','r')
v = thing.readlines()
for line in v:
    week_days = line.split(' ')
thing.close()
#week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#Days of the week
days = int(input('Type amount of days per week you would like to exercise: '))
#Getting rid of days per week that are not real
while  days > len(week_days) or days == 0 or days < 0:
    print('Please enter a number between 1-7 :')
    days = int(input('Type amount of days per week you would like to exercise: '))

muscle_groups = ['Chest', 'Back', 'Legs', 'Arms'] * days
#Different muscle groups^
muscle_targets = {0: 'Bench Press, Dumbbell Chest Press, Cable Chest Fly',
                  1: 'Barbell Rows, Lat Pulldown, Cable Rows',
                  2: 'Squat, Hamstring Curls, Goblet Squats' ,
                  3: 'Bicep Curls, Skull Crushers, Dumbbell Shoulder Flys',
                  4: 'Bench Press, Dumbbell Chest Press, Cable Chest Fly',
                  5: 'Barbell Rows, Lat Pulldown, Cable Rows',
                   6: 'Squat, Hamstring Curls, Goblet Squats'
                  }

muscle_groups_wom = [ 'Back', 'Legs','Chest'] * days
muscle_targets_wom = {0: 'Barbell Rows, Lat Pulldown, Cable Rows',
                  1: 'Squat, Hamstring Curls, Goblet Squats' ,
                  2: 'Bench Press, Dumbbell Chest Press, Cable Chest Fly',
                  3: 'Barbell Rows, Lat Pulldown, Cable Rows',
                   4: 'Squat, Hamstring Curls, Goblet Squats',
                  5: 'Bench Press, Dumbbell Chest Press, Cable Chest Fly',
                  6: 'Barbell Rows, Lat Pulldown, Cable Rows',
                  }
#Excersizes to Target Muscle Groups^

#cal_men
y = int(2500)
#cal_wom
y1 = int(2000)

#General Callorie recomendations for men and women^

user_gen = str(input('Please enter gender, "Man" or "Woman". ' ))
while user_gen != 'Man' and user_gen != 'Woman':
    print('Please select "Man" or "Woman" ')
    user_gen = str(input('Please enter gender, "Man" or "Woman". ' ))
#user_cal
x = int(input('Please enter estimated number of calories consumed per day '))

#Gets users gender and estimated caloric intake^

def print_cal_man (x,y):
    #x = user_cal
  #  y = cal_men
    if x == y:
        k = 'You are currently maintaining by average standards'
    elif x >= y:
        k = 'You are in a caloric surplus by average standards'
    else :
        k = 'You are in a caloric deficit by average standards'
    return k

def print_cal_wom (x,y1):
    #x = user_cal
  #  y1 = cal_wom
    if x == y1:
        k1 = 'You are currently maintaining by average standards'
    elif x >= y1:
        k1 = 'You are in a caloric surplus by average standards'
    else :
        k1 = 'You are in a caloric deficit by average standards'
    return k1

print('For your workout plan',file=output_file)
if user_gen == 'Woman':
    muscle_groups = muscle_groups_wom
    muscle_targets = muscle_targets_wom



if days == 5 or days == 6 or days == 7:
    for day in range(0, days):
        print('On ', week_days[day],'you will work out ', muscle_groups[day],'by doing:', muscle_targets[day],file=output_file)
        
#
if days == 1:
    print('On ', week_days[2], 'you will work out\n ', muscle_groups[0:3],
          'by doing:\n', muscle_targets[0],'\n', muscle_targets[1],'\n', muscle_targets[2],'\n', file=output_file)

if days == 2:
    print('On ', week_days[0],'and', week_days[4], 'you will work out\n ', muscle_groups[0:3],
          'by doing:\n', muscle_targets[0],'\n', muscle_targets[1],'\n', muscle_targets[2],'\n', file=output_file)

if days == 3:
    print('On ', week_days[0],'you will work out ', muscle_groups[0],'by doing:', muscle_targets[0], file=output_file)
    print('On ', week_days[2],'you will work out ', muscle_groups[2],'by doing:', muscle_targets[2], file=output_file)
    print('On ', week_days[4],'you will work out ', muscle_groups[4],'by doing:', muscle_targets[4], file=output_file)

if days == 4:
    print('On ', week_days[0],'you will work out ', muscle_groups[0],'by doing:', muscle_targets[0], file=output_file)
    print('On ', week_days[1],'you will work out ', muscle_groups[1],'by doing:', muscle_targets[1], file=output_file)
    print('On ', week_days[3],'you will work out ', muscle_groups[2],'by doing:', muscle_targets[2], file=output_file)
    print('On ', week_days[4],'you will work out ', muscle_groups[3],'by doing:', muscle_targets[3], file=output_file)
#
if user_gen == 'Man':
    print (print_cal_man(x,y), file=output_file)
else:
    print (print_cal_man(x,y1), file=output_file)

print(' If you want more accurate information regarding calories and nutrition information please visit "https://www.iifym.com/" for a personalized assessment. ', file=output_file)

print('Please check file')
#with open('workout_plan.txt', 'a') as file:
 #   text_to_add= 
 #   file.write(text_to_add)
    
output_file.close()
