# This is a short text-based adventure that I created.
# A text adventure allows player inputs to influence their movement in a virtual world. Being that this is only a school project it's short,
# but has a few features that are pretty neat and hopefully fun to explore.

# Side note, IReallyLikeCamelCaseSoIWillBeUsingItEverywhereHere

import random # allows for RNG and random responses from lists

global GameOver
GameOver = 0 # The win condition is finding the exit. When they do, this value is set to 1 and the game ends.
global RoomID
RoomID = 0 # RoomID is changed depending on what room the player is in. This lets me keep track of where the player is and allows for backtracking. 
           # Special thanks to my friend Jadan for helping me come up with this method!

# Map (Numbers are RoomID, 5 is the exit)
#   5
#   4
# 2 1 3
#   0

# These are all available player inputs. Maybe there's a more efficient way to do this but oh well this works. Lists were generally
# used instead of dictionaries because they're just lists of possible commands the player can input.
MovementN = ['n','N','north','North','NORTH']
MovementE = ['e','E','East','east','EAST']
MovementS = ['s','S','South','south','SOUTH']
MovementW = ['w','W','West','west','WEST']
LookInput = ['l','L','look','Look','observe','Observe','LOOK']
UseAction = ['use','Use','USE','u','U']
HelpNeeded = ['Help','help','h','H','help!','Help!','HELP']
Leave = ['leave','Leave','go back','back','Go back','Back','return','Return','Exit','exit']

def Tutorial(): # This prints upon player request for help.
    print("\nHELP MENU")
    print("To move, use the cardinal directions (n, e, north, south, and so on.)")
    print("To get a description of the room and what's inside, try \"Look\"")
    print("You can use objects in the room with the \"Use\" input!")

# These sorts of lists are used in order to put a little more life into my program; by choosing a random response from
# possible responses, I avoid the oftentimes robotic-sounding "error" output common with programs faced with erroneous inputs.
def NoInput():
    NoInput = ["Sorry, I don't recognize that input.",
               "Unrecognized input.",
               "Sorry, that's an invalid input.",
               "I don't recognize that input.",
               "I can't recognize that input.",
               "I can't recognize that.",
               "I don't know what that means.",
               "I don't know what that is."]
    print(random.choice(NoInput))

def NoDirection():
    NowhereToGo = ["You can't go that way.",
                   "There's nowhere to go that way.",
                   "You can't phase through walls, you know.",
                   "You can't go that direction.",
                   "Try a different direction."]
    RandomNoDirResponse = random.choice(NowhereToGo)
    print(RandomNoDirResponse)

def NoUse(): # This draws a bunch of responses from the file "NoUseInRoom.txt" and chooses one at random to output.
    with open('66644_6372163_2324875.txt', 'r') as file: # opens the file
        NoUse = file.read().split(';') # Splits the responses and puts them in a list
    RandomUse = random.choice(NoUse) # Draws a random response
    print(RandomUse) # returns the response

# These are the rooms. Each room has a RoomID, which identifies it. The general game code (found near the bottom)
# uses RoomID to determine what code to run, i.e. RoomID = 1 calls Room1 code.
def StartingRoom():
    global RoomID
    print('You are in the starting room.')
    while RoomID == 0:
        PlayerInput = str(input())
        if (PlayerInput in MovementE) or (PlayerInput in MovementS) or (PlayerInput in MovementW):
            NoDirection()
        elif PlayerInput in UseAction:
            NoUse()
        elif PlayerInput in LookInput:
            print("You are in an empty room. A doorway leads into another room to your north.")
        elif PlayerInput in MovementN:
            RoomID = 1
        elif PlayerInput in HelpNeeded:
            Tutorial()
        else:
            NoInput()

def Room1(): # This room has a locked door. The player can only move north if the door has been unbarred.
    global RoomID
    global NorthDoorCondition
    print('You are in the second room.')
    while RoomID == 1:
        PlayerInput = input()
        if PlayerInput in MovementE:
            RoomID = 3
        elif PlayerInput in MovementW:
            RoomID = 2
        elif PlayerInput in MovementS:
            RoomID = 0
        elif (PlayerInput in MovementN) and (NorthDoorCondition == 'open'):
            RoomID = 4
        elif (PlayerInput in MovementN) and (NorthDoorCondition == 'barred'):
            print("The door is locked tight by iron bars that stretch across it. Maybe there's a way to deactivate or retract them nearby...")
        elif PlayerInput in HelpNeeded:
            Tutorial()
        elif PlayerInput in LookInput:
            print(f"You are in a rectangular room. There are doors to your north, east, and west.\nThere is a doorway to your south. The door to your north is {NorthDoorCondition}.")
        elif PlayerInput == 'exit':
            exit()
        elif PlayerInput in UseAction:
            NoUse()
        else:
            NoInput()

