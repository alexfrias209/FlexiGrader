import random

# Structures that store available options for both players
player_hands = {
    'R': 0,
    'P': 0,
    'S': 0
}
ai_hands = {
    'R': 0,
    'P': 0,
    'S': 0
}

wins = 0
losses = 0
ties = 0

try:
    with open("scores", 'r') as scores:
        scores_nums = scores.read().split()
    
        wins = int(scores_nums[0])
        losses = int(scores_nums[1])
        ties = int(scores_nums[2])
except:
    with open("scores", 'w') as scores:
        scores.write(f"0 0 0")

# Maintains whether the player is in advantage, disadvantage, or none
game_state = "neutral"

# These store choices
choice = ""
ai_choice = ""

def Menu():
    print("Welcome to Rock Paper Scissors!")
    print("1 - Play")
    print("2 - Info")
    print("3 - Display Scores")
    choice = int(input("Choose an option by number: "))

    while choice != 1 and choice != 2 and choice != 3:
        print()
        choice = int(input("Invalid choice: "))
    print()

    return choice

def Info():
    print("In this version of RPS, you have a limited number of rocks, papers, and scissors (hands) to throw out. When you run out of hands, you lose. The game starts out in neutral, which means that nobody is in a state of advantage or disadvantage. You are put in advantage when you win at neutral and disadvantage when you lose at neutral. You and your opponent cannot see each other's hands.")
    print("Disadvantage: When in disadvantage, ties count as a win for the one in advantage. However, you can attempt to reverse your situation by catching. If you catch, you take the opponent's hand and return to neutral. However, do not abuse this option as the one in advantage has a way of dealing with this.")
    print("Advantage: As stated earlier, ties count as a win for you. Although those in disadvantage can attempt to catch your hand to be put in advantage, you can call out a catch to instead cause your opponent to lose a random hand. However, a missed call causes you to lose advantage, lose a random hand, and return to neutral.")

def IsWin():
    if choice == 'R' and ai_choice == 'P' or choice == 'P' and ai_choice == 'S' or choice == 'S' and ai_choice == 'R':
        return False
    elif choice == 'R' and ai_choice == 'S' or choice == 'S' and ai_choice == 'P' or choice == 'P' and ai_choice == 'R':
        return True

def IsEndGame():
    global game_state
    
    player_hands_count = list(player_hands.values())
    ai_hands_count = list(ai_hands.values())

    # Checks if one side is out of available choices
    if player_hands_count == [0, 0, 0]:
        game_state = "player lost"
    elif ai_hands_count == [0, 0, 0]:
        game_state = "player won"
    # Tie if the game is put in a state where the game cannot progress
    elif player_hands_count == [1, 0, 0] and ai_hands_count == [1, 0, 0] or player_hands_count == [0, 1, 0] and ai_hands_count == [0, 1, 0] or player_hands_count == [0, 0, 1] and ai_hands_count == [0, 0, 1]:
        game_state = "player tie"

    

def GetRandomValidChoice(hands, include_c=True):
    if include_c:
        choices = "RPSC"
    else:
        choices = "RPS"
        
    while True:
        random_choice = random.choice(choices)

        if random_choice == 'C' or hands[random_choice] > 0:
            return random_choice
        else:
            continue

def Play():
    global choice
    global ai_choice
    global game_state

    hand_size = int(input("How many hands do you want the game to begin with?: "))

    # Splits up the amount of available choices evenly
    player_hands['R'] = random.uniform(0.2, 0.4)
    player_hands['P'] = random.uniform(0.2, 0.4)
    player_hands['S'] = random.uniform(0.2, 0.4)
    total = player_hands['R'] + player_hands['P'] + player_hands['S']
    player_hands['R'] = round(hand_size * (player_hands['R'] / total))
    player_hands['P'] = round(hand_size * (player_hands['P'] / total))
    player_hands['S'] = hand_size - player_hands['R'] - player_hands['P']
    ai_hands['R'] = random.uniform(0.2, 0.4)
    ai_hands['P'] = random.uniform(0.2, 0.4)
    ai_hands['S'] = random.uniform(0.2, 0.4)
    total = ai_hands['R'] + ai_hands['P'] + ai_hands['S']
    ai_hands['R'] = round(hand_size * (ai_hands['R'] / total))
    ai_hands['P'] = round(hand_size * (ai_hands['P'] / total))
    ai_hands['S'] = hand_size - ai_hands['R'] - ai_hands['P']

    while True:
        while True:
            # State and win check
            if game_state == "neutral":
                break
            elif game_state == "advantage":
                PlayAdvantage()
            elif game_state == "disadvantage":
                PlayDisadvantage()
            elif game_state == "player won":
                global wins
                print("YOU WIN!!!!!!!! :DDD")
                wins += 1
                return
            elif game_state == "player lost":
                global losses
                print("u lost womp womp")
                losses += 1
                return
            elif game_state == "player tie":
                global ties
                print("The game ended with a tie.")
                ties += 1
                return
            
        # Choice making time
        print("R - {}, P - {}, S - {}".format(player_hands['R'], player_hands['P'], player_hands['S']))
        print("The AI has {} hand(s)".format(sum(ai_hands.values())))
        ai_choice = GetRandomValidChoice(ai_hands, include_c=False)
        choice = input("What's your move?: ").upper()
    
        while choice not in "RPS":
            print()
            choice = input("Invalid choice, do it right this time.: ").upper()
        print()
        if player_hands[choice] == 0:
            print("You are out of that type!")
            continue
        
        # Get the outcome of the RPS game
        print("The AI chose {}.".format(ai_choice))
        if choice == ai_choice:
            print("Tie. Boring.")
        elif IsWin():
            print("You won! You are now in advantage.")
            ai_hands[ai_choice] -= 1
            game_state = "advantage"
        elif not IsWin():
            print("You lost. You are now in disadvantage.")
            player_hands[choice] -= 1
            game_state = "disadvantage"
            
        # Handle the win state
        IsEndGame()

