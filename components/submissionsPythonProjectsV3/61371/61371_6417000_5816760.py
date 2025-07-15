import random
import os  # To interact with my operating system

# The amount of chips I set the player to have
player_chips = 100

# The name of the file when the game ends
output_filename = "blackjack_results.txt"

# All of the card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Had to make it so K, J, Q equal 10 and A equals 11
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
# Since there are 4 suits, the entire deck is multiplied by 4

# Code that calculates the value of the hand
# Counting the number of times the charatcer (A) appears in the string
def calculate_hand_value(hand):
    value = sum(card_values[card] for card in hand)
    num_aces = hand.count('A')

    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value
# The value for the Ace card
# ending the function

# This code will deal a card
def deal_card():
    return deck.pop(random.randint(0, len(deck) - 1))
# Removing and returing certain elements from my provided list
# Returing an integer number randomly selected from the range I put
# Code that displays the player's and dealer's hands
def display_hands(player_hand, dealer_hand):
    print("\nYour Hand:", player_hand, "| Value:", calculate_hand_value(player_hand))
    print("Dealer's Hand:", [dealer_hand[0], 'X'])

# Before the main game loop, open the file in write mode
with open(output_filename, 'w') as file:
    file.write("Blackjack Game Results\n")

# Main game loop with opening file function
while player_chips > 0:
    print("You have", player_chips, "chips left.")
    bet = int(input("Please place your bets (1-" + str(player_chips) + "): "))
    if bet < 1 or bet > player_chips:
        print("Invalid bet. Please place a valid bet.")
        continue
# Converting values into string form str
# Forcing the loop to continue going to the next iteration
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    print("\nDealing the cards...")
    display_hands(player_hand, dealer_hand)

    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to Hit or Stand? ").lower()
        if action == 'hit':
            player_hand.append(deal_card())
            display_hands(player_hand, dealer_hand)
        elif action == 'stand':
            break
        else:
            print("Invalid response. Please enter 'hit' or 'stand'.")
# append will allow me to add terms to the list I gave
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    display_hands(player_hand, dealer_hand)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > 21:
        print("Player busts. Dealer wins!")
        player_chips -= bet
    elif dealer_value > 21:
        print("Dealer busts. Player wins!")
        player_chips += bet
    elif player_value > dealer_value:
        print("Player wins!")
        player_chips += bet
    elif player_value < dealer_value:
        print("Dealer wins!")
        player_chips -= bet
    else:
        print("It's a tie!")
# Function determining who wins

    with open(output_filename, 'a') as file:
        file.write(f"Player's Hand: {player_hand} | Value: {player_value}\n")
        file.write(f"Dealer's Hand: {dealer_hand} | Value: {dealer_value}\n")
        if player_value > 21:
            file.write("Player busts. Dealer wins!\n")
        elif dealer_value > 21:
            file.write("Dealer busts. Player wins!\n")
        elif player_value > dealer_value:
            file.write("Player wins!\n")
        elif player_value < dealer_value:
            file.write("Dealer wins!\n")
        else:
            file.write("It's a tie!\n")
            # writing the game results into a file

    if player_chips == 0:
        print("\nHaha! You've run out of chips! Better luck next time. GAME OVER")
        break

    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != 'yes':
        break

# After the game loop, writing the final chip count
with open(output_filename, 'a') as file:
    file.write(f"Final chip count: {player_chips}\n")

print("Thank you for playing! Your final chip count is", player_chips)
