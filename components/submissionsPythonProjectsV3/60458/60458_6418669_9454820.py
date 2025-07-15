from PIL import Image

print('Welcome to "Can You Spot Which Logo is Correct?" Quiz!')
print("My name is J'marki McPherson and I'm the developer of this game. This game entails looking at two pictures of the same brand logo, and guessing which one is correct.")

max_rounds = 3
round_number = 1

print("You're gonna start off by doing easy, then moving onto medium, and finally hard.")

start_game = input("Are you ready to begin (Yes, No)?")

if start_game == "Yes":
    print("Let's begin!")
else:
    print("Come back when you're ready!")
    exit(0)
correct_answers =  0

image_path1 = r"Apple_image.jpg" # Gives the computer the path to the Jpg
img1 = Image.open(image_path1)
img1.show()
player_guess = input(f'\nRound {round_number}/{max_rounds}:Guess the correct logo *Right or Left):') # User is able to see what round number they're on

if (player_guess == 'Right'):
    print("Correct! Great job!")
    correct_answers += 1
    round_number += 1
else:
    print(f"The correct logo was:", 'Right')
    round_number += 1


image_path2 = r"Pepsi_image.jpg"
img2 = Image.open(image_path2)
img2.show()
player_guess = input(f'\nRound {round_number}/{max_rounds}:Guess the correct logo (Right or Left):')

if (player_guess == 'Right'):
    print("Correct! Great job!")
    correct_answers += 1 
    round_number += 1
else:
    print(f"The correct logo was:", 'Right')
    round_number += 1

image_path3 = r"BK_image.jpg"
img3 = Image.open(image_path3)
img3.show()
player_guess = input(f'\nRound {round_number}/{max_rounds}:Guess the correct logo (Right or Left):') 

if (player_guess == 'Right'):
    print("Correct! Great job!")
    correct_answers += 1
else:
    print(f"The correct logo was:", 'Right')

print(f"Game over! You got {correct_answers} out of {max_rounds} correct.")