def PlayAdvantage():
    global choice
    global ai_choice
    global game_state
    
    ai_losing_choice = ai_choice

    while True and game_state != "player lost" and game_state != "player won":
        # Choice making time
        print("R - {}, P - {}, S - {}, C".format(player_hands['R'], player_hands['P'], player_hands['S']))
        print("The AI has {} hand(s)".format(sum(ai_hands.values())))
        choice = input("What's your move (you are in advantage)?: ").upper()
        ai_choice = GetRandomValidChoice(ai_hands, include_c=True)
    
        while choice not in "RPSC":
            print()
            choice = input("Invalid choice, do it right this time.: ").upper()
        print()
        if choice != 'C' and player_hands[choice] == 0:
            print("You are out of that type!")
            continue

        # Get the outcome of the RPS game
        print("The AI chose {}.".format(ai_choice))
        if choice == 'C':
            if ai_choice in "RPS":
                print("Your call failed!")
                player_hands[GetRandomValidChoice(player_hands, include_c=False)] -= 1
                game_state = "neutral"
                return
            elif ai_choice == 'C':
                print("You called their catch!")
                ai_hands[GetRandomValidChoice(ai_hands, include_c=False)] -= 1
                return
        elif choice in "RPS" and ai_choice == 'C':
            print("They've caught your hand!")
            player_hands[choice] -= 1
            ai_hands[choice] += 1
            game_state = "neutral"
            return
        elif choice == ai_choice or IsWin():
            print("You won!")
            ai_hands[ai_choice] -= 1
        else:
            print("You lost.")
            player_hands[choice] -= 1
            game_state = "neutral"
            return
        
        # Handle the win state
        IsEndGame()

def PlayDisadvantage():
    global choice
    global ai_choice
    global game_state

    losing_choice = choice

    while True:
        # Choice making time
        print("R - {}, P - {}, S - {}, C".format(player_hands['R'], player_hands['P'], player_hands['S']))
        print("The AI has {} hand(s)".format(sum(ai_hands.values())))
        choice = input("What's your move (you are in disadvantage)?: ").upper()
        ai_choice = GetRandomValidChoice(ai_hands)
    
        while choice not in "RPSC":
            print()
            choice = input("Invalid choice, do it right this time.: ").upper()
        print()
        if choice != 'C' and player_hands[choice] == 0:
            print("You are out of that type!")
            continue
    
        # Get the outcome of the RPS game
        print("The AI chose {}.".format(ai_choice))
        if choice == 'C': 
            if ai_choice in "RPS":
                print("You've caught their hand!")
                ai_hands[ai_choice] -= 1
                player_hands[ai_choice] += 1
                game_state = "neutral"
                return
            elif ai_choice == 'C':
                print("They called your catch.")
                player_hands[GetRandomValidChoice(player_hands, include_c=False)] -= 1
        elif IsWin():
            print("You won!")
            ai_hands[ai_choice] -= 1
            game_state = "neutral"
            return
        else:
            print("You lost.")
            player_hands[choice] -= 1
            
        # Handle the win state
        IsEndGame()

def DisplayScores():
    print(f"Wins: {wins} Losses: {losses} Ties: {ties}")
    print()

while True:
    choice = Menu()

    print()
    if choice == 1:
        Play()
        game_state = "neutral"
        with open("scores", 'w') as scores:
            scores.write(f"{wins} {losses} {ties}")
    elif choice == 2:
        Info()
    elif choice == 3:
        DisplayScores()
