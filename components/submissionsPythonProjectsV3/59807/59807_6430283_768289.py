game_genres = ["Action", "Adventure", "RPG", "Strategy", "Sports", "Simulation"]
budget_ranges = {
    "Low": 10.00,
    "Medium": 30.00,
    "High": 70.00,
    "Very High": 100.00,
}
console_decision = ["Xbox", "Playstation", "Nintendo Switch", "PC"]

recommended_games = [
    ("Dead Island: Riptide", "Action", 10.00, "Playstation", "Medium"),
    ("Devil May Cry", "Action", 30.00, "Playstation", "Medium"),
    ("God of War Ragnarök", "Action",70.00, "Playstation", "Difficult"),
    ("Call of Duty Modern Warfare 2", "Action", 100.00, "Playstation", "Medium"),
    ("Dead Island: Riptide", "Action", 10.00, "Xbox", "Medium"),
    ("Devil May Cry", "Action", 30.00, "Xbox", "Medium"),
    ("Rainbow Six Siege", "Action", 70.00, "Xbox", "Difficult"),
    ("Mortal Kombat 1", "Action", 100.00, "Xbox", "Difficult"),
    ("Wonder 101", "Action", 10.00, "Nintendo Switch", "Medium"),
    ("Hades", "Action", 30.00, "Nintendo Switch", "Medium"),
    ("Pokemon Violet", "Action",70.00, "Nintendo Switch", "Medium"),
    ("Super Smash Bros Ultimate", "Action", 100.00, "Nintendo Switch", "Difficult"),
    ("Dead Island: Riptide", "Action", 10.00, "PC", "Medium"),
    ("Devil May Cry", "Action", 30.00, "PC", "Medium"),
    ("God of War", "Action", 70.00, "PC", "Medium"),
    ("Call of Duty Modern Warfare 2", "Action", 100.00, "PC", "Difficult"),


      ("Minecraft", "Adventure", 10.00, "Playstation", "Medium"),
      ("Titanfall 2", "Adventure", 30.00, "Playstation", "Medium"),
      ("Tiny Tina's Wonderland", "Adventure", 70.00, "Playstation", "Difficult"),
      ("Deathloop", "Adventure", 100.00, "Playstation", "Difficult"),
      ("Minecraft", "Adventure", 10.00, "Xbox", "Medium"),
      ("Titanfall 2", "Adventure", 30.00, "Xbox", "Medium"),
      ("Tiny Tina's Wonderland", "Adventure", 70.00, "Xbox", "Difficult"),
      ("Deathloop", "Adventure", 100.00, "Xbox", "Difficult"),
      ("Minecraft", "Adventure", 10.00, "Nintendo Switch", "Medium"),
      ("No Man's Sky", "Adventure", 30.00, "Nintendo Switch", "Medium"),
      ("The Legends of Zelda: Tears of the Kingdom", "Adventure", 70.00, "Nintendo Switch", "Medium"),
      ("Pokemon Legends: Arceus", "Adventure", 100.00, "Nintendo Switch", "Difficult"),
      ("Minecraft", "Adventure", 10.00, "PC", "Medium"),
      ("Titanfall 2", "Adventure", 30.00, "PC", "Medium"),
      ("Tiny Tina's Wonderland", "Adventure", 70.00, "PC", "Medium"),
      ("Deathloop", "Adventure", 100.00, "PC", "Difficult"),


      ("Hollow Knight", "RPG", 10.00, "PC", "Difficult"),
      ("Ghostrunner", "RPG", 30.00, "PC", "Difficult"),
      ("Borderlands 3", "RPG", 70.00, "PC", "Medium"),
      ("Spider Man", "RPG", 100.00, "PC", "Medium"),
      ("Hollow Knight", "RPG", 10.00, "Playstation", "Difficult"),
      ("Kena: Bridge of Spirits", "RPG", 30.00, "Playstation", "Difficult"),
      ("Borderlands 3", "RPG", 70.00, "Playstation", "Medium"),
      ("Spider Man 2 Digital Deluxe Edition", "RPG", 100.00, "Playstation", "Medium"),
      ("Hollow Knight", "RPG", 10.00, "Xbox", "Difficult"),
      ("Sekiro: Shadows Die Twice", "RPG", 30.00, "Xbox", "Difficult"),
      ("Borderlands 3", "RPG", 70.00, "Xbox", "Medium"),
      ("Elden Ring", "RPG", 100.00, "Xbox", "Difficult"),
      ("Hollow Knight", "RPG", 10.00, "Nintendo Switch", "Difficult"),
      ("Little Nightmares", "RPG", 30.00, "Nintendo Switch", "Medium"),
      ("Xenoblade Chronicles 2", "RPG", 70.00, "Nintendo Switch", "Medium"),
      ("Super Mario RPG", "RPG", 100.00, "Nintendo Switch", "Medium"),


      ("Overwatch 2", "Strategy", 10.00, "Playstation", "Medium"),
      ("Apex Legends", "Strategy", 30.00, "Playstation", "Difficult"),
      ("Armored Core 6: Fires of Rubicon", "Strategy", 70.00, "Playstation", "Difficult"),
      ("Dead By Daylight", "Strategy", 100.00, "Playstation", "Difficult"),
      ("Overwatch 2", "Strategy", 10.00, "Xbox", "Medium"),
      ("Apex Legends", "Strategy", 30.00, "Xbox", "Difficult"),
      ("Armored Core 6: Fires of Rubicon", "Strategy", 70.00, "Xbox", "Difficult"),
      ("Dead By Daylight", "Strategy", 100.00, "Xbox", "Difficult"),
      ("Overwatch 2", "Strategy", 10.00, "Nintendo Switch", "Difficult"),
      ("Apex Legends", "Strategy", 30.00, "Nintendo Switch", "Difficult"),
      ("Super Mario Bros Wonder", "Strategy", 70.00, "Nintendo Switch", "Medium"),
      ("Dead By Daylight", "Strategy", 100.00, "Nintendo Switch", "Difficult"),
      ("Overwatch 2", "Strategy", 10.00, "PC", "Medium"),
      ("Apex Legends", "Strategy", 30.00, "PC", "Difficult"),
      ("Armored Core 6: Fires of Rubicon", "Strategy", 70.00, "PC", "Difficult"),
      ("Dead By Daylight", "Strategy", 100.00, "PC", "Difficult"),


      ("PGA Tour 2K22", "Sports", 10.00, "Playstation", "Difficult"),
      ("FIFA 23", "Sports", 30.00, "Playstation", "Difficult"),
      ("Madden NFL 24", "Sports", 70.00, "Playstation", "Difficult"),
      ("NBA 2K24", "Sports", 100.00, "Playstation", "Difficult"),
      ("PGA Tour 2K22", "Sports", 10.00, "Xbox", "Medium"),
      ("FIFA 23", "Sports", 30.00, "Xbox", "Medium"),
      ("Madden NFL 24", "Sports", 70.00, "Xbox", "Medium"),
      ("NBA 2K24", "Sports", 100.00, "Xbox", "Medium"),
      ("PGA Tour 2K22", "Sports", 10.00, "Nintendo Switch", "Medium"),
      ("Nintendo Switch Sports", "Sports", 30.00, "Nintendo Switch", "Medium"),
      ("Madden NFL 24", "Sports", 70.00, "Nintendo Switch", "Medium"),
      ("NBA 2K24", "Sports", 100.00, "Nintendo Switch", "Medium"),
      ("PGA Tour 2K22", "Sports", 10.00, "PC", "Medium"),
      ("FIFA 23", "Sports", 30.00, "PC", "Medium"),
      ("Madden NFL 24", "Sports", 70.00, "PC", "Medium"),
      ("NBA 2K24", "Sports", 100.00, "PC", "Medium"),


      ("Farming Simulator 22", "Simluation", 10.00, "Playstation", "Medium"),
      ("Tony Hawk's Pro Skater 2", "Simluation", 30.00, "Playstation", "Medium"),
      ("Gran Turismo 7", "Simluation", 70.00, "Playstation", "Medium"),
      ("Rock Band 4", "Simluation", 100.00, "Playstation", "Medium"),
      ("Farming Simulator 22", "Simluation", 10.00, "Xbox", "Medium"),
      ("Tony Hawk's Pro Skater 2", "Simluation", 30.00, "Xbox", "Medium"),
      ("Microsoft Flight Simulator", "Simluation", 70.00, "Xbox", "Medium"),
      ("Rock Band 4", "Simluation", 100.00, "Xbox", "Medium"),
      ("Farming Simulator 22", "Simluation", 10.00, "Nintendo Switch", "Medium"),
      ("Go Vacation", "Simluation", 30.00, "Nintendo Switch", "Medium"),
      ("New Pokemon Snap", "Simluation", 70.00, "Nintendo Switch", "Medium"),
      ("Rock Band 4", "Simluation", 100.00, "Nintendo Switch", "Medium"),
      ("Farming Simulator 22", "Simluation", 10.00, "PC", "Medium"),
      ("Microsoft Flight Simulator", "Simluation", 30.00, "PC", "Medium"),
      ("Euro Truck Simulator 2", "Simluation", 70.00, "PC", "Medium"),
      ("The Sims 4", "Simluation", 100.00, "PC", "Medium"),
]


