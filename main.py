import os
import random
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

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
    maze[0][0] = 0.5
    maze[dim-1][dim-1] = 0.5
    print(counter)
    return np.array(maze)

def showMaze(maze):
    # fig, ax = plt.subplots()
    # ax.matshow(maze, cmap=plt.cm.Blues)

    plt.imshow(maze, interpolation='none')
    plt.colorbar()
    plt.show()  

def main():
    dimensions = 10
    probabilityOfFire = 0.3
    maze = creatMaze(dimensions,probabilityOfFire)
    print(maze)
    showMaze(maze)
                   

main()