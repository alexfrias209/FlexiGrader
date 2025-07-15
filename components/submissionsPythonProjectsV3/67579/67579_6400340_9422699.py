import pygame
import random
import time

User_Tag = input("Insert a Three Letter Tag").upper()[0: 3]
'''print(User_Tag, "\n")'''

# Score Manager
Score_Dict = {}
Top_3_Scores = {}
Scoreboard = open("67579_6400339_2888447.txt", "r")
for line in Scoreboard.readlines():
    # print(line.split(":")[1])
    Score_Dict[line.split(":")[0]] = int(line.split(":")[1].splitlines()[0])
'''print(Score_Dict, "\n")'''

# Get the three highest scores from the record, less if there is fewer than 3 total.
if len(range(3)) < len(range(len(Score_Dict))):
    for Score in range(3):
        Top_3_Scores[max(Score_Dict, key=Score_Dict.get)] = Score_Dict[
            max(Score_Dict, key=Score_Dict.get)]
        del Score_Dict[max(Score_Dict, key=Score_Dict.get)]
else:
    for Score in range(len(Score_Dict)):
        Top_3_Scores[max(Score_Dict, key=Score_Dict.get)] = Score_Dict[
            max(Score_Dict, key=Score_Dict.get)]
        del Score_Dict[max(Score_Dict, key=Score_Dict.get)]
'''print(Top_3_Scores)'''
Score_Dict = Score_Dict | Top_3_Scores

# Sprite Manager
Background_Img = pygame.image.load("Tetris_Background.png")
Start_Button = pygame.image.load("Tetris_Background_Start_Button.png")
B1 = pygame.image.load("L1_Block.png")
B2 = pygame.image.load("L2_Block.png")
B3 = pygame.image.load("T_Block.png")
B4 = pygame.image.load("Z1_Block.png")
B5 = pygame.image.load("Z2_Block.png")
B6 = pygame.image.load("O_Block.png")
B7 = pygame.image.load("I_Block.png")
Individual_Cube = pygame.image.load("L1-IN-Block.png")

# The Grid for moving the block
Grid_Temp = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 14
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 15
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 16
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 17
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 18
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 19
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # Row 20

# The Grid for Finalizing Movement
Grid_Real = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 14
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 15
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 16
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 17
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 18
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 19
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # Row 20

# The Combined Grid
Grid_Final = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 12
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 14
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 15
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 16
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 17
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 18
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 19
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # Row 20

# Block Dimensions
Block_Dimensions = [0, 0]
'''
L1_Block = [3, 2]
L2_Block = [3, 2]
T_Block = [3, 2]
Z1_Block = [3, 2]
Z2_Block = [3, 2]
O_Block = [2, 2]
I_Block = [4, 1]
'''

# Block Variations
Block_Plots = []
L1_Plot = [[[1, 0, 0], [1, 1, 1]],
           [[1, 1], [1, 0], [1, 0]],
           [[1, 1, 1], [0, 0, 1]],
           [[0, 1], [0, 1], [1, 1]]]
L2_Plot = [[[0, 0, 1], [1, 1, 1]],
           [[1, 0], [1, 0], [1, 1]],
           [[1, 1, 1], [1, 0, 0]],
           [[1, 1], [0, 1], [0, 1]]]
T_Plot = [[[1, 1, 1], [0, 1, 0]],
          [[0, 1], [1, 1], [0, 1]],
          [[0, 1, 0], [1, 1, 1]],
          [[1, 0], [1, 1], [1, 0]]]
Z1_Plot = [[[1, 1, 0], [0, 1, 1]],
           [[0, 1], [1, 1], [1, 0]],
           [[1, 1, 0], [0, 1, 1]],
           [[0, 1], [1, 1], [1, 0]]]
Z2_Plot = [[[0, 1, 1], [1, 1, 0]],
           [[1, 0], [1, 1], [0, 1]],
           [[0, 1, 1], [1, 1, 0]],
           [[1, 0], [1, 1], [0, 1]]]