def Room2(): # This room has a hidden switch under a waterfall. To interact, players must have seen it with the "look" command. This lever unlocks the path to room 5.
    global RoomID
    global NorthDoorCondition
    global LookedAtWaterfall
    global UsedLever
    print('You are in the west room.')
    while RoomID == 2:
        PlayerInput = input()
        if PlayerInput == 'exit':
            exit()
        elif PlayerInput in UseAction and LookedAtWaterfall and (UsedLever == False):
            print("You pull the lever hidden in the waterfall. The water is cold, but not uncomfortably so.\nYou hear a grating noise, and the bars on the door in the room behind you slide open.")
            UsedLever = True
            NorthDoorCondition = 'open'
        elif PlayerInput in UseAction and (UsedLever == True):
            print("You've pulled the lever in the waterfall already.")
        elif PlayerInput in UseAction and (LookedAtWaterfall == False):
            NoUse()
        elif PlayerInput in LookInput and (LookedAtWaterfall == False):
            print("Upon further inspection, the glint of metal catches your eye from underneath the waterfall.\nThere's a switch of some sort hidden there. You could probably pull it.")
            LookedAtWaterfall = True
        elif (PlayerInput in LookInput) and (LookedAtWaterfall) and (UsedLever):
            print("You are in a room with a small water feature. You've pulled the lever hidden in the water feature.")
        elif (PlayerInput in LookInput) and (LookedAtWaterfall) and (UsedLever == False):
            print("You are in a room with a small water feature. There is a lever hidden underneath the water.")
        elif (PlayerInput in UseAction) and UsedLever:
            print("You've already pulled the lever under the waterfall. There's nothing more to do here.")
        elif (PlayerInput in MovementN) or (PlayerInput in MovementS) or (PlayerInput in MovementW):
            NoDirection()
        elif PlayerInput in MovementE:
            RoomID = 1
        elif PlayerInput in HelpNeeded:
            Tutorial()
        else:
            NoInput()

# It's worth mentioning that while writing the 3rd room, I realized I could have set every single room to be looping while loops
# with the condition being if RoomID matched the room they were in. It probably would have been more efficient to do the other
# two rooms like that, but oh well. I did it for rooms 4 and 5, at least.

def Room3(): # This room has a timer that counts down the longer the player spends in it. If they spend too long, they are eaten by a Grue, which is in reference to a text adventure named Zork.
    global TimeCount
    global GameOver
    global RoomID
    TimeCount = 5
    print("You are in the east room.")
    while TimeCount >= 0:
        PlayerInput = input()
        if PlayerInput in MovementW:
            break
        elif (PlayerInput in MovementN) or (PlayerInput in MovementE) or (PlayerInput in MovementS):
            NoDirection()
        elif PlayerInput in LookInput:
            print("It's a very dark room. There's a table with a piece of paper on it.")
        elif PlayerInput in UseAction:
            print("The letter reads:\n\nIt's day 1. I'm attempting to learn of this...Grue creature.\nWith luck, I will be able to communicate, perhaps even befriend it--\n(The rest of the page is a scrawled line.)")
        elif PlayerInput == "exit":
            exit()
        elif PlayerInput in HelpNeeded:
            Tutorial()
        else:
            NoInput()
        if TimeCount == 5:
            print('Something lurks in the darkness here.')
        elif TimeCount == 4:
            print("You hear scrapings in the abyss. Something grows near.")
        elif TimeCount == 3:
            print("It is dark. Something wicked this way comes.")
        elif TimeCount == 2:
            print("You remember the phrase: \"It is dark. You are likely to be eaten by a grue.\"")
        elif TimeCount == 1:
            print(f"Careful, {PlayerName}. It draws ever closer.")
        TimeCount -= 1
    if TimeCount < 0:
        print("Something climbs from the darkness. You're grabbed by the ankle and dragged into the abyss and eaten alive.\n")
        print(f"=+=+=+=+=+= GAME OVER! =+=+=+=+=+=\nGood effort, {PlayerName}, but something tells me you could've gone further.\nI hope you enjoyed this little project of mine!\n")
        GameOver = 1
    else:
        RoomID = 1

