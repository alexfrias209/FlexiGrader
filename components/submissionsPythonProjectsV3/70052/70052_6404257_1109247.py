developer = "R"
import csv

chill = []
aggressive = []
dance = []
hip_hop = []
with open("song.csv", newline='') as file:
        csvFile = csv.reader(file)
        data = list(csvFile)
        for line in data:
                chill.append(line[0])
                aggressive.append(line[1])
                dance.append(line[2])
                hip_hop.append(line[3])
#Lists of songs from my playlist
#extracted from csv file

choices = ["choose","get recommendations","recommendations","playlist"]
end_options = ["try again","check list","end"]
dont = 0
personal_list = []
genres = {'chill': chill, 'aggressive': aggressive, 'dance': dance,
          'hip hop': hip_hop}
months = ['january','february','march','april','may','june','july','august','september','october','november',
          'october','november','december']
#list and dictionaries used in programming

O = 0
#^^This will determine everything

print (f"Hello user, welcome to my project. \n")
#Intro and welcome
while dont == 0:
        genre = input("Please choose a genre from this list by writing its name.\n"
              "[Chill     ]\n"
              "[Aggressive]\n"
              "[Dance     ]\n"
              "[Hip Hop   ]")
#List of genres 

        while genre.lower() not in genres:
                print ("That's not a genre here! Try again!")
                genre = input("Choose a genre!")
#Checks if they actually chose from list and loops until they get it right!
    
        print (f"You have chosen the {genre} genre!")
        choice = input(f"Would you like to choose from the playlist or get recommendations?")
        choice = choice.lower()
        while choice not in choices:
                print ("Not a option!")
                choice = input(f"Would you like to choose from the playlist or get recommendations?")
                choice = choice.lower()
        if choice == "choose" or choice == "playlist":
            dont = 1
            while dont == 1: 
                print (genres[genre.lower()])
                chosen = input("Write the name of the song to put it in your list!")
                while chosen not in genres[genre.lower()]:
                        print ("Make sure it looks the same as its written!")
                        chosen = input("Write the name of the song to put it in your list!")
                if chosen not in personal_list:
                        personal_list.append(chosen)
                print ("Done!")
                choice2 = input("Add another or stop?")
                choice2 = choice2.lower()
                if choice2 == ("add another"):     
                        dont == 1
                        continue
                elif choice2 == ("stop"):
                        break
                break
#Huge code for when they want to choose directly from the chosen playlist

        elif choice == "get recommendations" or choice == "recommendations":
                dont = 0
        while dont == 0:    
                month = input("Now what month were you born in?")

                while month.lower() not in months: 
                    print (f"Not a month! Try again!")
                    month = input("Now what month were you born in?")
                print ("That's a month!")
#makes sure they actually input a month, otherwise it loops until they do!

                O = ((len(month) + len(genre)) - 10)
                if O < 0:
                    O = 0
                elif O > 12:
                    O = 12
#Will make sure number generated for recommendations doesn't fall out of indexes
                    
                final_song = genres[genre.lower()][O]
                final_song2 = genres[genre.lower()][O-1]
                final_song3 = genres[genre.lower()][O-2]
                for i in range(3):
                    if (genres[genre.lower()][O-i]) not in personal_list:
                        personal_list.append(genres[genre.lower()][O-i])
#give 2 more songs closely connected to original

                print (f"You chose the {genre} genre and were born in {month}, \n"
                       f"here's some songs! : {final_song}, {final_song2}, and {final_song3}\n")
                break
#final result for recommendations
        
        dont = 1
        while dont == 1:
            ending = input("Try again,check list,get text file or end?")
            ending = ending.lower()
            if ending == ("try again"):
                dont = 0
            elif ending == ("check list"):
                dont = 1
                print (personal_list)
            elif ending == ("get text file"):
                dont= 1
                with open('userslist.txt', 'w+') as file:
                        for item in personal_list:
                                file.write(f"{item}\n")
                        file.seek(0)
                        file_stuff = file.read()
                        print (file_stuff)
                        file.close
            elif ending == ("end"):
                dont = 2
                quit
#end of code where the user can choose a variety of things to do
#such as
#       -trying again for either more songs or perhaps use the other option at the start
#       -checking their list which is made up of their songs
#       -getting a text file based on the list
#       -or just ending the code so they don't have to kill it 
