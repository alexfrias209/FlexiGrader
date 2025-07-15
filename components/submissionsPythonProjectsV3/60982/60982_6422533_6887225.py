import math
print('This is a calorie calculator to see what your daily caloric intake should be and what it should be to change your weight!')
print("Let's start off by asking a series of questions about yourself to see what your daily caloric intake should be.")
#Branch if user has chosen male sex
while True:
    user_sex = input('What is your sex? (Male/Female):')
    
    if user_sex == 'Male' or user_sex == 'male' or user_sex == 'MALE':
        
        weight = input('What is your weight in pounds?')
        weight = float(weight)
        if weight <= 0:
            print("Please enter a valid weight.")
            weight = input('What is your weight in pounds?')
            weight = float(weight)
        
        age = input('What is your age in years?')
        age = float(age)
        if age <= 0:
            print("Please enter a valid age.")
            age = input('What is your age in years?')
            age = float(age)
        
        height = input('What is your height in inches?')
        height = float(height)
        if height <= 0:
            print("Please enter a valid height.")
            height = input('What is your height in inches?')
            height = float(height)
#All of the input variables will be used in this equation
        def CalcBMR(weight, height, age):
            return (4.53592 * weight) + (15.875 * height) - (5 * age) + 5
        BMR = CalcBMR(weight, height, age)
        BMR = float(BMR)
#This is where the Basal Metabolic Rate is finally output
        while True:
            Activity_level = input('How active would you say you are? Rate your weekly activity level on a scale of 1-5 where 1 is barely active, 2 is lightly active, 3 is moderately active, 4 is active, and 5 is very active.')
            
            if Activity_level == '1':
                BMR = BMR * 1.2
                BMR = float(BMR)
                BMR = round(BMR, 0)
                print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                break
            if Activity_level == '2':
                BMR = BMR * 1.375
                BMR = float(BMR)
                BMR = round(BMR, 0)
                print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                break
            if Activity_level == '3':
                BMR = BMR * 1.55
                BMR = float(BMR)
                BMR = round(BMR, 0)
                print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                break
            if Activity_level == '4':
                BMR = BMR * 1.725
                BMR = float(BMR)
                BMR = round(BMR, 0)
                print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                break
            if Activity_level == '5':
                BMR = BMR * 1.9
                BMR = float(BMR)
                BMR = round(BMR, 0)
                print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                break
            while Activity_level not in ['1', '2', '3', '4', '5']:
                print("Please choose a number from 1 to 5 to represent your activity level.")
                Activity_level = input('How active would you say you are? Rate your weekly activity level on a scale of 1-5 where 1 is barely active, 2 is lightly active, 3 is moderately active, 4 is active, and 5 is very active.')
                if Activity_level == '1':
                    BMR = BMR * 1.2
                    BMR = float(BMR)
                    BMR = round(BMR, 0)
                    print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                    break
                if Activity_level == '2':
                    BMR = BMR * 1.375
                    BMR = float(BMR)
                    BMR = round(BMR, 0)
                    print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                    break
                if Activity_level == '3':
                    BMR = BMR * 1.55
                    BMR = float(BMR)
                    BMR = round(BMR, 0)
                    print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                    break
                if Activity_level == '4':
                    BMR = BMR * 1.725
                    BMR = float(BMR)
                    BMR = round(BMR, 0)
                    print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                    break
                if Activity_level == '5':
                    BMR = BMR * 1.9
                    BMR = float(BMR)
                    BMR = round(BMR, 0)
                    print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                    break
                break
            break
        break
#Branch if user has chosen female sex
    if user_sex == 'Female' or user_sex == 'female' or user_sex == 'FEMALE':
        
        weight = input('What is your weight in pounds?')
        weight = float(weight)
        if weight <= 0:
            print("Please enter a valid weight.")
            weight = input('What is your weight in pounds?')
            weight = float(weight)
        
        age = input('What is your age in years?')
        age = float(age)
        if age <= 0:
            print("Please enter a valid age.")
            age = input('What is your age in years?')
            age = float(age)
        
        height = input('What is your height in inches?')
        height = float(height)
        if height <= 0:
            print("Please enter a valid height.")
            height = input('What is your height in inches?')
            height = float(height)
        
#All of the input variables will be used in this equation
        def CalcBMR(weight, height, age):
            return (4.53592 * weight) + (15.875 * height) - (5 * age) + 5
        BMR = CalcBMR(weight, height, age)
        BMR = float(BMR)
