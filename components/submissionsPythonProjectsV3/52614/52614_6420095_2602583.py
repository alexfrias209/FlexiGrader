import random 

print('Welcome to Tic-Tac-Toe!')
print('-----------------------')
print('Latest scores are...')
leaderboard = open('52614_6420096_8271513.txt', 'r')
lines = leaderboard.readlines()
count = 0
for line in lines:
  count += 1
  print('victim {}: {}'.format(count, line.strip())) #this basically prints out a leaderboard of the recent players and scores
#also probably couldve limited it to just be a top 10 thing, but realized that i can try to fix it later on
print('-----------------------')
user_name = input('What would you like to be called? ') #simple username input for the score txt file.
print('-----------------------')
print('''Please pick the shape you would like to play as:
      1. I would like to play as O!
      2. I would like to play as X!''')

shape = input('What shape would you like to play as? ')
if shape == '1':
    print('You have chosen the shape O!')
elif shape == '2':
    print('You have chosen the shape X!')
else:
    print('Please type 1 or 2')

print('Thank you for picking your shape! The game will begin soon...')
print('-----------------------')
#defined all these variables and functions to help construct the game later on 
X = 'X'
O = 'O'
possibleNumbers = [1,2,3,4,5,6,7,8,9] #list of nums the ai and the player can use 
gameBoard = [[1,2,3], [4,5,6], [7,8,9]] #nums used to construct the 2d array (the board)
best_moves = [5, 1, 3, 7, 9] #list of nums that makes the ai focus on these first before going back to possible numbers
rows = 3
cols = 3
def printGameBoard():
  for x in range(rows):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(cols):
      print("", gameBoard[x][y], end=" |")
  print("\n+---+---+---+")

def shapeH(human):
   if shape == '1':
      human = O
   else:
      human = X
   return human

def shapeC(computer):
   if shape == '1':
      computer = X
   else:
      computer = O
   return computer
#shape functions here are to give the choice of what the player wants to be 

human = ''
computer = ''

shapeH(human)
shapeC(computer)
hooman = shapeH(human)
compooter = shapeC(computer)
#to identify a winner for later 

def editBoard(num, turn):
  num -= 1
  if(num == 0):
    gameBoard[0][0] = turn
  elif(num == 1):
    gameBoard[0][1] = turn
  elif(num == 2):
    gameBoard[0][2] = turn
  elif(num == 3):
    gameBoard[1][0] = turn
  elif(num == 4):
    gameBoard[1][1] = turn
  elif(num == 5):
    gameBoard[1][2] = turn
  elif(num == 6):
    gameBoard[2][0] = turn
  elif(num == 7):
    gameBoard[2][1] = turn
  elif(num == 8):
    gameBoard[2][2] = turn
#transforms the spot on the board into the shape that is correlated with the turn, e.g. 00 on the array is the first block, if
#turn is = human which is equal to X, the 00 spot on the array becomes an X.

def check(gameBoard):
  if(gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X'):
    print("X has won!")
    return 'X'
  elif(gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O'):
    print("O has won!")
    return 'O'
  elif(gameBoard[1][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[1][2] == 'X'):
    print("X has won!")
    return 'X'
  elif(gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O'):
    print("O has won!")
    return 'O'
  elif(gameBoard[2][0] == 'X' and gameBoard[2][1] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return 'X'
  elif(gameBoard[2][0] == 'O' and gameBoard[2][1] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")
    return 'O'
  
  if(gameBoard[0][0] == 'X' and gameBoard[1][0] == 'X' and gameBoard[2][0] == 'X'):
    print("X has won!")
    return 'X'
  elif(gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O'):
    print("O has won!")
    return 'O'
  elif(gameBoard[0][1] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][1] == 'X'):
    print("X has won!")
    return 'X'
  elif(gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O'):
    print("O has won!")
    return 'O'
  elif(gameBoard[0][2] == 'X' and gameBoard[1][2] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return 'X'
  elif(gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")
    return 'O'
  
  elif(gameBoard[0][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return 'X'
  elif(gameBoard[0][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")  
    return 'O'
  elif(gameBoard[0][2] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][0] == 'X'):
    print("X has won!")  
    return 'X'
  elif(gameBoard[0][2] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][0] == 'O'):
    print("O has won!") 
    return 'O'
  else:
     return 'not over'
#just hardcoded the winner check on tic-tac-toe, plan to change it into a function in the future

leaveloop = False
turncounter = 0
#leaveloop lets me continue running the game until i can make a point where it doesnt continue
#turncounter was used for score (shown later) and to have it be a hardstop when it hits 9 (a tie)

while(leaveloop == False):
   if (turncounter % 2 == 0):
      printGameBoard()
      spot_picked = int(input('\nPlease choose a number [1-9]: '))
      if(spot_picked >= 1 or spot_picked <= 9):
         editBoard(spot_picked, shapeH(human))
         if(spot_picked in best_moves):
           best_moves.remove(spot_picked) #removes the human choice from the list so the AI cant pick it
         possibleNumbers.remove(spot_picked)
         turncounter += 1
      else:
         print('Not a valid input. Please try again.')
   else:
      while(True):
          if len(best_moves) == 0: #if the ai exhausted the corners and center move list, this makes it go back to possible nums
           computer_choice = random.choice(possibleNumbers)
           print('\nThe all-mighty computer chose: ', computer_choice)
           if(computer_choice in possibleNumbers):
              editBoard(computer_choice, shapeC(computer))
              possibleNumbers.remove(computer_choice)
              turncounter += 1 
              break
          computer_choice = random.choice(best_moves)
          print('\nYou fool, the superiority of AI has chosen: ', computer_choice)
          if(computer_choice in possibleNumbers):
           editBoard(computer_choice, shapeC(computer))
           possibleNumbers.remove(computer_choice)
           best_moves.remove(computer_choice)
           turncounter += 1
           break #returns to player turn 
         
   winner = check(gameBoard)
   if (winner != 'not over'):
    printGameBoard() #to showcase the endboard and so the player can see who won/lost
    print('Thanks for playing!')
    break
   elif (turncounter == 9):
    printGameBoard()
    break

#if it's a tie, winner = 'not over'

if (hooman == winner):
  print('you beat the computer!!')
elif (turncounter == 9):
  print('looks like ya tied...somehow')
else:
  print('bro how do you lose')

score = 10 - turncounter


score_file = open('52614_6420096_8271513.txt', 'a')

score_file.write(user_name + ' ' + str(score) + '\n')

score_file.close()

