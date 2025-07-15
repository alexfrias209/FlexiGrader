# 55081_6421708_4632527 

def goals_2023_2024(player_name):
    Goals = '32 goals'
    return f"{player_name} scored {Goals} in the 2023/2024 season so far!"
def all_time_goals(player_name):
    Goals = '821 goals'
    return f"{player_name} scored {Goals} in 1,045 appearances!"
def trophies(player_name):
    # Replace these with the actual trophies information for the player
    league_trophies = 7
    champions_league_trophies = 4
    domestic_cup_trophies = 3
    fifa_club_WC = 3
    French_SC = 1
    FIFA_WC = 3
    Spanish_champ = 10
    French_champ = 2
    CopaAM_champ = 1
    

    # Construct a message with the player's trophies
    message = f"{player_name} has won the following trophies:\n"
    message += f"League Trophies: {league_trophies}\n"
    message += f"Champions League Trophies: {champions_league_trophies}\n"
    message += f"Domestic Cup Trophies (UEFA Supercup): {domestic_cup_trophies}\n"
    message += f"FIFA Club World Cups: {fifa_club_WC}\n"
    message += f"French Super Cup Championship: {French_SC}\n"
    message += f"Fifa Worldcup: {FIFA_WC}\n"
    message += f"Spanish Championship: {Spanish_champ}\n"
    message += f"French Championship: {French_champ}\n"
    message += f"Copa América Championship: {CopaAM_champ}\n"
    return message
def clubs(player_name):
    clubs = [
        {
            'name': 'Barcelona',
            'years': '2005-2021',
        },
        {
            'name': 'PSG',
            'years': '2021-2023',
        },
        {
            'name': 'Inter Miami',
            'years': '2023-Present Time',
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
            'team': 'Argentina',
            'caps': 178,
            'goals': 106,
        }
    ]

    # Construct a message with the player's international history
    message = f"{player_name}'s international history:\n"
    for team in international_teams:
        message += f"{team['team']}  Caps: {team['caps']}, Goals: {team['goals']}\n"

    return message
player_name = 'Messi'




