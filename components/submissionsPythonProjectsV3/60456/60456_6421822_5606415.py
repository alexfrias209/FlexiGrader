print('Hello, and welcome to Your-Fitness-Pal!')
print('')
print('I am an simple, interactive fitness app that helps you stay accountable on your fitness journey.')
# Introduction

help = False
# The help function is initialized to be false.

#There needs to be a loop so that the user is forced into answering yes or no, if they answer otherwise they will be prompted to reanswer.
while True:
    doyouneedhelp = input('Before we start your fitness journey, would you like to enable advice and suggestions? (yes/no)')
    if doyouneedhelp.lower() == 'yes':
        print('Fantastic, I will help you reach your goals on your fitness journey.')
        help = True
        break
        # If help request is returned with a yes, help is enabled by being validated as true. Loop is then broken.
    elif doyouneedhelp.lower() == 'no':
        print('Awesome, I will provide you with only representations of your choices.')
        break
        # If help request is returned with a no, help is left as disabled. Loop is then broken.
    else:
        print('Please either answer yes or no.')
        # The user is not allowed to answer anything other than yes or no, if they do they are told what they can't do and promptly returned to the input function. 

# This is part of the suggestions enabled services, the user is provided with the input ability to provide weight and average calorie consumption. 
# User will be allowed to decide a simple discpline of gaining weight, keeping weight, or losing weight.

#Help enabled section 1-------------------------------Pre-decision 

#These are preliminary questions to help the user with some functions down the line.
if help == True:
    while True:
        try:
            weight = int(input('Please input your body weight in pounds(lb): '))
            halfweight = weight * 0.5
            # Here I define what half of weight is, simply called halfweight. This is used later as a means of getting 0.5 of the integer of weight in lbs.
            break
        except ValueError:
            print('Please enter a valid integer for weight in pounds.')
    # I make sure to specify the weight needs to be inputed in the ubit of pounds (lbs). Some of the functions of this program involve academically backed advice which requires conversions based on ratiors of grams:pounds. In other words, to not over complicate the suggestions and the calculations for them, I have restricted the option.
    while True:
        try:
            usercaloriebef = int(input('Please, take the time you count the average amount of calories you consume in a day. What is the average amount of calories you consume in a day?'))
            break
        except ValueError:
            print('Please enter a valid integer for your average calorie intake in a day.')
            


if help == True: 
    print('You have inputed', weight, ' lbs. Many health experts suggest for those looking to increase in muscle mass to consume anywhere from 0.5 to 1 gram of protein for every pound of body weight they have, which would mean you would need to consume anywhere from', halfweight, 'to', weight, 'grams of protien a day.') 
    print('Of course, you must take into consideration lifestyle, the more intensly active you are, the more your body is going to need protien to rebuild the muscles bigger and better!')
    print('This is one example of the many ways Your-Fitness-Pal will aid you on your fitness journey.')
    print('')
    print('To better help match you to your preferred fitness lifestyle, please choose one of the prewritten phrases below that most aligns with your goal.')
    print('1) I just want to lose some weight')
    print('2) I want to maintain body weight [maintain calories]')
    print('3) I would like to gain muscle mass')
    while True:
        try:
            choice = int(input('Input option number here: [EX: 1]'))
            if choice == 1:
                break
            if choice == 2:
                break
            if choice == 3:
                break
        except ValueError:
            print('Please enter the number that correlates with the choice that fits your intentions the most.')
            #Since by our definition of the variable choice, it is an integer, anything that is entered into the input option for the vairable "choice" will be ran through the "int" function. Words[As well as number options I have not given] as the user input send the user back to the input request. Value error would be a word being read as an integer.


#Help enabled section 2-------------------------------decision brances


# Since the user has enabled help, they are to be helped in choosing a healthy calorie deficit. There is a loop that holds true until the user picks an appropriate value for the deficit. If the user doesn't want these restrictions, they could have chose help disabled.
# Here we are checking for help status
if help == True:
    if choice == 1:
     # Here I am checking for suggestion choice. This same process is repeated for appropriate responses (1, 2, 3).
        print('You have chosen: I just want to lose some weight')
        while True:
            # A loop is created here. So long as this loop is to exist, the user is to be asked to input a calories choice. From how I set it up, the input will always be ran though as an integer. For appropriate integer responses, the user breaks the loop and proceeds. For an integer response that is restricted by the advice feautre, the user is returned to input. For any character inputs other than numbers, the user creates a value error and is told to input an appropriate response. They are returned to input.
            try:
                calchoice = int(input(f'Considering your weight is {weight} lbs and you would like to lose weight, you must now decide the calorie deficit you would like to be on. Please choose a number between 300 to 500 to subtract from your current average calorie intake: '))
                if 300 <= calchoice <= 500:
                    print('Great choice.')
                    usercalgain = usercaloriebef - calchoice
                    usercal1111 = usercalgain
                    #Usercal1111 is used to refer to the calories a user will consume. This is regardless of if the user is in surplus or deficit or maintaining. Usercal1111 is a general name used to define across the board so that one term can be used later to refer to the user calories.
                    break
                else:
                    # Since the user has enabled suggestions, they are treated under the suggested health parameters. They must enter a number that is between 300-500.
                    print('It is advised you have a calorie deficit between 300 to 500 calories to see effective results. Please choose a valid calorie deficit.')
            except ValueError:
                print('Please enter a valid integer between 300 and 500 for the calorie surplus.')
