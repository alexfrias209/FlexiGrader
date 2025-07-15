import random

# Function to choose a random word from a file
def choose_random_word(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
    return random.choice(words).strip()

# Function to display the current state of the word with hidden letters
# Also shows the user what letters are used and how many letters are left.
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to display the hangman based on the number of incorrect attempts
def display_hangman(hangman_state):
    hangman_parts = [
        """
           _______
          |       |
                  |
                  |
                  |
                  |
        """,
        """
           _______
          |       |
          O       |
                  |
                  |
                  |
        """,
        """
           _______
          |       |
          O       |
          |       |
                  |
                  |
        """,
        """
           _______
          |       |
          O       |
         /|       |
                  |
                  |
        """,
        """
           _______
          |       |
          O       |
         /|\      |
                  |
                  |
        """,
        """
           _______
          |       |
          O       |
         /|\      |
         /        |
                  |
        """,
        """
           _______
          |       |
          O       |
         /|\      |
         / \      |
                  |
        """
    ]
    print(hangman_parts[hangman_state])

# Main Hangman game
def hangman_game():
    # Choose a random word from file random_words file
    word = choose_random_word("69427_6422405_3545061.txt")
    guessed_letters = []
    hangman_state = 0  # Current hangman state

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print("Only letters no symbols.")

    while True:
        display_hangman(hangman_state)
        word_display = display_word(word, guessed_letters)
        print(word_display)

        if word_display == word:
            print("Congratulations! You've won. The word was:", word)
            break
        
        # Max hangman state and max incorrect guess allowed
        if hangman_state == 6:
            print("Oh no! You've been hanged! The word was:", word)
            break

        guess = input("Guess a letter: ").lower()
        
        #checks if only one letter is entered
        # guess.isalpha() checks if symbols are entered and lets user know to enter a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # If letter has been guessed or not
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
            
        # Shows how many attempts are left
        else:
            guessed_letters.append(guess)
            hangman_state += 1
            print("Incorrect guess. You have", 6 - hangman_state, "attempts left.")

if __name__ == "__main__":
    hangman_game()
