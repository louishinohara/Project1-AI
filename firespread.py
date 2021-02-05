import random
from node import Node
from queue import Queue

def igniteFire(MAZE, DIMENSIONS):
    initFireMaze = MAZE.copy()                              # Create Copy
    ignited = False                                         # Bool when valid spot is found
    FREE_SPACE = 2                                          # Constants
    FIRE_SPACE = 5
    
    while not ignited:
        xCoord = random.randrange(1, DIMENSIONS - 2 )       # Find a random x and y coord
        yCoord = random.randrange(1, DIMENSIONS - 2 )
        if (initFireMaze[xCoord][yCoord] == FREE_SPACE):    # Check if that space is free and ignite fire
            initFireMaze[xCoord][yCoord] = FIRE_SPACE
            ignited = True

    return initFireMaze                                     # Return maze with ignited fire 



def spreadFire(maze, dimensions, q):
    mazeCopy = maze.copy()
    FREE_SPACE = 2
    BLOCKED_SPACE = 3
    FIRE_SPACE = 5
    for x in range(dimensions):
        for y in range(dimensions):
            coordinate = maze[x][y]
            if (coordinate == FREE_SPACE and coordinate != BLOCKED_SPACE and coordinate != FIRE_SPACE): #only applies for free spaces that are not the start or goal

                #for each cell, check how many neighbors on fire
                k = 0
                leftRight = [1, 0, 0, -1]
                upDown = [0, 1, -1, 0]

                for i in range(4):
                    row = x + upDown[i]
                    col = y + leftRight[i]

                    if (0 <= row < dimensions and 0 <= col < dimensions and maze[row][col] == FIRE_SPACE): # in Matrix and status = on fire
                        k += 1

                prob = 1 - ((1 - q) ** k)
                if (random.random() <= prob):
                    mazeCopy[x][y] = FIRE_SPACE
    return mazeCopy 
