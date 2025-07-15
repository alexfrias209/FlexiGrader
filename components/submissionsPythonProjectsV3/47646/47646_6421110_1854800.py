import random
import csv

import pandas
import requests
from PIL import Image
from io import BytesIO

#introduction where user gets to know what it's about and are able to input their name
name = input('Please enter your name: ')
print(f'\nWelcome {name}!\nIn this program you will learn about 10 common edible fungi in North America.\n')
m_options = "1. Oyster\n2. Chanterelle\n3. Morel\n4. Shaggy Inkcap\n5. Black Trumpet\n6. Chicken of the woods\n7. Lion's mane\n8. Hen of the woods\n9. King Bolete\n10. Puffball\n"

#opening/reading the csv file by putting it into a dictionary so it's iterated and has keys
file = open('mushrooms_info.csv', 'r')
opened = csv.reader(file)

m_dict = {}
for row in opened:
        m_dict[row[0]] = {'Common name': row[1], 'Latin name': row[2], 'Image url': row[3]}
  

#created a general definition function for retrieving images that could be applied to any mushroom picture by using requests module since the image link is in csv file
#sometimes links would stop working for no reason, so I created an error print in case it doesn't work
def m_inf(in1):
    if in1 in m_dict:
        print(f'You have selected mushroom #{in1}. One of the common names for this mushroom is', m_dict[in1]['Common name'], 'mushroom. It has the Latin name of',m_dict[in1]['Latin name'],'.')
        
        mushroom = m_dict[in1]
        img_url = mushroom['Image url']
        r = requests.get(img_url)

        if r.status_code == 200:
            img_raw = BytesIO(r.content)
            img = Image.open(img_raw)
            img.show()

        else:
            print('Error loading picture... Please choose again.')
            print()


#created a definition function for the quiz
#used random module to randomly generate one of the ten mushroom pictures for the user to check their visual identification knowledge on the mushroom
def m_quiz():
    while True:
        m_random = random.choice(list(m_dict.keys()))
        mushroom = m_dict[m_random]
        img_url = mushroom['Image url']
        r = requests.get(img_url)
       

        if r.status_code == 200:
            img_raw = BytesIO(r.content)
            img = Image.open(img_raw)
            img.show()

            print()
            in2 = input('Guess the mushroom in the picture by entering its associated number:')
            print()

            return in2, m_random
        else:
            break


score = 0
guesses = 0

#user inputs a number 1-10 to learn about the mushroom assigned to the number and eventually enters q after they feel commfortable with what they have learned
#user can go back to learning menu if they feel they do not know the mushroom enough
while True:
    
    print(m_options)
    print()
    in1 = input('Please enter a mushroom number to learn about or continue to the mushroom identification quiz by entering Q.\n')
    print()

    if '1' == in1:
        m_inf(in1)
    elif '2' == in1:
        m_inf(in1)
    elif '3' == in1:
        m_inf(in1)
    elif '4' == in1:
        m_inf(in1)
    elif '5' == in1:
        m_inf(in1)
    elif '6' == in1:
        m_inf(in1)
    elif '7' == in1:
        m_inf(in1)
    elif '8' == in1:
        m_inf(in1)
    elif '9' == in1:
        m_inf(in1)
    elif '10' == in1:
        m_inf(in1)
    elif in1 == 'q' or in1 == 'Q':

        print('The quiz will now start.')
        print()

        #random module used for generating a random picture in which user will guess the mushroom associated with it
        #it will keep a score on how many they guess correctly and how many total attempts they have made
        while True:
            in2, m_random = m_quiz()
            if in2 == m_random:

                score +=1
                guesses += 1

                print()
                print(f'You have guessed correctly! Your current score is {score} out of {guesses} guesses. Enter q to return to the msuhroom information list.')
                print()

            elif in2 == 'q' or in2 == 'Q':

                print()
                print('You are exiting the quiz.')
                print()
                break
            else:

                guesses += 1

                print()
                print(f'You have guessed incorrectly. Your current score is {score} out of {guesses}. Enter q to return to the msuhroom information list.')
                print()
    else:
        print('Please select a mushroom by its number or start the quiz.')