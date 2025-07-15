import random

# Function to display the player's score and the dealer's score at the beginning of the game
def display_score(player_score, dealer_score):
    try:
        with open("scores.txt", "r") as file:
            score = int(file.read())
            print(f"Your current score is: {score}")
    except FileNotFoundError:
        print("Welcome to Blackjack!")

    print(f"Dealer's score is: {dealer_score}")

# Function to update the score in the text file
def update_score(score):
    with open("scores.txt", "w") as file:
        file.write(str(score))

# Function to map card values and suits to their names
def get_card_name(card):
    card_names = {
        1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"
    }
    card_suits = {
        1: "Hearts", 2: "Diamonds", 3: "Clubs", 4: "Spades"
    }
    value, suit = card
    return f"{card_names[value]} of {card_suits[suit]}"

# Function to calculate the hand total
def hand_total(hand):
    total = sum(card[0] for card in hand)
    aces = sum(1 for card in hand if card[0] == 1)
    return total, aces

# Function to start the Blackjack game
def blackjack_game():
    player_score = 0
    dealer_score = 0

    while True:
        display_score(player_score, dealer_score)
        print("\nLet's play Blackjack!")

        player_hand = []
        dealer_hand = []

        # Initial deal
        player_hand.append((random.randint(1, 13), random.randint(1, 4)))
        dealer_hand.append((random.randint(1, 13), random.randint(1, 4)))

        # Player's turn
        while True:
            print("Your hand:")
            for card in player_hand:
                print(get_card_name(card))
            total, aces = hand_total(player_hand)
            print(f"Total: {total} (Ace count: {aces})")

            action = input("Do you want to hit or stand? (hit/stand): ")

            if action.lower() == "hit":
                player_hand.append((random.randint(1, 13), random.randint(1, 4)))
                total, aces = hand_total(player_hand)
                if total > 21:
                    if aces > 0:
                        choice = input("You're over 21! Do you want to count an Ace as 1 or 11? (1/11): ")
                        if choice == "1":
                            player_hand = [(1, card[1]) if card[0] == 1 else card for card in player_hand]
                            total, aces = hand_total(player_hand)
                            if total <= 21:
                                print(f"You've adjusted the Ace! New total: {total}")
                            else:
                                print("You're still over 21. Dealer wins this round.")
                                dealer_score += 1
                                break
                        else:
                            player_hand = [(11, card[1]) if card[0] == 1 else card for card in player_hand]
                            total, aces = hand_total(player_hand)
                            print(f"You've adjusted the Ace! New total: {total}")
                    else:
                        print("You bust! Dealer wins this round.")
                        dealer_score += 1
                        break
                elif total == 21:
                    print("You got 21!")
                    player_score += 1
                    break
            else:
                break

        # Dealer's turn
        while hand_total(dealer_hand)[0] < 17:
            dealer_hand.append((random.randint(1, 13), random.randint(1, 4)))

        print("Dealer's hand:")
        for card in dealer_hand:
            print(get_card_name(card))
        dealer_total, _ = hand_total(dealer_hand)
        print(f"Total: {dealer_total}")

        player_total, _ = hand_total(player_hand)
        if player_total <= 21:
            if dealer_total > 21 or player_total > dealer_total:
                print("You win this round!")
                player_score += 1
            elif player_total == dealer_total:
                print("It's a tie!")
            else:
                print("Dealer wins this round!")
                dealer_score += 1
        else:
            print("Dealer wins this round!")
            dealer_score += 1

        update_score(player_score)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

# Starting the game
blackjack_game()