def Room4():
    global RoomID
    global LookedAtNote
    global Padlock
    global ExitDoor
    print("You are in the final room. The exit is near...")
    while RoomID == 4:
        PlayerInput = input()
        if PlayerInput in MovementS:
            RoomID = 1
        elif (PlayerInput in MovementE) or (PlayerInput in MovementW):
            NoDirection()
        elif (PlayerInput in MovementN) and (ExitDoor == 'unlocked'):
            RoomID = 5
        elif (PlayerInput in MovementN) and (ExitDoor == 'locked with a padlock'):
            print('The north door is locked with a four-digit combination lock.')
        elif (PlayerInput in LookInput) and (ExitDoor != 'unlocked'):
            print(f"There is a note on the wall. It reads:\nMine code has 4 digits. Mine third is one more than mine first, which is twice thy fourth,\nten less than thy first with 8. Mine second is mine total without two.\nThe door is {ExitDoor}. There is a doorway to your south.")
        elif (PlayerInput in LookInput) and (ExitDoor == 'unlocked'):
            print(f"You are in the final room. The door to the north is {ExitDoor}. There is a doorway to your south.")
        elif PlayerInput in UseAction and (ExitDoor != 'unlocked'):
            print("It is a four-digit lock. (To go back, type back or leave)")
            Padlock = 0
            while Padlock not in Leave: # This loop caused me many issues and I hate it.
                Padlock = input()
                if Padlock.isdigit() and len(Padlock) == 4:
                    if Padlock == "4952":
                        print("The lock snaps open!")
                        ExitDoor = 'unlocked'
                        break
                    elif Padlock in Leave or (Padlock in Leave):
                        break
                    elif Padlock.isdigit() and Padlock != "4952":
                        print("The lock doesn't budge.")
                        continue
                elif len(Padlock) != 4:
                    print("Please enter a four-digit code using numbers only.")        
            else:
                print("You return to the room.")
        elif PlayerInput in UseAction and (ExitDoor == 'unlocked'):
            print("You've already unlocked the lock! There's nothing else here to use.")
        else:
            NoInput()

def Room5(): # The final room, where the player wins.
    global GameOver
    print(f"=+=+=+=+=+= GAME OVER! =+=+=+=+=+=\nCongratulations, {PlayerName}! You have reached the end of the text adventure.\nI hope that you enjoyed it and it wasn't too rubbish.\nOh, right.\n\nYou reach the final room. Sitting there, shining in the sunlight...\nis a cake. And it's all yours.\n")
    GameOver = 1

# The actual game code begins here.
print("Welcome to James Qian's zany text adventure! This is a quick text adventure created for ME021 in python.\nIf you're looking for a more exciting text adventure, go play Zork, because this is just a school project!")
global PlayerName
global ExitDoor
PlayerName = str(input("What's your name, adventurer? "))
print(f"Welcome, {PlayerName}! Let the adventure begin!")
LookedAtWaterfall = False
UsedLever = False
Room0Desc = 0
Room1Desc = 0
Room2Desc = 0
Room3Desc = 0
Room4Desc = 0
ExitDoor = 'locked with a padlock'
NorthDoorCondition = 'barred'
LookedAtNote = True
while GameOver == 0:
    if RoomID == 0: #This if else statement controls what room the player is in.
        if Room0Desc == 0: # These statements only run the first time the player enters each room. I probably could have made this in a more efficient way but it works so oh well
            print('You find yourself in an empty room. The room is dimly lit from a light coming from a doorway to your north. (Hint: request help by typing "help")')
            Room0Desc += 1
            continue
        StartingRoom() # Calls room 0 code
    elif RoomID == 1:
        if Room1Desc == 0:
            print("You enter a rectangular room stretching down to your left and right. The doorway you came from is to your south.\nThe north wall has a door locked by metal bars. There are doorways to your east and west.")
            Room1Desc += 1
            continue
        Room1()
    elif RoomID == 2:
        if Room2Desc == 0:
            print("You enter a serene-looking room. The walls are made from a light bamboo, and there is a pleasant water feature trickling before you.\nOtherwise, the room is featureless.")
            Room2Desc += 1
            continue
        Room2()
    elif RoomID == 3:
        if Room3Desc == 0:
            print("The room you enter is completely pitch black save for a small table illuminated by the light from the doorway.\nThere's a piece of paper on the table.")
            Room3Desc +=1
            continue
        Room3()
    elif RoomID == 4:
        if Room4Desc == 0:
            print("This room is small, little more than a square. There's a door to your north, locked by a four-digit combination padlock.\nOn the left, there is a small piece of paper pinned to the wall with some writing on it.")
            Room4Desc +=1
            continue
        Room4()
    else:
        Room5()
exit()