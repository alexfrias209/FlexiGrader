import matplotlib.pyplot as plt

# This section of code is to keep track of data inputted for the Users, Songs and Ratings, and Artists Mean. 
user_database = {}
song_database = {}
artist_database = {}

# This part of the code is used to input new users to program if user isn't new, it will not be executed.
def add_user(username):
    if username not in user_database:
        user_database[username] = []

# First asks for a username.
# Then asks for information including played song, artist, rating.
# Stores the information in the user database, song database, and artist database.
def add_played_track(username, artist, song, rating):
    if username in user_database:
        if 0 <= rating <= 5:
            user_database[username].append((artist, song, rating))
            
            if artist not in artist_database:
                artist_database[artist] = {"total_ratings": 0, "num_songs": 0}
            artist_database[artist]["total_ratings"] += rating
            artist_database[artist]["num_songs"] += 1
            song_database[(artist, song)] = rating
        else:
            print("Rating must be between 0 and 5. Please try again.")
            # You can add a loop here to keep asking for a valid rating.
            while True:
                try:
                    new_rating = float(input("Enter a new rating (0-5): "))
                    if 0 <= new_rating <= 5:
                        # Add the new valid rating to the database and break the loop.
                        rating = new_rating
                        user_database[username].append((artist, song, rating))
                        artist_database[artist]["total_ratings"] += rating
                        artist_database[artist]["num_songs"] += 1
                        song_database[(artist, song)] = rating
                        break
                    else:
                        print("Invalid rating. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a numeric rating.")
    else:
        print("User not found in database!")

# This will sort the users inputted songs into chronological order from highest to lowest rating.
# Must be from 0-5 of course or it will not show up in order
def sort_songs_by_rating():
    sorted_songs = sorted(song_database.items(), key=lambda item: item[1], reverse=True)
    return sorted_songs

# This creates a histogram of artist rankings
# This shows the artists from highest ratigns to lowest as well
# Only takes artists that were inputted to the database
# Named Graph Recommended Artists to demonstrate your most liked to least liked
def generate_artist_histogram():
    artist_avg_ratings = {}
    for artist, data in artist_database.items():
        if data["num_songs"] > 0:
            avg_rating = data["total_ratings"] / data["num_songs"]
            artist_avg_ratings[artist] = avg_rating

    sorted_artists = sorted(artist_avg_ratings.items(), key=lambda item: item[1], reverse=True)
    artists, avg_ratings = zip(*sorted_artists)

    plt.bar(range(len(artists)), avg_ratings)
    plt.xticks(range(len(artists)), artists, rotation=90)
    plt.xlabel("Artists")
    plt.ylabel("Average Ratings")
    plt.title("Recommended Artists")
    plt.show()

# Main loop
# Takes all of the inputs from the user and inputs into the functions above^
while True:
    print("\n\nWelcome to my ME021 Project called Music Player!")
    print("What would you like to do today?")
    print("1. Add a user")
    print("2. Add a played track and rating")
    print("3. Sort songs by rating")
    print("4. Generate Artist Rankings Histogram")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Please enter your desired username: ")
        add_user(username)
    
    elif choice == '2':
        username = input("Please enter your username: ")
        artist = input("Enter the artist name: ")
        song = input("Enter the song title: ")
        rating = float(input("Enter the rating (0-5): "))
        print(f"Now Playing {song} by {artist}!")
        add_played_track(username, artist, song, rating)
    
    elif choice == '3':
        sorted_songs = sort_songs_by_rating()
        print("Top-rated songs:")
        for (artist, song), rating in sorted_songs:
            print(f"{artist} - {song}: {rating}")
    
    elif choice == '4':
        generate_artist_histogram()
    
    elif choice == '5':
        print("Thank you for using my ME021 Project!")
        break

    else:
        print("Please pick a valid option!")
