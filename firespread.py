import random
from node import Node
from queue import Queue


def spreadFire(maze, dimensions, q):
    mazeCopy = maze.copy()
    for x in range(dimensions):
        for y in range(dimensions):
            if (maze[x][y] == 2): #only applies for free spaces that are not the start or goal

                #for each cell, check how many neighbors on fire
                k = 0
                leftRight = [1, 0, 0, -1]
                upDown = [0, 1, -1, 0]

                for i in range(4):
                    row = x + upDown[i]
                    col = y + leftRight[i]

                    if (0 <= row < dimensions and 0 <= col < dimensions            # in matrix
                            and maze[row][col] == 4):           # status = on fire
                        k += 1
                prob = 1 - ((1 - q) ** k)
                if (random.random() <= prob):
                    mazeCopy[x][y] = 4
    return mazeCopy 




                    

