import random
import copy
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



def spreadFire(maze, dimensions, q):    # Params are the maze (and updated fire maze from last iteration), dimensions, probability of fire spread
    mazeCopy = copy.deepcopy(maze)      # Need to make copy so current iteration results don't affect results of current iterations' coordinates that appear later 
    FREE_SPACE = 2
    BLOCKED_SPACE = 3
    FIRE_SPACE = 5

    fire_coordinate = []            # Coordinates of where the fire spread to this iteration
    for x in range(dimensions):     # Mapping through entire matrix for coord on fire
        for y in range(dimensions):

            coordinate = maze[x][y] 
            
            if (coordinate == FREE_SPACE and coordinate != BLOCKED_SPACE and coordinate != FIRE_SPACE): # Only applies for free spaces, unblock spaces, and non fire spaces

                #for each cell, check how many neighbors on fire
                neighbors_on_fire = 0
                leftRight = [1, 0, 0, -1]
                upDown = [0, 1, -1, 0]

                for i in range(4):
                    row = x + upDown[i]
                    col = y + leftRight[i]

                    if (0 <= row < dimensions and 0 <= col < dimensions and maze[row][col] == FIRE_SPACE): # in Matrix and status = on fire
                        neighbors_on_fire += 1

                prob = 1 - ((1 - q) ** neighbors_on_fire)   # Probability that this coord will catch on fire

                if (random.random() <= prob):               # Execute probability
                    mazeCopy[x][y] = FIRE_SPACE
                    fire_coordinate.append([x,y])
                    
    return mazeCopy, fire_coordinate 
