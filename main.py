import os
import random
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from queue import Queue


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
    counter = 0             # Obstacle counter

    for i in range(dim):    # Populate maze   
        col = []
        for j in range(dim):
            spaceStatus = 2
            if blocked(fp):  # Decide if space is open/blocked
                spaceStatus = 3
                counter += 1
            col.append(spaceStatus)
        maze.append(col)

    maze[0][0] = 0        # Start/Goal spaces
    maze[dim-1][dim-1] = 1
    print(counter)
    return np.array(maze)

def showMaze(maze, dim):
    ## grid from array: https://stackoverflow.com/questions/43971138/python-plotting-colored-grid-based-on-values
    
    # create discrete colormap 
    cmap = colors.ListedColormap(['green', 'white', 'black', 'red'])
    bounds = [0,1.9,2.9, 3.9, 4.9]   #[green = 0, green=1, white=2, black=3, red=4]
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


def DFS(maze):
    stack = []
    stack.append('a')
    stack.append('b')
    stack.append('c')

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

# Node: used for search algorithm
class Node():
  def __init__(self, x: int, y: int, prev=None):
      self.x = x
      self.y = y
      self.prev = prev

# BFS: takes in a start node and the dimensions (for the goal),
# outputs result node w/ path accessible via result.prev

def BFS(maze, startNode, dim):
    fringe = Queue()
    fringe.put(startNode)
    visitedCoords = set()

    # These arrays are used to get row and column
    # numbers of 4 neighbours of a given cell
    # (From GFG: https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/)
    leftRight = [1, 0, 0, -1]
    upDown = [0, 1, -1, 0]

    while(not fringe.empty()):
        curr = fringe.get()

        if(curr.x == (dim-1) and curr.y == (dim-1)):  # Goal Node Found
            return curr

        elif((curr.x, curr.y) not in visitedCoords):  # Process New Node's Neighbors

            # # Printing Path (debugging)
            # print("Processing coords: " + str(curr.x) + " " + str(curr.y))
            # bfsResult = curr
            # print('Processing Path: ', end='')
            # while(bfsResult is not None):
            #   print('(' + str(bfsResult.x) + ', ' + str(bfsResult.y) + ') <- ', end='')
            #   bfsResult = bfsResult.prev
            # print()

            
            for i in range(4):
                row = curr.x + upDown[i]
                col = curr.y + leftRight[i]

                # Add valid child to fringe
                if (0 <= row < dim and 0 <= col < dim            # in matrix
                        and (maze[row][col] in (1, 2))           # status = open/goal
                        and ((row, col) not in visitedCoords)):  # not visited
                    fringe.put(Node(row, col, curr))

            visitedCoords.add((curr.x, curr.y))                  # mark current node as visited

    # Else: Goal Node not found, fringe empty
    return None


def main():
    dimensions = 5
    probabilityOfBlock = 0.4
    maze = createMaze(dimensions,probabilityOfBlock)
    print(maze)
    DFS(maze)

    bfsResult = BFS(maze, Node(0,0), dimensions)
    if (bfsResult is not None):
      print("--BFS Goal Path--")
      while(bfsResult is not None):
        print('(' + str(bfsResult.x) + ', ' + str(bfsResult.y) + ') <- ', end='')   # why does this print only after exiting matplotlib?
        bfsResult = bfsResult.prev
    else:
      print("BFS found no solution")
    
    showMaze(maze, dimensions)
                   

main()