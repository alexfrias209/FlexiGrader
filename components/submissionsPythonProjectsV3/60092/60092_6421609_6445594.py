import random #imports an external library for randomness so that the code can randomize the bullets in the chamber. 
#I started off the code with this message, the lore behind the message is that WW3 is going on and you are a soldier captured by the PLA.
print("You have been captured by the PLA. Welcome to Russian Roulette.")


def russian_roulette(numBullets):
    chambers = [0] * (6 - numBullets) + [1] * numBullets #Creates a list that shows which chamber has the bullet, and which chambers do not.
    random.shuffle(chambers) #Shuffles the bullets in the chamber, [1,1,0,0,0,0] -> [0,1,0,1,0,0]

    spins = 0  # Creates the spin count
    while chambers:
        spins += 1
        input("Here you go. Pull the trigger. (Press enter)") #This statement is made by the soldier who is holding you prisoner
        firedChamber = chambers.pop()
        if firedChamber == 1:
            print(f"Bang! You have shot yourself after {spins} spins. Game over.") #Once you shoot yourself, it tells you how many spins you lasted.
            return spins

def save_score(spins): #Creates function to save scores to the file "russian_roulette_scores.txt"
    with open("60092_6421610_9187736.txt", "a") as file:
        file.write(f"Spins: {spins}\n")

def display_scores(): #Creates function to display previous scores
    try:
        with open("60092_6421610_9187736.txt", "r") as file:
            scores = file.read()
            if scores:
                print("Previous scores:")
                print(scores)
            else:
                print("No previous scores found.")
    except FileNotFoundError:
        print("No previous scores found.") #Creates display for the event that no scores have been recorded yet.

while True:
    display_scores() 

    numBullets = int(input("How many bullets would you like to play with? ")) 
    if numBullets < 1 or numBullets > 6:
        print("This revolver only holds 6 rounds.")
        continue

    score = russian_roulette(numBullets)
    save_score(score)

    play_again = input("Spin again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("You have been shot anyway. Nobody escapes the PLA.\n")
        print("Here are the final scores.") #Once the game is ended, a final list of scores is displayed
        open("60092_6421610_9187736.txt", "r")
        break
