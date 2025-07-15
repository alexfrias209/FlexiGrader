#Welcome to my project*


file= open("55316_6422308_449932.txt","r")

#This print is a test to see if my values are being printed as expected I will be continuing this with all the rest of my hands
#print(file.readlines())

x = file.readlines()
y=[]

for i in x:
    y.append(i [:-1].split(' '))

print(y)


#This is the one single line breakdown but the for loop i set makes it so it runs for all lines
#y = x[1][:-1].split(' ')



#Play hand CHoice

def hand_selection(player_number, hands):
    while True:
        choice = input(f"Player {player_number}, select a hand (1 or 2): ")
        if choice in ["1", "2"]:
            return hands[int(choice) - 1]



First_hand= y[0][:5]

#print(First_hand)

Second_hand= y[0][5:10]

#print(Second_hand)

#General_1sthand = y[][5]
#print(General_1sthand)

#General_2ndhand = y[][5:10]
#print(General_2ndhand)


#Win Counter
player1_wins = 0
player2_wins = 0

       
# Defining all the possible hands based off of the given cards


#This section gives value to the string
def value(v):
    if v == 'A':
        return 14
    if v == 'K':
        return 13
    if v == 'Q':
        return 12
    if v == 'J':
        return 11
    if v == '10':
        return 10
    if v == 'T':
        return 10
    if v == '9':
        return 9
    if v == '8':
        return 8
    if v == '7':
        return 7
    if v == '6':
        return 6
    if v == '5':
        return 5
    if v == '4':
        return 4
    if v == '3':
        return 3
    if v == '2':
        return 2
    if v == '1':
        return 1

#hand_deteermination just runs the hand options that are definded later on to be called upon. It has the order ranking so you can get the first one.    
def hand_determination(hand):
    if straight(hand) and flush(hand):
        return "Straight Flush"
    if fourofakind(hand):
        return "Four of a Kind"
    if full_house(hand):
        return "Full House"
    if flush(hand):
        return "Flush"
    if straight(hand):
        return "Straight"
    if three_of_a_kind(hand):
        return "Three of a Kind"
    if two_pair(hand):
        return "Two Pair"
    return "High Card"

with open("55316_6422308_449932.txt", "r") as file:
    hands = file.readlines()

for i in range(len(hands)):
    hands[i] = hands[i].strip().split()

    

#Defining all of the possible hand combinations in a poker set#

#Defining the Flush we use the last part of the combinations to gather the information on Card type followed by trying to make sure that the all of the pairs in the hand match the initial first letter    
def flush(hand):
    suit = hand[0][-1]
    return all(card[-1] == suit for card in hand)


# Defining Straight we define cardvalues with the first character in each pair. once you get that character we sort all of the card values in an acending list becaue of our sort command. 
#After we begin running our look in the order it is and run the test seeing if we have a accending order of plus or minus one if this isnt true then its returned with false.
def straight(hand):
    cardvalues = [value(card[:-1]) for card in hand]
    cardvalues.sort()
    for i in range(1, len(cardvalues)):
        if cardvalues[i] != cardvalues[i - 1] + 1:
            return False
    return True

# in this case we have a counts variable set up where the counter looks specifically at the first string in the hands
#after returning the max(counts.values())== 4 means that once it regonizes the first cards value it will take values for all other cards in the hands and see if there equal a maximum of 4 times
def fourofakind(hand):
    counts = Counter(card[:-1] for card in hand)
    return max(counts.values()) == 4

#three o a kind the counter will be counting the occurances of the same first string for all pairs and begin to take note if they are the same
#if the counter determines that there are three reoccurances of the same number in this case and a maxiumum number of 3 then it will determine its a three of a kind pair.
def three_of_a_kind(hand):
    counts = Counter(card[:-1] for card in hand)
    return max(counts.values()) == 3

