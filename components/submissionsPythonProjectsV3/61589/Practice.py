import numpy as np
import matplotlib.pyplot as plt

Users = [[['Aryan', ' keskar'], [' LOTR', ' HP', ' Manushruti', ' Bhagvad Puran']], [['Vigneshwar', ' Ananth'], [' HP']]]
username = 'Aryan'
book = "seath"
for i in range(len(Users)):
        if(Users[i][0][0] == username):
            Users[i][1].append(book)

print(Users)


