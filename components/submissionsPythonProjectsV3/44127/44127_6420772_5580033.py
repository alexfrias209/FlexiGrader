import random  # loads the random module which gets a random variable from a function
import webbrowser  # makes the web browser applicable, so it won't come out as undefined

user_name = input("Please enter your name: ")
print(f"Welcome to the US Capital python quiz {user_name}.")

print("I hope you've been studying the US capitals."
      "\nThis quiz will give you 10 random states and you have to guess their Capitals correctly."
      f"\nAt the end you will be given a score to see how you did. \nBest of luck {user_name}!")

us_capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
               'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
               'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
               'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
               'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
               'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
               'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
               'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
               'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
               'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
               'South Carolina': 'Columbia',
               'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
               'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
               'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

link = "https://www.lovetoknow.com/parenting/kids/50-states-capitals-alphabetical-order"
webbrowser.open(link)  # This will open the link provided above to use as answers

random_Capital = random.sample(list(us_capitals.keys()), 10)  # This is where the import random gets used
# If import random was not at the top we get 'random' is not defined
# 10 is the amount of random samples we get from our dictionary
score = 0  # Score starts at 0 and +1 everytime the user gets the answer right

# For the Capital in random_capital which is just a random sample of my dict
# Since random_Capital has .keys() this means it pulls the first part which is the state
# The first part is the value which is the state.
for Capital in random_Capital:
    capital = us_capitals[Capital]
    tries = 0  # Starts your amount of tries at 0, it then goes up by one until you reach 3 tries
    while tries < 3:
        user_answer = input(f'What is the capital of {Capital}? ').strip()  # Strip disregards multiple spaces
        if user_answer == capital:  # This is the part where the users answer has to be the same as the key
            score += 1  # +1 to score when correct
            print("Correct!")
            break
        else:
            print("Wrong please try again.")
            tries += 1  # +1 tries when wrong
        if tries == 3:  # Once the tries reaches three it goes on to the next question
            print("Sorry, you're out of tries")
# Your score is then shown and based on your score you get one of the following feedbacks
if score == 0:
    print("\nWow I don't know how you got 0, but you did. Hopefully, you were just playing around.")
if 1 <= score <= 6:
    print(f'\nYou might need to study the US Capitals more {user_name}. Your score is: {score}')
if score == 7:
    print(f"\nYou passed {user_name}, but a little review won't hurt. Your score is: {score}")
if score == 8:
    print(f'\nGood job on the quiz, {user_name}! Your score is: {score}')
if score == 9:
    print(f'\nAmazing job on the quiz {user_name}, you definitely know the Capitals! Your score is {score}')
if score == 10:
    print(f'\nBeautifully done {user_name}, you deserve a cookie! Your score is: {score}')
