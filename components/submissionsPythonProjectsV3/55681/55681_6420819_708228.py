import random
import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Initialize Pygame fonts
pygame.font.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define colors
WHITE = (255, 255, 255)

# Function to roll the dice and return the result
def roll_dice():
    return random.randint(1, 6)

# Function to mirror an image horizontally
def mirror_image(image):
    return pygame.transform.flip(image, True, False)

# Assign values to dice images based on filenames
dice_images = {}
for i in range(1, 7):
    image_filename = os.path.join("dice_images", f"dice_{i}.png")
    dice_images[i] = pygame.image.load(image_filename)

# Initialize Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dice Game")

# Create font for displaying results and instructions
font = pygame.font.SysFont(None, 36)

# Initialize variables for computer and user wins
computer_wins = 0
user_wins = 0

# Initialize result_text variable
result_text = ""

# Initialize a flag to track the game state
game_over = False

# Initialize goal_result variable
goal_result = 0

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    # Reset the game state if it's over
                    game_over = False
                    result_text = ""
                    goal_result = 0

                if goal_result == 0:
                    # If goal_result is not set, store the first roll result as the goal result
                    user_result = roll_dice()
                    computer_result = roll_dice()

                    roll_result = user_result + computer_result

                    dice_user = dice_images[user_result]
                    dice_computer = dice_images[computer_result]

                    if roll_result == 7 or roll_result == 11:
                        result_text = "Congratulations! You win!"
                        user_wins += 1
                        game_over = True
                    elif roll_result == 2 or roll_result == 3:
                        result_text = "Computer wins. Better luck next time!"
                        computer_wins += 1
                        game_over = True
                    else:
                        goal_result = roll_result  # Set goal result here

                    screen.fill(WHITE)
                    screen.blit(dice_user, (250, 250))  # Adjust the positions as needed
                    screen.blit(dice_computer, (450, 250))  # Adjust the positions as needed
                    pygame.display.flip()
                    pygame.time.delay(1000)
                else:
                    # If goal_result is already set, continue the game
                    user_result = roll_dice()
                    computer_result = roll_dice()

                    roll_result = user_result + computer_result

                    dice_user = dice_images[user_result]
                    dice_computer = dice_images[computer_result]

                    if roll_result == goal_result:
                        result_text = "Congratulations! You win!"
                        user_wins += 1
                        game_over = True
                    elif roll_result == 7:
                        result_text = "Computer wins. Better luck next time!"
                        computer_wins += 1
                        game_over = True

                    screen.fill(WHITE)
                    screen.blit(dice_user, (250, 250))  # Adjust the positions as needed
                    screen.blit(dice_computer, (450, 250))  # Adjust the positions as needed
                    pygame.display.flip()
                    pygame.time.delay(1000)

            elif event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(WHITE)  # Clear the screen

    text = font.render(f"Computer Wins: {computer_wins}  User Wins: {user_wins}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    if goal_result != 0:
        text_goal = font.render(f"Goal Result: {goal_result}", True, (0, 0, 0))
        screen.blit(text_goal, (250, 400))

    text_roll = font.render("Press 'Space' to roll the dice", True, (0, 0, 0))
    screen.blit(text_roll, (300, 500))

    if not game_over:
        text_exit = font.render("Press 'Escape' to exit", True, (0, 0, 0))
        screen.blit(text_exit, (10, 500))

    result_display = font.render(result_text, True, (0, 0, 0))
    screen.blit(result_display, (250, 450))

    pygame.display.flip()

pygame.quit()
sys.exit()
