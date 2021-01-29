import os
import random
import matplotlib.pyplot as plt
import matplotlib.colors


def onFire(fp):

    probabilityOfFire = False
    if random.random() <= fp:           # Can do different types of probabilities here like uniform , gauss
        probabilityOfFire = True
    else:
        probabilityOfFire = False

    return probabilityOfFire

def creatMaze(dim, fp):
    maze = []
    counter = 0
    for i in range(dim):
        col = []
        for j in range(dim):
            spaceOnFire = 0
            if onFire(fp):
                spaceOnFire = 1
                counter += 1
            col.append(spaceOnFire)
        maze.append(col)
    maze[0][0] = float('inf')
    maze[dim-1][dim-1] = float('-inf')
    print(maze,counter)


def main():
    dimensions = 10
    probabilityOfFire = 0.5
    creatMaze(dimensions,probabilityOfFire)

main()