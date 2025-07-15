import random

values = list(range(1, 13))
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def generate_cards(values, suit):
    deck = [Card(value, suit) for value in values for suit in suits]
    return deck

standard_deck = generate_cards(values, suits)

num_decks = 1

blackjack_deck = standard_deck * num_decks

for card in blackjack_deck:
    print(f"{card.value} of {card.suit}")

card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

def blackjack():
    user_hand = [draw_card() for _ in range(2)]
    dealer_hand = [draw_card() for _ in range(2)]

    print(f'User has: {user_hand}')
    print(f'Dealer has: {dealer_hand}')
    
    continue_game = True
    user_total = sum([card_values[card] for card in user_hand])
    
    while continue_game and user_total < 21:
        drawing = input("Would you like to draw another card (y/n): ").lower()
        
        if drawing == 'y':
            user_card = draw_card()
            user_hand.append(user_card)
            user_total += card_values[user_card]

            
            aces = [card for card in user_hand if card == 'A']
            while user_total > 21 and aces:
                user_total -= 10
                aces.pop()  
                
            print(f'User now has: {user_hand}')
            print(f'Dealer has: {dealer_hand}')
        else:
            continue_game = False        

    dealer_draw(dealer_hand)

    print("~~~~~~~~~~~~~~~~~ Final results ~~~~~~~~~~~~~~~~~")
    print(f"User has {user_hand} for a total of {user_total}")
    dealer_total = sum([card_values[card] for card in dealer_hand])
    print(f"Dealer has {dealer_hand} for a total of {dealer_total}")

    if user_total > 21:
        print("User busts! Dealer wins")
    elif user_total == dealer_total:
        print("Draw")
    elif dealer_total > user_total and dealer_total <= 21:
        print("Dealer wins")
    else:
        print("User wins")

def draw_card():
    return random.choice(list(card_values.keys()))

def dealer_draw(dealer_hand):
    while sum([card_values[card] for card in dealer_hand]) < 17:
        dealer_card = draw_card()
        dealer_hand.append(dealer_card)

print('____________________________________________________________________')
print("Welcome to Blackjack")
print("Blackjack is a card game where the user goes against the dealer.")
print("Your goal is to draw cards to get closest to 21 points,")
print("however, you don't want to go above 21 points because you will lose!")

play_game = True
while play_game:
    blackjack()
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        play_game = False
        print("Goodbye")
