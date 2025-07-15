import csv
from PIL import Image
import requests
from io import BytesIO
import random

# The program is a country flag quiz. It will display a flag to which the user will have to answer which country it represents.
# Image links within countries.csv are scanned by the program and then displayed to the user.

countries = []
scores = []

# Opens both csv files and writes them into a list. Program reads from the lists based on the csv files.
   ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
   ##  !! THE PROGRAM SEARCHES FOR THE CSV FILES IN THE DIRECTORY THE CONSOLE IS SET TO !!   ##
   ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
with open("59681_6420319_5185272.csv", 'r', encoding='cp1252') as csvfile:
    sr = csv.reader(csvfile)
    for row in sr:
        ', '.join(row)
        countries.append(row)
with open("59681_6420318_3900007.csv", 'r', encoding='cp1252') as csvfile2:
    sw = csv.reader(csvfile2)
    for row in sw:
        ', '.join(row)
        scores.append(row)

# Defining image displaying
def display_img(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.show()

# Prompt that asks to begin the quiz
while True:
        print('\nWelcome to the country quiz. \nDeveloped by Kurt Qin. \nThe previous scores were (for correct answers):', scores)
        yell = input('\nType \'Begin\' to begin: ')
        if yell == 'Begin':
            break
        else:
            print('')

# Program loop that will ask questions and prompt to retry after all questions have been asked. 
# Result delivered at the end. Result is saved into the csv file containing the scores, which can then be read again later.
while True:
    correct = []
    incorrect = []
    excludedints = []

    # Q1
    rndm1 = random.randint(0, len(countries))
    display_img(countries[rndm1 - 1][1])
    answer1 = input('\nFirst question; What country does this flag represent? ')
    if answer1 == countries[rndm1 - 1][0]:
        print('That is *correct*! \n')
        correct.append(1)
        excludedints.append(rndm1)
    else:
        print('That is *incorrect*! \n')
        incorrect.append(1)
        excludedints.append(rndm1)

    # Q2
    while True:
        rndm2 = random.randint(0, len(countries))
        if rndm2 not in excludedints:
            break
    display_img(countries[rndm2 - 1][1])
    answer2 = input('Second question; What country does this flag represent? ')
    if answer2 == countries[rndm2 - 1][0]:
        print('That is *correct*! \n')
        correct.append(2)
        excludedints.append(rndm2)
    else:
        print('That is *incorrect*! \n')
        incorrect.append(2)
        excludedints.append(rndm2)

    # Q3
    while True:
        rndm3 = random.randint(0, len(countries))
        if rndm3 not in excludedints:
            break
    display_img(countries[rndm3 - 1][1])
    answer3 = input('Third question; What country does this flag represent? ')
    if answer3 == countries[rndm3 - 1][0]:
        print('That is *correct*! \n')
        correct.append(3)
        excludedints.append(rndm3)
    else:
        print('That is *incorrect*! \n')
        incorrect.append(3)
        excludedints.append(rndm3)

    # Q4
    while True:
        rndm4 = random.randint(0, len(countries))
        if rndm4 not in excludedints:
            break
    display_img(countries[rndm4 - 1][1])
    answer4 = input('Fourth question; What country does this flag represent? ')
    if answer4 == countries[rndm4 - 1][0]:
        print('That is *correct*! \n')
        correct.append(4)
        excludedints.append(rndm4)
    else:
        print('That is *incorrect*! \n')
        incorrect.append(4)
        excludedints.append(rndm4)

    # Q5
    while True:
        rndm5 = random.randint(0, len(countries))
        if rndm5 not in excludedints:
            break
    display_img(countries[rndm5 - 1][1])
    answer5 = input('Final question; What country does this flag represent? ')
    if answer5 == countries[rndm5 - 1][0]:
        print('That is *correct*! \n')
        correct.append(5)
    else:
        print('That is *incorrect*! \n')
        incorrect.append(5)
    
    # Results
    print('You have completed all the questions. Your total score is:', len(correct), 'right;', len(incorrect), 'wrong.')
    if len(correct) >= 5:
        print('You\'ve got a spotless score! \n')
    elif 0 < len(correct) <= 4:
        print('You could do better. \n')
    else:
        print('You\'ve totally failed this quiz! \n')

    # Score Save
    if len(correct) > 0:
        scores.append(str(len(correct)))
    with open(r"Score.csv", 'w', newline='', encoding='cp1252') as csvfile2:
        writer = csv.writer(csvfile2)
        writer.writerows(scores)

    # Continue
    cont = input('Try again? (yes/no): ')
    if cont == 'no':
        break
    else:
        correct.clear()
        incorrect.clear()
        excludedints.clear()
