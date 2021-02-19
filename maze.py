import random
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


#Returns true false based on probability blocked, true false indicating whether cell should be blocked or free
def blocked(fp):

    probabilityBlocked = False
    if random.random() <= fp:           # Can do different types of probabilities here like uniform , gauss
        probabilityBlocked = True
    else:
        probabilityBlocked = False

    return probabilityBlocked

def createMaze(dim, fp):
    maze = []

    for i in range(dim):    # Populate maze   
        col = []
        for j in range(dim):
            spaceStatus = 2
            if blocked(fp):  # Decide if space is open/blocked
                spaceStatus = 3
            col.append(spaceStatus)
        maze.append(col)

    maze[0][0] = 0        # Start/Goal spaces
    maze[dim-1][dim-1] = 1
    return np.array(maze)

def showMaze(maze, dim):
    ## grid from array: https://stackoverflow.com/questions/43971138/python-plotting-colored-grid-based-on-values

    # create discrete colormap 
    cmap = colors.ListedColormap(['green', 'white', 'black', 'blue', 'red', 'purple'])
    bounds = [0,1.9,2.9, 3.9, 4.9, 5.9, 6.9]   #[green = 0, green=1, white=2, black=3, blue=4, red=5, purple = 6] [start, goal, open, blocked, path, fire, predictedFire]
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


def updateMaze(maze, coordinates, dimensions):      # Updates the maze to see the path
    completedMaze = maze.copy()                     # Create deep copy

    while coordinates is not None:                  # Iteratively place 4 where nodes used to be
        completedMaze[coordinates.x][coordinates.y] = 4
        coordinates = coordinates.prev
        if coordinates.x + coordinates.y == 0:      # If we are at the start node, break
            break
    completedMaze[dimensions-1][dimensions-1] = 1    #Convert goal node back to 1
    return completedMaze, coordinates != None   # Returns the completed maze or if there is no path, return false