#This is where the Basal Metabolic Rate is finally output
        while True:
            Activity_level = input('How active would you say you are? Rate your weekly activity level on a scale of 1-5 where 1 is barely active, 2 is lightly active, 3 is moderately active, 4 is active, and 5 is very active.')
            if Activity_level == '1':
                BMR = BMR * 1.2
                BMR = float(BMR)
                BMR = round(BMR, 1)
                print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                break
            if Activity_level == '2':
                BMR = BMR * 1.375
                BMR = float(BMR)
                BMR = round(BMR, 1)
                print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                break
            if Activity_level == '3':
                BMR = BMR * 1.55
                BMR = float(BMR)
                BMR = round(BMR, 1)
                print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                break
            if Activity_level == '4':
                BMR = BMR * 1.725
                BMR = float(BMR)
                BMR = round(BMR, 1)
                print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                break
            if Activity_level == '5':
                BMR = BMR * 1.9
                BMR = float(BMR)
                BMR = round(BMR, 1)
                print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                break
            while Activity_level not in ['1', '2', '3', '4', '5']:
                print("Please choose a number from 1 to 5 to represent your activity level.")
                Activity_level = input('How active would you say you are? Rate your weekly activity level on a scale of 1-5 where 1 is barely active, 2 is lightly active, 3 is moderately active, 4 is active, and 5 is very active.')
                if Activity_level == '1':
                    BMR = BMR * 1.2
                    BMR = float(BMR)
                    BMR = round(BMR, 0)
                    print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                    break
                if Activity_level == '2':
                    BMR = BMR * 1.375
                    BMR = float(BMR)
                    BMR = round(BMR, 0)
                    print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                    break
                if Activity_level == '3':
                    BMR = BMR * 1.55
                    BMR = float(BMR)
                    BMR = round(BMR, 0)
                    print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                    break
                if Activity_level == '4':
                    BMR = BMR * 1.725
                    BMR = float(BMR)
                    BMR = round(BMR, 0)
                    print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                    break
                if Activity_level == '5':
                    BMR = BMR * 1.9
                    BMR = float(BMR)
                    BMR = round(BMR, 0)
                    print ('The amount of calories you have to consume daily to maintain your weight is', BMR,'calories!')
                    break
                break
            break
        break

    else:
        print('Please state what your sex is.')

print("Now that we've determined how many calories you have to consume each day to maitain your weight, let's now see what it would take to change your weight.")       
#Weight change section
while True:
    user_weight_goal = input("Would you like to lose, gain, or maintain weight?: (Gain/Lose/Maintain)")
#Branch if user wants to lose weight
    if user_weight_goal == 'Lose' or user_weight_goal == 'lose' or user_weight_goal == 'LOSE':
        weightlossgoal = input('What is your desired weight in pounds?')
        weightlossgoal = float(weightlossgoal)
        lossinpounds = weight - weightlossgoal
        lossinpounds = float(lossinpounds)
        
        timechange = input('Over how many months would you like you weight change to happen?')
        timechange = float(timechange)
        if timechange <= 0:
            print("Please enter a valid amount of time.")
            timechange = input('Over how many months would you like you weight change to happen?')
        lossinpounds = weight - weightlossgoal
        
        loss_daily_calorie_intake = (BMR - ((lossinpounds * 3500) / (timechange * 30)))
        
        print(f"In order to get to {weightlossgoal} pounds over {timechange} months, you should eat {loss_daily_calorie_intake:.2f} calories per day.")
        print("Thank you for trying out the calorie calculator!")
        break
#Branch if user wants to gain weight
    if user_weight_goal == 'Gain' or user_weight_goal == 'gain' or user_weight_goal == 'GAIN':
        weightgaingoal = input('What is your desired weight in pounds?')
        weightgaingoal = float(weightgaingoal)
        gaininpounds = weightgaingoal - weight
        gaininpounds = float(gaininpounds)
        
        timechange = input('Over how many months would you like you weight change to happen?')
        timechange = float(timechange)
        
        gain_daily_calorie_intake = (BMR + ((gaininpounds * 3500) / (timechange * 30)))
        
        print(f"In order to get to {weightgaingoal} pounds over {timechange} months, you should eat {gain_daily_calorie_intake:.2f} calories per day.")
        print("Thank you for trying out the calorie calculator!")
        break
#Branch if user wants to maintain weight
    if user_weight_goal == 'maintain' or user_weight_goal == 'Maintain' or user_weight_goal == 'MAINTAIN':
        print('Continue to consume', BMR, 'calories daily and you will maintain your current weight.')
        print("Thank you for trying out the calorie calculator!")
        break