# 55081_6421709_4247651

def goals_2023_2024(player_name):
    Goals = '20 goals'
    return f"{player_name} scored {Goals} in the 2023/2024 season so far!"
def all_time_goals(player_name):
    Goals = '862 goals'
    return f"{player_name} scored {Goals} in over 1,100 appearances!"
def trophies(player_name):
    # Replace these with the actual trophies information for the player
    league_trophies = 5
    champions_league_trophies = 4
    domestic_cup_trophies = 3
    fifa_club_WC = 5
    UEFA_Nations = 1
    English_champ = 3
    Spanish_champ = 2
    Italian_champ = 2
    Euro_champ = 1
    

    # Construct a message with the player's trophies
    message = f"{player_name} has won the following trophies:\n"
    message += f"League Trophies: {league_trophies}\n"
    message += f"Champions League Trophies: {champions_league_trophies}\n"
    message += f"Domestic Cup Trophies (UEFA Supercup): {domestic_cup_trophies}\n"
    message += f"FIFA Club World Cups: {fifa_club_WC}\n"
    message += f"UEFA Nations Championship: {UEFA_Nations}\n"
    message += f"English Championship: {English_champ}\n"
    message += f"Spanish Championship: {Spanish_champ}\n"
    message += f"Italian Championship: {Italian_champ}\n"
    message += f"European Championship: {Euro_champ}\n"
    return message
def clubs(player_name):
    clubs = [
        {
            'name': 'Manchester United',
            'years': '2003-2009',
        },
        {
            'name': 'Real Madrid',
            'years': '2009-2018',
        },
        {
            'name': 'Juventus',
            'years': '2018-2021',
        },
        {
            'name': 'Manchester United',
            'years': '2021-2022',
        },
        {
            'name': 'Al-Nassr',
            'years': '2022- Present time',
        }
    ]
    message = f"{player_name}'s Club History!:\n"
    for club in clubs:
        message += f"{club['name']} ({club['years']})\n"
    return message

def international_history(player_name):
    # Replace these with the actual international history information for the player
    international_teams = [
        {
            'team': 'Portugal',
            'caps': 180,
            'goals': 120,
        },
        {
            'team': 'International XI',
            'caps': 5,
            'goals': 3,
        }
    ]

    # Construct a message with the player's international history
    message = f"{player_name}'s international history:\n"
    for team in international_teams:
        message += f"{team['team']}  Caps: {team['caps']}, Goals: {team['goals']}\n"

    return message
player_name = 'Ronaldo'




