def welcome_statement():
    username = input("And whom might you be?\n")
    age = input("If you don't mind me asking, how old are you?\n")
    print(f"Hi {username} and welcome to Tristhan's music recommendation program!\n")
    
welcome_statement()#greets user and asks some info

music_preference = input("Do you prefer old school music or modern music? \n")#will setup which csv is used

print(f"Oh you prefer {music_preference}? Nice choice! \n")

print("Are you having trouble picking out tunes? Well I got your back!\n")

print("If you are feeling energetic and want some heavy beats, rock is the way to go!\n")

print("If you are in a dancey vibe and just want some good vibes in general then pop music might be just for you. \n")

print("If the western cowboy music is your type then Country will suit you just fine. \n")

print("If the blues or swing is swaying you with the rhythmn then jazz is a great choice! \n")

print("If you like rock and heavy metal but wanna slow down the pace a bit then Grunge is the way to go! \n")

print("If you're more interested in rhyming at a fast speed then rap will blow your mind! \n")

print("And if you love the blues and gospel music then the soul genre will suit you very well. \n")

if music_preference == "old school music":#Chooses what they prefer because age doesnt necessarily determine the music age they like
    csv_file = '55782_6418888_2762458.csv'

else:
    csv_file = '55782_6418889_4209071.csv'

import csv
    
with open(csv_file, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)

print("Genres mentioned above:")
for i, header in enumerate(headers):
    if i != 0:
        print(f"{i}: {header}")

selected_column = None
while selected_column is None:
    try:
        column_number = int(input("Enter the number of the genre you'd like to vibe with:"))
        if 0 <= column_number < len(headers):#Column_number should be less than len b/c equal to would result in error
            selected_column = headers[column_number]
        else:
            print("Wrong Column.")
    except ValueError:
        print("Your input needs to be a number from the list given.")

songs = [] # empty list for songs

with open(csv_file, 'r', newline='') as file: #Reads out the songs listed in the CSV
    csv_reader = csv.reader(file)
    next(csv_reader)  # Alex Frias: next to skip headers
    for row in csv_reader:
        if len(row) > column_number:
            songs.append(row[column_number])

if songs:
    print(f"Some songs from this genre that you should listen to are: \n")
    for value in songs:
        print(value)
else:
    print(f"No values found in the selected column '{selected_column}'.")





                
