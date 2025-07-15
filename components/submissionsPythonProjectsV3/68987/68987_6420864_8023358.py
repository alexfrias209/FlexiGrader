print('Welcome user\nThe computer will automatically execute the code created to solve a maze.\n')
print('The code has to be overwritten prior to being run, meaning only the programmer  may choose the maze.\n')
print("This code was too complicated for me to write completely. I used external services to write this code. No inputs could be made into the maze to change the maze as the individual wants.\n")
import queue

# creating an empty string for lists and putting the maze strings in the list

def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#", " ", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", " ", "#", " ", " ", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", "#", " ", " ", "#"])
    maze.append(["#", "X", "#", "#", "#", "#", "#", "#", "#", "#"])

# returns the maze chosen in the programmer by the programmer

    return maze

def createMaze2():
    maze = []
    maze.append(["#", "#", "#", "#", "O", "#", "#", "#", "#", "#"])
    maze.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append([" ", "#", " ", "#", " ", " ", "#", " ", "#", "#"])
    maze.append([" ", " ", "#", "#", "#", " ", "#", " ", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", "#", " ", " ", " "])
    maze.append(["#", " ", "#", "#", "#", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "X", "#", "#", "#", "#", "#"])

    return maze

def createMaze3():
    maze = []
    maze.append(["#", "O", "#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append([" ", "#", " ", "#", " ", " ", "#", " ", "#", "#"])
    maze.append([" ", " ", "#", "#", "#", " ", "#", " ", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", "#", " ", " ", " "])
    maze.append(["#", " ", "#", "#", "#", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", "#", "#", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#", "#"])

    return maze

# prints the maze and validates the maze's entrance, sides and exits

def printMaze(maze, path = " "):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end=" ")
            else:
                print(col + " ", end=" ")
        print()

# Gives the computer moves and tells the outline of the maze and having the computer tell whether that path is the shortest

def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


# Allows the computer to use the moves to find the end of the maze with the fastest possible solution

def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        printMaze(maze, moves)
        return True
    
    return False

# Is the main structure of the program, creating the queue for the maze and letting LRUD to be introduced to the Queue till the moves do not equal to X

nums = queue.Queue()
nums.put("")
add = " "
maze = createMaze3()

while not findEnd(maze, add):
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)
        