print("Choose a game genre:")
for i, genre in enumerate(game_genres, 1):
    print(f"{i}. {genre}")

genre_choice = int(input("Enter the number of your preferred genre: "))

if 1 <= genre_choice <= len(game_genres):
    selected_genre = game_genres[genre_choice - 1]
    print(f"You selected the '{selected_genre}' genre.")
else:
    print("Invalid input. Please select a valid genre.")
    exit()


print("Choose your budget range:")
for i, (range_name, max_price) in enumerate(budget_ranges.items(), 1):
    print(f"{i}. {range_name} (up to ${max_price:.2f})")

budget_choice = int(input("Enter the number of your budget range: "))

if 1 <= budget_choice <= len(budget_ranges):
    selected_budget_range, max_price = list(budget_ranges.items())[budget_choice - 1]
    print(f"You selected the '{selected_budget_range}' budget range (up to ${max_price:.2f}).")
else:
    print("Invalid input. Please select a valid budget range.")
    exit()
print("Choose a console:")
for i, console in enumerate(console_decision, 1):
    print(f"{i}. {console}")

console_choice = int(input("Enter the number of your preferred console: "))

if 1 <= console_choice <= len(console_decision):
    selected_console = console_decision[console_choice - 1]
    print(f"You selected '{selected_console}' console.")
else:
    print("Invalid input. Please select a valid console.")
    exit()


filtered_games = [
    game for game in recommended_games
    if game[1] == selected_genre
    and game[2] <= max_price
    and game[3] == selected_console
]

if not filtered_games:
    print("No games match your criteria. Please try different selections.")
else:
    print("\nRecommended Games:")
    for i, (game_title, game_genre, game_price, game_console, game_difficulty) in enumerate(filtered_games, 1):
        print(f"{i}. Title: {game_title}, Genre: {game_genre}, Price: ${game_price:.2f}, Console: {game_console}, Difficulty: {game_difficulty}")

recommendation_answer = ["Yes", "No"]
print("\nAre you happy with this recommendation:")
for i, answer in enumerate(recommendation_answer, 1):
    print(f"{i}. {answer}")

recommendation_choice = int(input("Enter your answer: "))

if 1 <= recommendation_choice <= len(recommendation_answer):
    selected_recommendation_answer = recommendation_answer[recommendation_choice - 1]
    if selected_recommendation_answer == "Yes":
        print("I'm glad you liked the recommendation I gave you! Thank you for using my recommendation system!")
    else:
        print("Sorry I didn't give you a good recommendation. Better luck next time!")
else:
    print("Invalid recommendation choice.")