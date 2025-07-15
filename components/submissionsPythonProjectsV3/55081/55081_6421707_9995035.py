import csv
import matplotlib.pyplot as plt

def create_goal_leaders_graph(players):#name handle to call graph
    player_names = list(players.keys())
    player_goals = list(players.values())

    #creating graph
    plt.figure(figsize=(10, 6))
    plt.barh(player_names, player_goals)
    plt.xlabel('Goals')
    plt.title('Leading Players in Goals (LaLiga)')
    plt.gca().invert_yaxis()  # Reverse the order to show the highest scorer at the top
    plt.show()

players_data = {}#list for graph data

with open('55081_6421705_9582593.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:#to read csv file
        if row['League'] == 'LaLiga' and row['Category'] == 'Leading players in Goals':
            player_name = row['Player']
            goals = int(row['Goals'])
            players_data[player_name] = goals #used to seperate the columns of information
        
def create_assist_leaders_graph(players):
    player_names = list(players.keys())
    player_assists = list(players.values())

    plt.figure(figsize=(5,3))
    plt.barh(player_names, player_assists)
    plt.xlabel('Assists')
    plt.title('Leading Players in Assists (LaLiga)')
    plt.gca().invert_yaxis()  # Reverse the order to show the most assists at the top
    plt.show()

players_assists = {}

with open('55081_6421704_4432019.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['League'] == 'LaLiga' and row['Category'] == 'Leading players in Assists':
            player_name = row['Player']
            assists = int(row['Assists'])
            players_assists[player_name] = assists

def create_title_leaders_graph(teams):
    team_names = list(teams.keys())
    team_titles = list(teams.values())

    plt.figure(figsize=(40,8))
    plt.barh(team_names, team_titles)
    plt.xlabel('Titles')
    plt.title('Leading Teams in Titles (LaLiga)')
    plt.gca().invert_yaxis()  # Reverse the order to show the most titles on top
    plt.show()

teams_titles = {}

with open('55081_6421710_2604273.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['League'] == 'LaLiga' and row['Category'] == 'Leading team in trophies':
            team_name = row['Team']
            titles = int(row['Trophies'])
            teams_titles[team_name] = titles

def create_league_standings_graph(team):
    team_names = list(team.keys())
    team_titles = list(team.values())

    plt.figure(figsize=(30,0))
    plt.barh(team_names, team_titles)
    plt.xlabel('League Points')
    plt.title('League Standings (LaLiga)')
    plt.gca().invert_yaxis()  # Reverse the order to show the most points at the top
    plt.show()

teams_standings = {}

with open('55081_6421706_227317.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['League'] == 'LaLiga' and row['Category'] == 'LaLiga Standings':
            team_name = row['Team']
            standings = int(row['Points'])
            teams_standings[team_name] = standings

while True: #will loop until system is shut down with '4'
    print("Welcome to this FIFA' statistics search engine!")
    print('Developed by Fernando Tapia')
    print("Please choose one of the following options:")
    print()
    print("1. Cristiano Ronaldo")
    print("2. Lionel Messi")
    print("3. LaLiga")
    print("4. Exit")
    print()
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        while True:
            print()
            print("You chose option 1: Cristiano Ronaldo")
            print("Which of these options are you looking for?: ")
            print()
            print("1. Goals of 2023/24 Season")
            print("2. All-time Goals")
            print("3. Trophies")
            print("4. Club History")
            print("5. International History")
            print("6. Return")
            print()
            choice = input("Enter your choice (1/2/3/4/5/6): ")
            import Ronaldo #thought this will help when the py file should be executed
            player_name = 'Cristiano Ronaldo'
            if choice == '1':
                print(Ronaldo.goals_2023_2024(player_name))#to get outputs out, followed same trend throughout program
            elif choice == '2':
                print(Ronaldo.all_time_goals(player_name))
            elif choice == '3':
                print(Ronaldo.trophies(player_name))
            elif choice == '4':
                print(Ronaldo.clubs(player_name))
            elif choice == '5':
                print(Ronaldo.international_history(player_name))
            elif choice == '6':
                print("Returning to Main Menu.")
                print()
                break

    elif choice == '2':
        while True:
            print()
            print("You chose option 2: Lionel Messi")
            print("Which of these options are you looking for?: ")
            print()
            print("1. Goals of 2023/24 Season")
            print("2. All-time Goals")
            print("3. Trophies")
            print("4. Club History")
            print("5. International History")
            print("6. Return")
            print()
            choice = input("Enter your choice (1/2/3/4/5/6): ")
            import Messi
            player_name = 'Lionel Messi'
            if choice == '1':
                print(Messi.goals_2023_2024(player_name))
            elif choice == '2':
                print(Messi.all_time_goals(player_name))
            elif choice == '3':
                print(Messi.trophies(player_name))
            elif choice == '4':
                print(Messi.clubs(player_name))
            elif choice == '5':
                print(Messi.international_history(player_name))
            elif choice == '6':
                print("Returning to Main Menu.")
                print()
                break

    elif choice == '3':
        while True:
            print()
            print("You chose option 3: LaLiga")
            print("Which of these options are you looking for?: ")
            print()
            print("1. Leading players in Goals")
            print("2. Leading players in Assists")
            print("3. All Time Trophies in LaLiga")
            print("4. League standings")
            print("5. Return")
            print()
            choice = input("Enter your choice (1/2/3/4/5): ")
            if choice == '1':
               create_goal_leaders_graph(players_data)#forced graph output
            elif choice == '2':
                create_assist_leaders_graph(players_assists)
            elif choice == '3':
                create_title_leaders_graph(teams_titles)
            elif choice == '4':
                create_league_standings_graph(teams_standings)
            elif choice == '5':
                print("Returning to Main Menu.")
                print()
                break

    elif choice == '4':
        print("Goodbye!")
        break
