print('Welcome to my project! My name is XXX XXXXX and I am the developer. \nThis project is intended to recommend video games to you based on your input of interests.')

# Xbox is the key, Xbox_One is the item in the Xbox
console_dict = {'Xbox':['Xbox_One'],
                 'Nintendo':['Nintendo_Switch'], 
                 'Playstation':['Playstation_4', 'Playstation_5'], 
                 'PC':['PC'], 
                 'Mobile':['iOS', 'Android']}

print('Here is a list of video game consoles to choose from: ', console_dict)
user_console = input('From the above list, which console do you prefer to play on? ')

# asking the user which console they want to play on
for value in console_dict.values():
    if user_console == value:
        print('That is not a valid console! ')
    else:
        print('You have selected: ', user_console)
        print(console_dict[user_console])
        print('Please select which', user_console, 'generation you like to play on')
        console_gen = input()
        print('You have selected:', console_gen)
        break


# dictionary of available genres within the file
genre_dict = {'Adventure', 'Role-Play Game', 'Action', 
              'Survival', 'Strategy', 'Shooter'}

print('Here is a list of game genres: \n', genre_dict)
user_genre = input('From the above list, what genre of game do you prefer to play? Please choose one: ')

# asking user to input the genre in which they want games of
for g in genre_dict:
    if user_genre == g:
        print('That genre is not valid! ')
    else:
        print('You have selected: ', user_genre)
        break
    
# asking user to input the number of players they want the game to be compatible with
user_player = input('Enter a non-decimal integer for the number of players you prefer to play with. If solo player, please type 0, \n if more than 3, please type "Multi-Player": ')
user_dict = {'1,', '2', '3', 'Multi-Player'}

for p in user_dict:
    if user_player == p:
        print('Not a valid number of players! ')
    else:
        print('You have selected', user_player, 'player(s)')
        break

# opening videogames.txt file
file = open("60570_6420600_1782737.txt", "r")
# reads lines in the file
f = file.readlines()

# holds each item that is iterated over the file. 
string_1 = ""
#string 1 holds the first line in the file, the title line
string_2 = ""
#string 2 holds every line after the title line such as the actual data in the file

#counter reads first line in file
counter = 1

# while loop counter checks each line one by one throughout the whole file 
while (counter != len(f)):
    # f[counter] skips over the first line of the file because it's a category line, not relevant to the ouput
    string_1 = f[counter]
    # splitting each line in the file to it's own separate list to iterate over later
    string_2 = string_1.split()

    # taking each element in the list and separating each item containing a "/"
    string_2[3] = string_2[3].split("/")
    string_2[1] = string_2[1].split("/")
    #string_2[2] = string_2[2].split("_")
    
    #checks to see if each condition the user inputted is correct, if so, returns a random game title under those conditions
    if (user_genre in string_2[3]):
        if (user_player in string_2[1]):
            if (console_gen in string_2[2]):
                print('Here is a list of games recommended to you:\n', string_2[0])
                break

    counter = counter + 1

#creating pie chart for popular game genres

print('Here is a pie chart of how popular', user_genre, 'games are compared to other genres:')

import matplotlib.pyplot as plt

#random gen selects which games are chosen, percentages of numbers are given based on how often they were chosen. 

genres = ['Action', 'Adventure', 'Role-Play Game', 'Shooter', 'Survival', 'Strategy']
percents = [17, 12, 26, 10, 16, 35] #percentage outputs out of 100, values are how often they are chosen

plt.style.use('ggplot')
plt.title('Popular Game Genres')

#format of pie chart
plt.pie(x=percents, labels=genres, autopct='%.2f%') #how many decimal places

#;pcation of key to show which colors are which genre
plt.legend(loc='upper right')
plt.show() #display pie chart


#close file
file.close()