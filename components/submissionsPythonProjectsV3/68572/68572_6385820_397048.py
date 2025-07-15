from random import randint
import os

if os.path.isfile('68572_6385821_7400501.txt'):
  os.remove("68572_6385821_7400501.txt")
f = open("68572_6385821_7400501.txt", "a")


# Checks total rolls
def check_die(score, die_value, die_number):
  if die_value == die_number:
    return 0
  else:
    return score + die_value


# Roll
def roll(numd, nums):
  total_roll = 0
  for a in range(numd):
    total_roll = total_roll + randint(1, nums)
  return total_roll


# Display scoreboard
def display_scoreboard(player_score, computer_score, file):
  print(f"Your Score: {player_score}")
  print(f"Computer Score: {computer_score}")
  file.write(f"Your Score: {player_score}\n")
  file.write(f"Computer Score: {computer_score}\n")


player_score = 0
computer_score = 0

welcome_message = """
          Simple Dice Game
"""

print(welcome_message)

# Set number of dice
numdice = input("Enter number of dice: ")

numdice = int(numdice)
f.write(f"Number of dice: {numdice}\n")

# Set number of sides on all dice
numsides = input("Enter number of sides the dice will have: ")

numsides = int(numsides)
f.write(f"Number of sides on each die: {numsides}\n")

# Set difficulty level
difficultylevel = input("Enter difficulty level: ")

difficultylevel = int(difficultylevel)
f.write(f"Difficulty level: {difficultylevel}\n")

winscore = numdice * numsides * difficultylevel
f.write(f"Score required to win: {winscore}\n")

print(f"The score required to win is: {winscore}")

# While True loop
while True:
  input(f"Press Enter to roll\n")

  player_die_value = roll(numdice, numsides)
  print(f"Your roll: {player_die_value}")
  f.write(f"Your roll: {player_die_value}\n")

  computer_die_value = roll(numdice, numsides)
  print(f"Computer roll: {computer_die_value}")
  f.write(f"Computer roll: {computer_die_value}\n")

  player_score = check_die(player_score, player_die_value, numdice)
  computer_score = check_die(computer_score, computer_die_value, numdice)

  display_scoreboard(player_score, computer_score, f)

  if (player_score >= winscore) and (computer_score >= winscore) and (
      player_score == computer_score):
    print("Both have reached the winning score. Greater roll wins!")
    while (player_score == computer_score):
      if player_score > computer_score:
        print(f"Winner: You")
        f.write(f"Winner: You\n")
        break
      elif computer_score > player_score:
        print("Winner: Computer")
        f.write(f"Winner: Computer\n")
        break
  elif player_score >= winscore:
    print(f"Winner: You")
    f.write(f"Winner: You\n")
    break
  elif computer_score >= winscore:
    print("Winner: Computer")
    f.write(f"Winner: Computer\n")
    break
