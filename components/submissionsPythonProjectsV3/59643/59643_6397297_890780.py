#Music Playlist Creator: Users can create and save playlists. Playlists can be loaded, edited, and saved back to files.
#Users may add statistics about the songs they listened to. Visualize the data of user listening history

#Project must do the following:

#Control the program flow with branching and loops
#Uses correct data structures for optimal computations
#Uses functions for modular code
#Loads data from files (real-world data is preferable) and writes outputs to files (if needed)
#Documents the flow of logic with comments, docstrings, and user-friendly messages


import os
import random

songs_heard = {}

liked_songs = open('Liked songs.txt', 'w', encoding="cp1252") 
liked_songs = []

    
print("\n","Welcome' Playlist! (ME021 Python Project)","\n","Please enjoy the music and feel free to customize the playlist to your liking") #Friendly comment
print()
user_in = 0 #base response

def invalid(): #default response for error from user
    print()
    print("Response was not accepted, Please try again. :)")
    print()
    return()

while user_in != "6":  #typing 6 will exit program
    print()
    print("What would you like to do?")
    print("1. View Playlist")
    print("2. View Music Statistics")
    print("3. Remove Song")
    print("4. Add Song")
    print("5. Listen to Music!") 
    print("6. Exit")
    print()
    user_in = input('Please Select Option 1-6. (ex: "3"): ')
    print()

    if user_in == "1":      # will print list of playlist
        if liked_songs == []:
            print("There are no songs in your playlist :(")
            print()
        else:
            print(liked_songs)
            print()
            
    elif user_in == "2":
        for songs in songs_heard: 
            
            print(songs,"was listened to",songs_heard.get(songs),"times.")

        if songs_heard == {}:
            print("No Songs have been listened to yet. :(")             #if no songs have been added

        print()

                
    elif user_in == "3":
        remove = input("What song would you like to Remove?\n: ")
        if remove in liked_songs:
            response = input(f'Are you sure you want to remove{remove}? (i.e. "Yes" or "No"\n:')
            if response == "Yes":
                liked_songs.remove(remove)
            elif response == "No":
                print("No worries")
            else:
                print("Reponse was not accepted, please try again")
        
        else:
            print("Song was not found. :( , try again.")
        print()
                
    elif user_in =="4":
        add = input("What song would you like to Add?\n:")
        if add in liked_songs:
            response = input(f'This song is already in the playlist, are you sure you want to add {add}? (i.e. "Yes" or "No")\n:') 
            if response == "Yes":
                liked_songs.append(add)
                songs_heard[add] = int(0)
            elif response == "No":
                print("No worries")
            else:
                print("Reponse was not accepted, please try again")
        elif add not in liked_songs:
            response = input(f'Are you sure you want to add {add}? (i.e. "Yes" or "No")\n:') 
            if response == "Yes":
                liked_songs.append(add)
                songs_heard[add] = int(0)
            elif response == "No":
                print("No worries")
            else:
                invalid ()
                
        print()


    elif user_in == "5":
        print("What would you like to listen to?")
        print("1. One song only")
        print("2. Entire playlist")
        response = input("Please select which option. (i.e. '1' or '2'): ")

        if response == "1":
            print()
            song = input('Please input the Song name ')
                
            if song in liked_songs:
                print("Playing", song)
                print(".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n")
                print("Completed!")

                

                songs_heard[song] = songs_heard[song] + 1

            else:
                print("Song was not found. :( , try again.")

        elif response == "2":
            print()
            print("How would you like to listen to your playlist?")
            print()
            print("1. Normal\n2. Reversed\n3. Shuffle")
            answer = input("Please select which option. (ex '2'): ")

            if answer == "1":
                for song in liked_songs:
                    print("Playing", song)
                    print(".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n")
                    print("Completed!")
                    print()

                    songs_heard[song] = songs_heard[song] + 1
                    
            elif answer == "2":
            
                liked_songs.reverse()

                for song in liked_songs:
                    print("Playing", song)
                    print(".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n")
                    print("Completed!")
                    print()

                    songs_heard[song] = songs_heard[song] + 1
                        
                liked_songs.reverse()
                
                    
            elif answer == "3":

                

                for song in liked_songs:                                #FIXME Create random # from 0 to len(list) then choose list by the number
                    
                    playlist_shufl = random.randint(0, len(liked_songs) - 1)
                    print("Playing", liked_songs[playlist_shufl])
                    print(".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n")
                    print("Completed!")
                    print()
                    songs_heard[song] = songs_heard[song] + 1

                    
            else:
                invalid ()
                  
        
 



        print()
                
                
            
                    
            
        





print()
print('Have a wonderful day! :D')

    
