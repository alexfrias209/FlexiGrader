import random

def save_to_file(tries):
    with open("game_history.txt", "a") as file:
        file.write(str(tries) + "\n")

def display_game_history():
    try:
        with open("game_history.txt", "r") as file:
            game_history = file.readlines()
            if game_history:
                print("Most recently played game took", game_history[-1].strip(), "tries to guess the number.")
            else:
                print("No game history available.")
    except FileNotFoundError:
        print("No game history available.")

def play_game():
    number_to_guess = random.randint(1, 100)
    tries = 0

    print("Welcome to the Number Guessing Game!")
    display_game_history()

    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        tries += 1

        if user_guess == number_to_guess:
            print("Congratulations! You guessed the number in", tries, "tries.")
            save_to_file(tries)
            break
        elif abs(user_guess - number_to_guess) <= 10:
            print("Very hot!")
        elif abs(user_guess - number_to_guess) <= 20:
            print("Hot!")
        elif abs(user_guess - number_to_guess) <= 30:
            print("Warm.")
        else:
            print("Cold.")

if __name__ == "__main__":
    play_game()