#similar to how three of a kind works this time the counder counts the occurances of number groups them into pairing with the counts.items.
#by ranking the cards it sees there are two unique pairs that are maid and so then it lets us know that its two pairs.
#two pairs 
def two_pair(hand):
    counts = Counter(card[:-1] for card in hand)
    pairranks = [card for card, count in counts.items() if count == 2]
    return len(pairranks) == 2

#full house just uses the concept of three of a kind and check again if we have three of a kind and uses the idea of a pair being 2 of a kind and if both are satisfied then you
#have a full house. RAnks assigns the value of a card followed then by doing same processes of counting taking the number of occurences for specfic numbers
#followed by the len checked the rank and count coming out with a pair of three being same and another pair equaling 2 for the stand alone pair. To satisfy full house it need the three of a kind and a pair.
def full_house(hand):
    ranks = [value(card[:-1]) for card in hand]
    counts = Counter(ranks)
    return len([rank for rank, count in counts.items() if count == 3]) == 1 and len([rank for rank, count in counts.items() if count == 2]) == 1
 
from collections import Counter

#General hand comparison
def compare_hands(hand1, hand2):
    # Define hand rankings
    hand_rankings = ["High Card", "One Pair", "Two Pair", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush"]

    # Define the rank of each hand
    rank1 = hand_rankings.index(hand_determination(hand1))
    rank2 = hand_rankings.index(hand_determination(hand2))

    # Compare hand ranks
    if rank1 < rank2:
        return "Player 1"
    elif rank1 > rank2:
        return "Player 2"
    else:
        # If hands have the same rank, compare card values
        values1 = [value(card[:-1]) for card in hand1]
        values2 = [value(card[:-1]) for card in hand2]

        # Sort card values in descending order
        values1.sort(reverse=True)
        values2.sort(reverse=True)

        # Compare each card value
        for v1, v2 in zip(values1, values2):
            if v1 < v2:
                return "Player 2"
            elif v1 > v2:
                return "Player 1"

    return "Tie"


#This will be the opening section gathering what card selection we will give the person based off of their choice in Player
print('Welcome to poker hand Reader', 'Developed By Angel Martinez')

#Section for Winning Counter#

#Welcome to my project

import random
from collections import Counter

import random
from collections import Counter
#In this section I am beginning to read the new lines. So previoulsy above I opened the file and compessed the lines on the shell. I began lookingf at ways to test that the code was reading lines
#above when it was reading lines it predetermined the lines and wouldnt continue to read lines. Now With initialize_hands I am setting the first 5 pairs togteher for hand one and second 5 for hand two and making it repeat this  
# Define the function to read the data file and assign hands
def initialize_hands():
    with open("55316_6422308_449932.txt", "r") as file:
        lines = file.readlines()

    hands = []
    for line in lines:
        cards = line.strip().split()
        hand1 = cards[:5]
        hand2 = cards[5:]
        hands.append([hand1, hand2])

    return hands

# Define the function to select a hand for a player
def hand_selection(player_number, hands):
    while True:
        choice = input(f"Player {player_number}, select a hand (1 or 2): ")
        if choice in ["1", "2"]:
            return hands[int(choice) - 1]

# Initialize hands at the beginning of the game
hands = initialize_hands()

# Start the game loop
play_again = "yes"

while play_again.lower() == "yes":
    # Section for Winning Counter
    player1_wins = 0
    player2_wins = 0

    for hand_pair in hands:
        player1_hand = hand_pair[0]
        player2_hand = hand_pair[1]

        # Display the hands selected by both players
        print("Player 1 hand:", player1_hand)
        print("Player 2 hand:", player2_hand)

        result = compare_hands(player1_hand, player2_hand)

        # Determine the winner and update win counters.
        if result == "Player 1":
            player1_wins += 1
        elif result == "Player 2":
            player2_wins += 1

        print(f"Player 1 wins: {player1_wins}, Player 2 wins: {player2_wins}")
        play_again = input("Do you want to play again? (Yes or No): ")

    # Initialize new hands for the next round
    hands = initialize_hands()

print("Thank you for playing!")
