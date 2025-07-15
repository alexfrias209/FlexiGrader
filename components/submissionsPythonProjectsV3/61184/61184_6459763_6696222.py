import random

def initialize_grid(grid_size):
    return [[0] * grid_size for _ in range(grid_size)]

def place_battleship(grid):
    battleship_row = random.randint(0, len(grid) - 1)
    battleship_col = random.randint(0, len(grid) - 1)
    grid[battleship_row][battleship_col] = 1
    return (battleship_row, battleship_col)

def display_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def play_game(grid_size):
    grid = initialize_grid(grid_size)
    battleship_location = place_battleship(grid)
    attempts = grid_size  # Attempts match the ocean size

    while attempts > 0:
        print("\nGuess the Battleship's location!")
        display_grid(grid)

        try:
            guess_row = int(input(f"Enter the row (0-{grid_size - 1}): "))
            guess_col = int(input(f"Enter the column (0-{grid_size - 1}): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if 0 <= guess_row < grid_size and 0 <= guess_col < grid_size:
            if (guess_row, guess_col) == battleship_location:
                print("Congratulations! You sunk the battleship!")
                grid[guess_row][guess_col] = 'X'
                display_grid(grid)
                return True
            else:
                print("Missed! Try again.")
                attempts -= 1
        else:
            print(f"Invalid input. Row and column must be between 0 and {grid_size - 1}.")

    print("\nGame Over! You ran out of attempts.")
    print(f"The battleship was located at row {battleship_location[0]} and column {battleship_location[1]}.")
    return False

def update_score(score_file, won):
    try:
        with open(score_file, 'r') as file:
            score = int(file.read())
    except FileNotFoundError:
        score = 0

    if won:
        score += 1

    with open(score_file, 'w') as file:
        file.write(str(score)

    print(f"Your score: {score}")

def main():
    grid_size = 4  # You can adjust the ocean size here
    SCORE_FILE = "battleship_scores.txt"
    
    print("Welcome to Battleship!")
    play_again = True

    while play_again:
        won = play_game(grid_size)
        update_score(SCORE_FILE, won)
        play_again = input("Do you want to play again? (yes/no): ").lower() == 'yes'

if __name__ == "__main":
    main()
