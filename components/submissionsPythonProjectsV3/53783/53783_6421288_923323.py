import random
print('Hello, welcome to my random movie generator!\n')
print('With my project, I hope to make an app that, given a certain genre and actors')
print('will recommend you a movie of your liking.')

valid_genres = ['comedy', 'romance', 'action', 'horror']

while True:
    genre = input('To begin, please choose a movie genre from the given choices: comedy, romance, action, or horror: ')

    if genre.lower() in valid_genres:
        break
    else:
        print('Invalid genre. Please choose a valid genre.')


actor_input = input('Enter your preferred actor from the given pool (Scarlett Johansson, Jake Gyllenhaal, Adam Sandler, Jennifer Aniston): ')
preferred_actor = actor_input.lower()

recommendations = {
    'comedy': [
        {"title": "The Waterboy", "actors": ["Adam Sandler"]},
        {"title": "Spiderman: Far From Home", "actors": ["Jake Gyllenhaal"]},
        {"title": "Jojo Rabbit", "actors": ["Scarlett Johansson"]},
        {"title": "Just Go With it", "actors": ["Jennifer Aniston"]},
        {"title": "Big Daddy", "actors": ["Adam Sandler"]},
        {"title": "Demolition", "actors": ["Jake Gyllenhaal"]},
        {"title": "Hail Ceaser", "actors": ["Scarlett Johansson"]},
        {"title": "Friends", "actors": ["Jennifer Aniston"]},
        {"title": "The Ridiculous 6", "actors": ["Adam Sandler"]},
        {"title": "Barbie", "actors": ["Jake Gyllenhaal"]},
        {"title": "Asteroid City", "actors": ["Scarlett Johansson"]},
        {"title": "We're the Millers", "actors": ["Jennifer Aniston"]},
        
        
        
    ],
    'romance': [
        {"title": "The Wedding Singer", "actors": ["Adam Sandler"]},
        {"title": "Love and Other Drugs", "actors": ["Jake Gyllenhaal"]},
        {"title": "Marriage Story", "actors": ["Scarlett Johansson"]},
        {"title": "Love Happens", "actors": ["Jennifer Aniston"]},
        {"title": "Punch-Drunk Love", "actors": ["Adam Sandler"]},
        {"title": "Accidental Love", "actors": ["Jake Gyllenhaal"]},
        {"title": "He's Just Not That Into You", "actors": ["Scarlett Johansson"]},      
        {"title": "The Breakup", "actors": ["Jennifer Aniston"]},
        {"title": "Blended", "actors": ["Adam Sandler"]},
        {"title": "The Good Girl", "actors": ["Jake Gyllenhaal"]},
        {"title": "The Nanny Diaries", "actors": ["Scarlett Johansson"]},
        {"title": "Along Came Polly", "actors": ["Jennifer Aniston"]},
        
        
        
    ],
    'action': [
        {"title": "The Do Over", "actors": ["Adam Sandler"]},
        {"title": "The Covenant", "actors": ["Jake Gyllenhaal"]},
        {"title": "Avengers Endgame", "actors": ["Scarlett Johansson"]},
        {"title": "Murder Mystery", "actors": ["Jennifer Aniston"]},
        {"title": "You Don't Mess With Zohan", "actors": ["Adam Sandler"]},
        {"title": "Southpaw", "actors": ["Jake Gyllenhaal"]},
        {"title": "Avengers: Age of Ultron", "actors": ["Scarlett Johansson"]},
        {"title": "Derailed", "actors": ["Jennifer Aniston"]},
        {"title": "Uncut Gems", "actors": ["Adam Sandler"]},
        {"title": "Jarheads", "actors": ["Jake Gyllenhaal"]},
        {"title": "Avengers Infinity War", "actors": ["Scarlett Johansson"]},
        {"title": "Life Of Crime", "actors": ["Jennifer Aniston"]},
        
        
        
        
        
    ],
    'horror': [
        {"title": "Hubie Halloween", "actors": ["Adam Sandler"]},
        {"title": "Zodiac", "actors": ["Jake Gyllenhaal"]},
        {"title": "The Black Dahlia", "actors": ["Scarlett Johansson"]},
        {"title": "Leprechaun", "actors": ["Jennifer Aniston"]},
        {"title": "Hotel Transylvania", "actors": ["Adam Sandler"]},
        {"title": "Life", "actors": ["Jake Gyllenhaal"]},
        {"title": "Under The Skin", "actors": ["Scarlett Johansson"]},
        {"title": "Donnie Darko", "actors": ["Jake Gyllenhaal"]},
        {"title": "The Island", "actors": ["Scarlett Johansson"]},
        
        
    ]
}


filtered_movies = [
    movie["title"] for movie in recommendations.get(genre.lower(), [])
    if preferred_actor in [actor.lower() for actor in movie.get("actors", [])]
]

if not filtered_movies:
    print(f'Sorry, no {genre} movies with the chosen actor match your criteria.')
else:

    selected_movie = random.choice(filtered_movies)
    print(f'Your randomly selected {genre} movie with the chosen actor is: {selected_movie}.')