O_Plot = [[[1, 1], [1, 1]],
          [[1, 1], [1, 1]],
          [[1, 1], [1, 1]],
          [[1, 1], [1, 1]]]
I_Plot = [[[1, 1, 1, 1]],
          [[1], [1], [1], [1]],
          [[1, 1, 1, 1]],
          [[1], [1], [1], [1]]]

# Window Setup
pygame.init()
size = (800, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TETRIS")

# Variables
Start_Game = True
RandBlockGen = [0, 0]
RandBlockGen[0] = random.randint(1, 7)
RandBlockGen[1] = random.randint(1, 7)
Rotational_Phase = 0
BlockDropDelay = 0
Block_Drop_Amount = 0
Block_Shift = 3
DropBlockTF = False
Score = 0
CanMoveLeft = 0
CanMoveRight = 0
CanMoveDown = 0
text_font = pygame.font.SysFont("Arial", 50, bold=True)
Next_Block = 0


# Functions
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


# Start the program
Run_Program = True
while Run_Program is True:
    # Event Handler
    for event in pygame.event.get():
        # If someone presses the top-right X button, close the window.
        if event.type == pygame.QUIT:
            Run_Program = False
        # If someone presses a key, check what key and react appropriately
        if event.type == pygame.KEYDOWN:
            # Someone pressed Enter
            if event.key == pygame.K_RETURN:
                Start_Game = True
                DropBlockTF = False
            # Someone pressed Q
            if event.key == pygame.K_q and Start_Game is True:
                if Block_Shift <= (10 - Block_Dimensions[1]):
                    Block_Dimensions.reverse()
                    Rotational_Phase -= 1
                    if Rotational_Phase == -1:
                        Rotational_Phase = 3
                    '''print(Rotational_Phase)'''
            # Someone pressed E
            if event.key == pygame.K_e and Start_Game is True:
                if Block_Shift <= (10 - Block_Dimensions[1]):
                    Block_Dimensions.reverse()
                    Rotational_Phase += 1
                    if Rotational_Phase == 4:
                        Rotational_Phase = 0
                    '''print(Rotational_Phase)'''
            # Someone pressed A
            if event.key == pygame.K_a and Start_Game is True:
                CanMoveLeft = 0
                if Block_Shift > 0:
                    for Row in range(len(Grid_Final)):
                        for Column in range(len(Grid_Final[Row])):
                            if Grid_Final[Row][Column] == 1 and Grid_Final[Row][Column - 1] != 2:
                                '''print(f"to the right of a block, row is {Row}, Column is {Column}")'''
                                CanMoveLeft += 1
                    if CanMoveLeft == 4:
                        Block_Shift -= 1
            # Someone pressed D
            if event.key == pygame.K_d and Start_Game is True:
                CanMoveRight = 0
                if Block_Shift < (10 - Block_Dimensions[0]):
                    for Row in range(len(Grid_Final)):
                        for Column in range(len(Grid_Final[Row])):
                            if Grid_Final[Row][Column] == 1 and Grid_Final[Row][Column + 1] != 2:
                                '''print(f"to the right of a block, row is {Row}, Column is {Column}")'''
                                CanMoveRight += 1
                    if CanMoveRight == 4:
                        Block_Shift += 1
            # Someone pressed S
            if event.key == pygame.K_s and Start_Game is True:
                CanMoveDown = 0
                if Block_Drop_Amount < (20 - Block_Dimensions[1]):
                    for Row in range(len(Grid_Final)):
                        for Column in range(len(Grid_Final[Row])):
                            if Grid_Final[Row][Column] == 1 and Grid_Final[Row + 1][Column] != 2:
                                '''print(f"to the right of a block, row is {Row}, Column is {Column}")'''
                                CanMoveDown += 1
                    if CanMoveDown == 4:
                        Block_Drop_Amount += 1

    # Early Window Management
    screen.blit(Background_Img, (0, 0))

    # Background Processes
    if Start_Game is False:
        screen.blit(Start_Button, (60, 778))
    elif Start_Game is True:
        # This checks if a block is present and initiates it when necessary
        if DropBlockTF is False:
            if RandBlockGen[0] == 1:
                Block_Plots = L1_Plot
                Block_Dimensions = [3, 2]
            elif RandBlockGen[0] == 2:
                Block_Plots = L2_Plot
                Block_Dimensions = [3, 2]
            elif RandBlockGen[0] == 3:
                Block_Plots = T_Plot
                Block_Dimensions = [3, 2]
            elif RandBlockGen[0] == 4:
                Block_Plots = Z1_Plot
                Block_Dimensions = [3, 2]
            elif RandBlockGen[0] == 5:
                Block_Plots = Z2_Plot
                Block_Dimensions = [3, 2]
            elif RandBlockGen[0] == 6:
                Block_Plots = O_Plot
                Block_Dimensions = [2, 2]
            elif RandBlockGen[0] == 7:
                Block_Plots = I_Plot
                Block_Dimensions = [4, 1]
            DropBlockTF = True
            Block_Shift = 3
            Rotational_Phase = 0

        # This is a Timer that sets the delay for blocks dropping row by row
        # When ready, remove the sleep command and increase BlockDropDelay
        if BlockDropDelay == 50:
            BlockDropDelay = 0
            Block_Drop_Amount += 1
            '''time.sleep(1)'''
        else:
            BlockDropDelay += 1

        # This Process Detects Complete Rows in the Grid_Real layer and drops everything down
        for Row in range(len(Grid_Real)):
            if Grid_Real[Row] == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]:
                Grid_Real.pop(Row)
                Grid_Real.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                Score += 1

        # Prevent Block Collisions and Floor Clipping
        for Row in range(len(Grid_Temp)):
            for Column in range(len(Grid_Temp[Row])):
                # Check if the block is colliding with another block
                if Grid_Temp[Row][Column] == 1 and Grid_Real[Row][Column] == 2:
                    for Row1 in range(len(Grid_Temp)):
                        for Column1 in range(len(Grid_Temp[Row1])):
                            if Grid_Temp[Row1][Column1] == 1:
                                Grid_Real[Row1 - 1][Column1] = 2
                                Grid_Temp[Row1][Column1] = 0
                    # Reset everything for the next block
                    Block_Drop_Amount -= 1
                    RandBlockGen[0] = RandBlockGen[1]
                    RandBlockGen[1] = random.randint(1, 7)
                    DropBlockTF = False
                    Block_Drop_Amount = 0
        if Block_Drop_Amount > 20 - len(Block_Plots[Rotational_Phase]):
            for Row in range(len(Grid_Temp)):
                for Column in range(len(Grid_Temp[Row])):
                    if Grid_Temp[Row][Column] == 1:
                        Grid_Real[Row][Column] = 2
            # Reset everything for the next block
            Block_Drop_Amount -= 1
            RandBlockGen[0] = RandBlockGen[1]
            RandBlockGen[1] = random.randint(1, 7)
            DropBlockTF = False
            Block_Drop_Amount = 0

        # This does the math so that the block is plotted on the grid
        Grid_Temp = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 1
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 2
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 3
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 5
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 6
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 7
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 8
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 9
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 10
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 11
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 12
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 13
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 14
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 15
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 16
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 17
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 18
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 19
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # Row 20
        for Row in range(len(Block_Plots[Rotational_Phase])):
            for Column in range(len(Block_Plots[Rotational_Phase][Row])):
                if Block_Plots[Rotational_Phase][Row][Column] == 1:
                    '''print(Block_Shift, "+", Column)'''
                    Grid_Temp[Block_Drop_Amount + Row][Block_Shift + Column] = Block_Plots[Rotational_Phase][Row][
                        Column]

        # Print The Final Grid
        for Rows in range(len(Grid_Temp)):
            for Columns in range(len(Grid_Temp[Rows])):
                if Grid_Temp[Rows][Columns] > Grid_Real[Rows][Columns]:
                    Grid_Final[Rows][Columns] = Grid_Temp[Rows][Columns]
                else:
                    Grid_Final[Rows][Columns] = Grid_Real[Rows][Columns]
            '''print(Grid_Final[Rows])
        #print("\n")'''

        # Update the

        # This Detects a Game Over
        for Column in Grid_Final[0]:
            if Column == 2:
                time.sleep(3)
                Start_Game = False
                Grid_Real = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 1
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 2
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 3
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 4
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 5
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 6
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 7
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 8
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 9
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 10
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 11
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 12
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 13
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 14
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 15
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 16
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 17
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 18
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Row 19
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # Row 20
                Block_Shift = 3

                # Update the Score File
                Score_Dict[User_Tag] = Score
                Score_File = open("67579_6400339_2888447.txt", "w")
                for Name in list(Score_Dict.keys()):
                    Score_File.write(f"{Name}:{Score_Dict[Name]}\n")
                    print(f"{Name}:{Score_Dict[Name]}\n")
                time.sleep(1)

                # Update the Scoreboard
                Top_3_Scores = {}
                Scoreboard = open("67579_6400339_2888447.txt", "r")
                for line in Scoreboard.readlines():
                    # print(line.split(":"))
                    Score_Dict[line.split(":")[0]] = int(line.split(":")[1].splitlines()[0])
                print(Score_Dict)
                if len(range(3)) < len(range(len(Score_Dict))):
                    for Score in range(3):
                        Top_3_Scores[max(Score_Dict, key=Score_Dict.get)] = Score_Dict[
                            max(Score_Dict, key=Score_Dict.get)]
                        del Score_Dict[max(Score_Dict, key=Score_Dict.get)]
                    print(Top_3_Scores)
                else:
                    for Score in range(len(Score_Dict)):
                        Top_3_Scores[max(Score_Dict, key=Score_Dict.get)] = Score_Dict[
                            max(Score_Dict, key=Score_Dict.get)]
                        del Score_Dict[max(Score_Dict, key=Score_Dict.get)]
                    print(Top_3_Scores)
                Score_Dict = Score_Dict | Top_3_Scores

        # Create the Pygame Window Effects
        draw_text(f"Score : {Score}", text_font, (255, 255, 255), 100, 800)
        draw_text(f"Top Scores ", text_font, (255, 255, 255), 75, 375)
        PlayerNumber = 0
        for TopPlayer in list(Top_3_Scores.keys()):
            PlayerNumber += 1
            draw_text(f"{TopPlayer} : {Top_3_Scores[TopPlayer]}", text_font, (255, 255, 255), 75,
                      375 + (50 * PlayerNumber))

        # Create the Next Block Display
        for Row in range(len(Grid_Final)):
            for Column in range(len(Grid_Final[Row])):
                if Grid_Final[Row][Column] == 1:
                    screen.blit(Individual_Cube, (329 + (41 * Column), 60 + (41 * Row)))
                elif Grid_Final[Row][Column] == 2:
                    screen.blit(Individual_Cube, (329 + (41 * Column), 60 + (41 * Row)))
        if RandBlockGen[1] == 1:
            screen.blit(B1, (125, 200))
        elif RandBlockGen[1] == 2:
            screen.blit(B2, (125, 200))
        elif RandBlockGen[1] == 3:
            screen.blit(B3, (125, 200))
        elif RandBlockGen[1] == 4:
            screen.blit(B4, (125, 200))
        elif RandBlockGen[1] == 5:
            screen.blit(B5, (125, 200))
        elif RandBlockGen[1] == 6:
            screen.blit(B6, (145, 200))
        elif RandBlockGen[1] == 7:
            screen.blit(B7, (105, 215))

    pygame.display.update()
pygame.quit()
