# create a file to later be appended with matches that are discovered
f = open('my.file.txt', 'a')
#  a list with both types of questions [main question, sub question]
questions = [
    ('First Question: When do you prefer to sleep? ', 'What time do you generally sleep at?'),
    ('Second Question: Where do you prefer to study', 'Between what times might you like to study in your dorm?'),
    ('Third Question: Are you okay with guests over night?', 'If yes, what type of guest?'),
    ('Fourth Question: How clean is your room expected to be?', 'How is cleaning expected to be done in your dorm?'),
    ('Fifth Question: What are your hobbies?', 'When do you usually take part in this hobby?')
]
# a list of answers in respect to its [main question, sub question] as [choice, sub choice]
question_choices = [
    (['1. Sleep Early', '2. Sleep Late'], ['1. 7:00pm - 9:00pm', '2. 10:00pm - 12:00am', '3. Later than 12:00am']),
    (['1. In my dorm', '2. Outside of my dorm'], ['1. During daylight hours', '2. In the Evening/Night']),
    (['1. Yes', '2. No'], ['1. Yes, anyone', '2. Yes, same sex', '3. NA(if your previous answer was No)']),
    (['1. Very Clean', '2. Messy', '3. In Between'],
     ['1. In weekly rotation', '2. Person(s) dedicated to a specific task', '3. As needed']),
    (['1. Video Games', '2. Sports', '3. Gym', '4. Sleeping'], ['1. During the day', '2. Mid-day', '3. Night'])
]

# Introduction to code
print("Hello, and Welcome to Housing Roommate Matcher")
print('Developed')
print('Here you will create a housing profile based on your preferences and test if you\'re match with another user\n')
# enter a number of users to simulate how many possible roommates are within the loop
num_users = int(input("Enter the number of users(to consider how many profiles will be crossed to find a match): "))
# profile_data will be used to store individual peoples responses to questions
profile_data = []

# The program begins by asking the user for their name to later be stored as its own user_profile to match against
for user_num in range(1, num_users + 1):
    user_profile = {}
    name = input('Please enter your name to begin : ')
    user_profile['Name'] = name
    print(f"\n{name}\'s Profile:")
    # Identifies questions, sub questions, choices, and sub choices given within previous lists
    for q_n_sq in range(len(questions)):
        question, sub_question = questions[q_n_sq]
        choices, sub_choices = question_choices[q_n_sq]
        print(question)
        # For every question its respective choice list will be printed
        for choice in choices:
            print(choice)
            # For every given [Question, choice] the program will execute the first 'while' loop demonstrating the
            # storing of a users choices to later be cross-referenced with other profiles to identify matches
        while True:
            user_choice = input('Please enter the respective number of your choice')
            print()
            # This 'if/else' statement determines whether a users choice to a question is an integer and valid
            # in order for the code to execute a followup of a sub question
            if user_choice.isdigit() and 1 <= int(user_choice) <= len(choices):
                user_profile[questions[q_n_sq][0]] = choices[int(user_choice) - 1]
                break
            else:
                print("Invalid input. Please enter a valid choice.")

        # For every sub question its respective sub choice list will be printed
        print(sub_question)
        for sub_choice in sub_choices:
            print(sub_choice)

        # For every given [sub_question, sub_choice] the program will execute the second 'while' loop
        while True:
            user_choice = input('Please enter the respective number of your choice')
            print()
            # This 'if/else' statement determines whether a users choice to a sub question is an integer and valid
            # dependent on the number of choices in order for the program to execute the next [Question, Choice] section
            if user_choice.isdigit() and 1 <= int(user_choice) <= len(sub_choices):
                user_profile[questions[q_n_sq][1]] = sub_choices[int(user_choice) - 1]
                break
            else:
                print("Invalid input. Please enter a valid choice.")
    # Now that the series of [Questions, Sub_questions] have been answered, we store the users data with its respective
    # profile and then add that profile and its answers to profile_data to later be cross-referenced for a match with
    # other users [choices, sub choices]
    profile_data.append(user_profile)

# With data collected from users profiles we cross-match them in order to determine similarities
potential_roommate = []

for x, profile1 in enumerate(profile_data):
    for y in range(x + 1, len(profile_data)):
        profile2 = profile_data[y]

        # Check if the profiles match by comparing their choices
        matched_responses = 0  # Counter for matching responses

        for items in range(len(questions)):
            question = questions[items][0]
            sub_question = questions[items][1]

            # Check if choices for the main question and sub-question match
            if profile1[question] == profile2[question] and profile1[sub_question] == profile2[sub_question]:
                matched_responses = matched_responses + 1

        # Check if at least half of the users responses to [questions, sub_questions] to another users profile
        if matched_responses >= len(questions) / 2:
            potential_roommate.append((x, y))

# Print potential roommate matches
if potential_roommate:
    print("\nPotential Roommate Matches:")
    for i, j in potential_roommate:
        user1 = profile_data[i]['Name']
        user2 = profile_data[j]['Name']
        print(f"{user1} and {user2} are considerable roommates for each other.")
        f.write(f"{user1} and {user2} are considerable roommates for each other.")
# in the instance that a user does not meet at least half matched responses as previous users
# then it will be considered that they have no potential people to be roommate matched with
else:
    print("\nYou have no potential roommate matches :(.")

for line in f:
    print(line)
    
f.close()