if help == True:
    if choice == 2:
        print('You have chosen: I want to maintain body weight')
        print(f'Considering you want to maintain your weight of {weight}lbs, you should maintain your calories of {usercaloriebef}. The only difference in your calorie intake should be in the choice of foods, remmeber there must be a balance with attaining macronutrients and eating healthy.')
        usercal1111 = usercaloriebef
if help == True:
    if choice == 3:
        print('You have chosen: I would like to gain muscle mass')
        while True:
            try:
                calchoice = int(input(f'Considering your weight is {weight}lbs and you would like to gain muscle mass, you must now decide the calorie surplus you would like to be on. Please choose a number between 300 to 500 to add onto your current average calorie intake: '))
                if 300 <= calchoice <= 500:
                    print('Great choice.')
                    usercalgain = usercaloriebef + calchoice
                    usercal1111 = usercalgain
                    break
                else:
                    # Since the user has enabled suggestions, they are treated under the suggested health parameters. They must enter a number that is between 300-500.
                    print('It is advised you have a calorie surplus between 300 to 500 calories to see effective results. Please choose a valid calorie surplus.')
            except ValueError:
                print('Please enter a valid integer between 300 and 500 for the calorie surplus.')



#Help enabled section 3-------------------------------workout frequency

# Workout routine decision process for suggestions enabled.

if help == True:
    while True:
        try:
            work = int(input('Now it is time to decide how often you are going to workout. For the purposes of sticking to a reasonable regime, we are going to ask you to choose how often you intend on going to the gym a week. please enter between 2-6 as the amount of days you intend to go each week:'))
            if 2 <= work <= 6:
                print('Excellent choice')
                break
            elif work < 2:
                print('Perhaps we can attempt a bit more exercising.')
            elif 6 < work:
                print('That is a very high intensity. Since we are on suggestion mode, we suggest you choose a more reasonable and sustainable workout routine for yourself.')
            else:
                print('Please provide an appropriate response.')
        except ValueError:
            print('invalid input, please enter a number.')
            

#Help disabled section 1-------------------------------based inputs
        
# This is the path in which suggestions are disabled, which still has its uses. The user just now doesn't see many of the services. 
if help == False:
    while True:
        usercal1111 = input('Please input the number of calories you would like to consume per day:')
        try:
            usercal1111 = int(usercal1111)
            if 0 < usercal1111 < 10000:
            # My method for ensuring the user enters only an integer as their input was to only allow for the loop to break if the entered item is between 0 and 10000, otherwise their input is seen as invalid.
                print('Excellent choice.')
                usercal1111 = int(usercal1111)
                break
            else:
                print('Please enter a valid calorie choice.')
        except ValueError:
            print('Invalid input, please enter an integer.')
    
#Help disabled section 2-------------------------------workout frequency

# Workout routine decision process for suggestions disabled.
# The user has practically free reign over their decisions and are allowed to input pretty much whatever they want for their workout routine. Much like their choice of intended calorie goal.
if help == False:
    while True:
        try:
            work = input('Now it is time to decide how often you are going to workout. Please provide how many times do you intend to go each week:')
            work = int(work)
            if 0 <= work <= 9999:
                print('Excellent choice')
                break
            else:
                print('Please provide an appropriate response.')
                #I had to specify that the user could input "pretty much whatever they want". If the user inputed anything at the level of 9999 workouts in a week, it would be absurd.
        except ValueError:
            print('invalid input, please enter a number.')
            # For any such case that the user inputs anything other than a number, they are returned to the input.
            
print('----------------------------------------------------------------------------------------')
print('Now lets get started on YOUR fitness journey!')
# Now that the introduction is complete, and the user has enabled or disabled suggestions, they services of the program can commence.
print('----------------------------------------------------------------------------------------')

#graphing prelude-----------------------Tracker

# In the case of suggestions being enabled, the user is provided with a suggested protein and carb intake. The suggestions are based off of numerous credible online sources

