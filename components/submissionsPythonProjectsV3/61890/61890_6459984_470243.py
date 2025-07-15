# Defining age categories
age_categories = {
    'kids': range(5, 14),
    'teenagers': range(14, 18),
    'adolescent': range(18, 23),
    'adults': range(23, 64),
    'seniors': range(64, 120),
}
# Before I was defining each one with age which took up a lot more space and was less efficient

# Step 2: Get user information
name = input("Enter your name: ")
while True: 
    try: 
        gender = input("Are you male or female? (Type 'male' or 'female'): ").lower()
        if gender in ['male', 'female']:
            break 
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")
# searches for age and category based off input
while True:
    try:
        age_input = int(input("How old are you? "))

        for category, age_range in age_categories.items():
            if age_input in age_range:
                age_category = category
                break
        else:
            print("Invalid age input. ")
            continue  # Continue the loop if age is invalid
        break  # Break out of the loop if a valid age is provided
    except ValueError:
        print("Invalid age input. Please enter a number.")

print(f"You belong to the '{age_category}' category.")


# Step 5: Check if the user eats healthy food
healthy = input("Do you eat healthy food? (Type 'yes' or 'no'): ").lower()

if healthy not in ('yes', 'no'):
    print("Invalid input. Please enter 'yes' or 'no'.")
else:
    if healthy == 'no':
        if gender == 'male' and age_category == 'kids':
            print("You're very unhealthy at such a young age, come on you can do better!")
        elif gender == 'female' and age_category == 'kids':
            print("You're very unhealthy at such a young age, come on you can do better!")
        elif gender == 'male' and age_category == 'young_adults':
            print("You're very unhealthy and you're youngadult so work on improving yourself!")
        elif gender == 'female' and age_category == 'young_adults':
            print("You're very unhealthy and you're youngadult so work on improving yourself!")
        elif gender == 'male' and age_category == 'adults':
            print("You're very unhealthy and you're a grown man, you should know better!")
        elif gender == 'female' and age_category == 'young_adults':
            print("You're very unhealthy and you're a grown woman, you should know better!")
        elif gender == 'male' and age_category == 'seniors':
            print("You're very unhealthy and this could lead to worse things!")
        elif gender == 'male' and age_category == 'teenagers':
            print("You're very unhealthy at such a young age, come on you can do better!")
        elif gender == 'female' and age_category == 'teenagers':
            print("You're very unhealthy at such a young age, come on you can do better!")
        elif gender == 'female' and age_category == 'seniors':
            print("You're very unhealthy and this could lead to worse things!")
        elif gender == 'female':
            print("You may not be very healthy. Stay healthy!")
    else:
        if gender == 'male' and age_category == 'teenagers':
            print("Great job! Teenagers usually need to be careful about their health.")
        elif gender == 'female' and age_category == 'teenagers':
            print("Great job! Teenagers usually need to be careful about their health.")
        elif gender == 'male' and age_category == 'seniors':
            print("Great job! keep this up to live a long and healthy life")
        elif gender == 'female' and age_category == 'seniors':
            print("Great job! keep this up to live a long and healthy life")
        elif gender == 'male' and age_category == 'young_adults':
            print("Great job! keep this up to live a long and healthy life")
        elif gender == 'female' and age_category == 'young_adults':
            print("Great job! keep this up to live a long and healthy life")
        elif gender == 'male' and age_category == 'adults':
            print("Great job! keep this up to live a long and healthy life")
        elif gender == 'female' and age_category == 'adults':
            print("Great job! keep this up to live a long and healthy life")
        elif gender == 'male' and age_category == 'kids':
            print("Great job! you're a very healthy child and keep this up to live a great life!")
        elif gender == 'female' and age_category == 'kids':
            print("Great job! you're a very healthy child and keep this up to live a great life!")


# Step 6: Collect gender and weight information to make it into list
genders = ['male', 'female']
# then making it into a dictionary 
weights = {
    'male': {
        'height': [],
        'weight': [],
    },
    'female': {
        'height': [],
        'weight': [],
    },
}

