import csv
import pandas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

animals = {}
sports = {}
foods = {}
score ={}
count = 0

with open('61704_6415759_7099829.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["username", "score"]
    writer.writerow(field)

"""
xpoints = np.array([0, 10])
ypoints = np.array([0, 4])

plt.plot(xpoints,ypoints)
plt.show()
"""


def read_scoreboard():
    with open ("61704_6415759_7099829.csv","r") as file:
        csvreader = csv.reader(file,delimiter = ',')
        for row in csvreader:
            print(row)
def scoreboard(username,count):
    with open("61704_6415759_7099829.csv","a") as file:
        blah = [username , count]
        writer = csv.writer(file)
        writer.writerow(blah)
def create_plot(csv_name):
    data = pd.read_csv(csv_name)

    df = pd.DataFrame(data)

    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    plt.bar(X, Y, color='g')
    plt.title("Scores")
    plt.xlabel("Names")
    plt.ylabel("Score")

    plt.show() 

read_scoreboard()
quizzes = ['animals','sports','foods']


f = open("61704_6415757_1001815.txt", 'r', encoding = 'utf-8-sig')
data = f.read()
lines = data.splitlines()
for line in lines:
    parts = line.split(", ")
    if parts[0] == "animals":
        animals[parts[1]] = parts[2]
    elif parts[0] == "sports":
        sports[parts[1]] = parts[2]
    elif parts[0] == "foods":
        foods[parts[1]] = parts[2]

play = input("Do you want to play? (Y/N) ")
while(play == 'Y'):
    count = 0
    username = input("what is your username: ")
    quizzes = [animals, sports, foods]
    choice = int(input(f'Which quiz do you want to do? Choose "1 for animals", "2. for sports", or "3 for foods": '))
    if choice == 1:
        x=quizzes[0]
    elif choice == 2:
        x=quizzes[1]
    else:
        x=quizzes[2]

    for key,value in x.items():
        user = input(f'{key}:')
        if user==value:
            print(f'Correct user chose {user}')
            count += 1
        else:
            print(f'Incorrect, answer is {value}')
            
    scoreboard(username,count)
    play = input("Do you want to play again? (Y/N) ")

create_plot('61704_6415759_7099829.csv')

