import random


def initialize_game():
    word_bank = ['computer', 'merced', 'apartment', 'water', 'bottle', 'python', 'integral', 'gamer', 'engineering']
    word = random.choice(word_bank).lower()
    blanks = ["_" if letter.isalpha() else letter for letter in word]
    missed_letters = []
    remaining_chances = 10

    
    print('Play Hangman!!! You get 10 chances to guess the word correctly!')
    

    while remaining_chances > 0:
        print('Word: ' + ' '.join(blanks))
        guess = input('Guess: ').lower()

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    blanks[i] = guess

            if "_" not in blanks:
                print("Word: " + " ".join(blanks))
                print("You win!!! That's the word!")
                break
        else:
            remaining_chances -= 1
            print('Wrong letter! You only have', remaining_chances, 'chances left!')
            missed_letters.append(guess)
            print("Misses: " + ", ".join(missed_letters))

    if remaining_chances == 0:
        print("The word is:", word)


if __name__ == "__main__":
    initialize_game()