if gender in genders:
    height = float(input("Enter your height (in cm): "))
    weight = float(input("Enter your weight (in kg): "))

    # Store height and weight information
    weights[gender]['height'].append(height)
    weights[gender]['weight'].append(weight)
    # add to end of list
def calculate_bmi(height, weight):
    # Will calculate height in meters
    height_meters = height / 100
    
    # Calculate BMI
    bmi = weight / (height_meters ** 2)
    
    return bmi

# Height in cm and weight in kg

bmi = calculate_bmi(height, weight)
underweight = False
perfect = False
overweight = False
obese = False

if bmi <= 18.5:
    print("You're UNDERWEIGHT!")
    underweight = True
elif 18.5 < bmi <= 24.9:
    print("You're PERFECT in weight!")
    perfect = True
elif 24.9 < bmi <= 29.9:
    print("You're OVERWEIGHT!")
    overweight = True
elif 29.9 < bmi <= 34.9:
    print("You're OBESE!")
    obese = True
elif bmi >= 34.9:
    print("You're in the worse condition you can be in right now!")
    worsethanobese = True
else:
    print("You're EXTREMELY EXTREMELY OBESE!")

print(f"Your BMI is: {bmi:.2f}")
# This will define age categories for information extraction
age_categories_for_extraction = ['kids', 'teenagers', 'adolescent', 'adults', 'seniors']

# Open the text file for reading
file_path = "61890_6459985_8408802.txt"

# Check if the user's age category is one for which information should be extracted
if age_category in age_categories_for_extraction:
    with open(file_path, 'r') as file:
        # Iterate through the lines of the file
        for line in file:
            # Check if the line contains the user's age category
            if age_category in line:
                # Print the entire line
                print(line.strip())  # Use strip() to remove leading/trailing whitespace
if underweight:
    if healthy == 'no':
        print(f"At a BMI of {bmi:.2f} {name}, you weigh {weight} at {height}. You're considered underweight and very unhealthy for a {gender}.")
    elif healthy == 'yes':
        print(f"At a BMI of {bmi:.2f} {name}, you weigh {weight} at {height}. You're considered underweight for a {gender}.")
elif perfect:
    if healthy == 'no':
        print(f"At a BMI of {bmi:.2f} {name}, you weigh {weight} at {height}. You're considered a perfect weight but unhealthy due to your eating habits for a {gender}.")
    elif healthy == 'yes':
        print(f"At a BMI of {bmi:.2f} {name}, you weigh {weight} at {height}. You're considered a perfect weight and very healthy for a {gender}.")
elif overweight: #Check this error
    if healthy == 'no':
        print(f"At a BMI of {bmi:.2f} {name}, you weigh {weight} at {height}. You're considered very unhealthy due to your height and weight ratio and your unhealthy food options for a {gender}.")
    elif healthy == 'yes':
        print(f"At a BMI of {bmi:.2f} {name}, you weigh {weight} at {height}. You're considered unhealthy due to your height and weight ratio for a {gender}.")
elif obese:
    if healthy == 'no':
        print(f"At a BMI of {bmi:.2f} {name}, you weigh {weight} at {height}. You're considered very unhealthy due to your height and weight ratio and your unhealthy food options and since you're obese your body wont function at its fullest for a {gender}.")
    elif healthy == 'yes':
        print(f"At a BMI of {bmi:.2f} {name}, you weigh {weight} at {height}. You're considered very unhealthy due to your height and weight ratio and obesity doesn't help too for a {gender}.")
elif worsethanobese:
    if healthy == 'no':
        print(f"At a BMI of {bmi:.2f} {name}, you weigh {weight} at {height}. You're considered very unhealthy due to your height and weight ratio and your unhealthy food options and since you're extremely obese your killing yourself even more for a {gender}.")
    elif healthy == 'yes':
        print(f"At a BMI of {bmi:.2f} {name}, you weigh {weight} at {height}. You're considered very unhealthy due to your height and weight ratio and since your super obese you're going to have more health problems for a {gender}.")