if help == True:
    print("Daily Nutritional Intake:")
    print(f'          Suggested protein intake: {halfweight} g - {weight} g')
    print(f'          Suggested protein intake: {weight} g - {2 * weight} g')
    print('Calorie Intake input + visual display')

day = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}

#The averagecaloires function which yields the average amount of calories a user intakes relative to their inputs and personalized lists.
def averagecalories(y):
    average_calories = sum(y) / len(y)
    return average_calories
    

# Writing to the calorie file, a file that indexes the calories a user consumes in a week
with open('Usercalorieindex.txt', 'a') as file:
    for day, index in day.items():
        # This is done once per each of the days in a week. We get weekly averages but theoretically a single list could be used for long durations.
        while True:
            try:
                calories = int(input(f'Please input the calories you have consumed for {day}: '))
                if 0 <= calories <= 100000:
                    # User inputs can be as open as possible but are only actually indexed if they are integers. 
                    file.write(str(calories) + '\n')
                    # Write calories as a string and add a newline character
                    break  # Exit the loop if input is a valid integer within the specified range
                else:
                    print('Please enter a valid calorie choice between 0 and 10000.')
            except ValueError:
                print('Please enter an integer value.')
# Reading calorie file.
with open('Usercalorieindex.txt', 'r') as file:
    lines = file.readlines()[-7:]
    usercalories = [int(line.strip()) for line in lines]


# Writing to the workout file
while True:
    try:
        gym_frequency = int(input("How many times did you exercise this week? "))
        with open('GymFrequency.txt', 'w') as file:
            file.write(str(gym_frequency))  # We write the gym frequency to the file as a string
        break  
        # The loop is broken if the input is an integer. Since we used the "int" feature, the input is automatically read as an integer so anything that isn't an integer yields a value error.
    except ValueError:
        print('Please enter an integer value.')
        
# Reading file.
with open('GymFrequency.txt', 'r') as file:
    gym_data = file.read()
# Now we get into the graphing portion of the program
import matplotlib.pyplot as plt

#calorie graphs-----------------------
if help == True:
    print('Calorie Intake')
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [usercal1111] * len(x)  # Create a list of constant values
    q = x  # x-axis values for user inputted calories
    r = usercalories  # y-axis values for user inputted calories
    # Plotting the data
    plt.plot(q, r, label='User Inputted Calories')
    plt.plot(x, y, label='Suggested Calories')
    # Adding the title, labels, and legend
    plt.title("Suggested Calories vs Actual Calories")
    plt.ylabel("calories (Kcal)")
    plt.xlabel("Days")
    plt.legend()
    plt.show()
    print(f'Average number of calories for the week: {averagecalories(usercalories):.2f} Kcal')
    print(f'Previously decided daily calorie target:{usercal1111}')
    
if help == False:
    print('Calorie Intake')
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [usercal1111] * len(x)  # Create a list of constant values
    q = x
    r = usercalories
    plt.plot(x, y, label='Decided Calories')
    plt.plot(q, r, label='Actual Calories')
    # Adding the title, labels, and legend
    plt.title("Decided Calories vs Actual Calories")
    plt.ylabel("Calories (Kcal)")
    plt.xlabel("Days")
    plt.legend()
    plt.show()
    # Print out the average number of user inputted calories
    print(f'Average number of calories for the week: {averagecalories(usercalories):.2f} Kcal')
    print(f'Previously decided daily calorie target:{usercal1111}')
print('')

# workout frequency graph-------------------

print('workout routine')
print('')
if help == True:
    s = [1, 2]
    u = [work, gym_frequency]
    width = 1  
    plt.bar(s, u, width=width, align='center')
    plt.xticks(s, ['decided', 'actual'])
    for i, v in enumerate(u):
        plt.text(i + 1, v + 0.1, str(v), ha='center')
    plt.title("Decided vs Actual workout frequency (per week)")
    plt.ylabel("Times a week")
    plt.show()
    print(f'Previously decided weekly workout target:{work}')
    
    
    
#This is literally the same thing, but I set it for if help = false. I understand I could do without it but it fits in with the work philosophy of the prior sections[Help = True and Help = False dichotomy]
if help == False:
    s = [1, 2]
    u = [work, gym_frequency]
    width = 1  
    plt.bar(s, u, width=width, align='center')
    plt.xticks(s, ['decided', 'actual'])
    for i, v in enumerate(u):
        plt.text(i + 1, v + 0.1, str(v), ha='center')
    plt.title("Decided vs Actual workout frequency (per week)")
    plt.ylabel("Times a week")
    plt.show()
    print(f'Previously decided weekly workout target:{work}')

