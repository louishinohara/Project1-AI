import os
import random
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def blocked(fp):

    probabilityBlocked = False
    if random.random() <= fp:           # Can do different types of probabilities here like uniform , gauss
        probabilityBlocked = True
    else:
        probabilityBlocked = False

    return probabilityBlocked

def createMaze(dim, fp):
    maze = []
    counter = 0             # Obstacle counter

    for i in range(dim):    # Populate maze   
        col = []
        for j in range(dim):
            spaceFull = 0
            if blocked(fp):  # Decide if space is open/blocked
                spaceFull = 1
                counter += 1
            col.append(spaceFull)
        maze.append(col)

    maze[0][0] = 0.5        # Start/Goal spaces
    maze[dim-1][dim-1] = 0.5
    print(counter)
    return np.array(maze)

def showMaze(maze, dim):
    ## grid from array: https://stackoverflow.com/questions/43971138/python-plotting-colored-grid-based-on-values
    
    # create discrete colormap 
    cmap = colors.ListedColormap(['white', 'green', 'black'])
    bounds = [0, 0.4, 0.6, 1]   #[white = 0, green=0.5, black=1]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(maze, cmap=cmap, norm=norm)

    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-.5, dim, 1))
    ax.set_yticks(np.arange(-.5, dim, 1))

    ## tick adjustment from https://stackoverflow.com/questions/38973868/adjusting-gridlines-and-ticks-in-matplotlib-imshow
    ax.set_xticklabels(np.arange(0, dim+1, 1))
    ax.set_yticklabels(np.arange(0, dim+1, 1))

    plt.show()

def main():
    dimensions = 10
    probabilityOfBlock = 0.3
    maze = createMaze(dimensions,probabilityOfBlock)
    print(maze)
    showMaze(maze, dimensions)
                   

main()