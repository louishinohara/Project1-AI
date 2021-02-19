import os
import matplotlib.pyplot as plt
import copy
import numpy as np

from maze import createMaze, showMaze, updateMaze
from firespread import igniteFire, spreadFire
from node import Node, aStarNode
from aStar import initAStar
from dfs import initDFS
from bfs import initBFS
from strat1 import initStrat1  # Algorithm for Strategy 1
from strat2 import initStrat2  # Algorithm for Strategy 2
from strat3 import initStrat3  # Algorithm for Strategy 3

def main():
    DIMENSIONS = 80
    PROBABILITY_OF_BLOCK = 0.3
    MAZE = createMaze(DIMENSIONS, PROBABILITY_OF_BLOCK)  # Create the maze

    MAZE_COPY = copy.deepcopy(MAZE)
    mazeWithoutStrategy(MAZE_COPY, DIMENSIONS,PROBABILITY_OF_BLOCK)           # Our BFS, DFS, A* Implementation
    mazeWithStrategy(MAZE, DIMENSIONS)                                 # Our three strategies


def mazeWithoutStrategy(MAZE, DIMENSIONS, PROBABILITY_OF_BLOCK):
    # List of functions to store in array and execute in for loop on next line
    # Store as function to call with param as our maze and the dimensions of the maze
    # DFS Maze Function, BFS Maze Function, Astar Maze Function
    funcList = [initDFS(MAZE, DIMENSIONS), initBFS(MAZE, DIMENSIONS), initAStar(MAZE, DIMENSIONS)]

    for func in funcList:
        # Returns Completed Maze and if path is found
        completedMaze, foundPath = updateMaze(MAZE, func, DIMENSIONS)
        if foundPath:
            showMaze(completedMaze, DIMENSIONS)
        else:
            break


def mazeWithStrategy(MAZE, DIMENSIONS):
    PROBABILITY_OF_FIRE_SPREAD = 0.3
    fireMaze = igniteFire(MAZE, DIMENSIONS)

    # fireMaze = [[0, 2, 2, 2, 2, 2, 2, 2, 2, 2,],
    #         [2, 2, 2, 2, 2, 3, 2, 5, 3, 2],
    #         [2, 2, 2, 2, 2, 3, 2, 3, 2, 2],
    #         [3, 2, 2, 2, 2, 2, 3, 2, 2, 2],
    #         [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    #         [2, 2, 3, 2, 2, 3, 2, 2, 2, 2],
    #         [3, 3, 2, 3, 2, 3, 3, 2, 3, 2],
    #         [2, 3, 3, 2, 3, 2, 2, 2, 2, 2],
    #         [2, 3, 2, 2, 3, 2, 3, 3, 2, 2],
    #         [2, 2, 2, 2, 2, 3, 2, 2, 2, 1]]

    # The three different strategies
    strat1Maze = copy.deepcopy(fireMaze)
    initStrat1(strat1Maze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS)     

    strat2Maze = copy.deepcopy(fireMaze)
    initStrat2(strat2Maze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS)

    strat3Maze = copy.deepcopy(fireMaze)
    initStrat3(strat3Maze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS)



main()

# Sample maze where agent gauranteed death
# fireMaze = [[0, 2, 2, 3, 2, 2, 2, 3, 2, 2,],
#             [2, 2, 2, 2, 2, 3, 2, 3, 2, 3],
#             [2, 2, 2, 2, 2, 3, 2, 2, 2, 2],
#             [3, 2, 2, 2, 2, 2, 3, 2, 2, 2],
#             [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
#             [2, 2, 3, 2, 2, 3, 5, 2, 2, 2],
#             [3, 3, 2, 3, 2, 3, 3, 2, 3, 3],
#             [2, 3, 3, 2, 3, 2, 2, 2, 2, 2],
#             [2, 3, 2, 2, 3, 2, 3, 3, 2, 3],
#             [2, 2, 2, 2, 2, 3, 2, 2, 2, 1]]

# This matrix for strat2Maze which shows that the agent will pick an alternate path
# Without the 5 in [1,7], the agent will travel along the edge of the matrix
# However once the fire blocks the path, the agent will choose an alternate path to adapt
# DIM = 10  (Make sure to set dimensions to 10)

# fireMaze = [[0, 2, 2, 2, 2, 2, 2, 2, 2, 2,],
#             [2, 2, 2, 2, 2, 3, 2, 5, 3, 2],
#             [2, 2, 2, 2, 2, 3, 2, 3, 2, 2],
#             [3, 2, 2, 2, 2, 2, 3, 2, 2, 2],
#             [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
#             [2, 2, 3, 2, 2, 3, 2, 2, 2, 2],
#             [3, 3, 2, 3, 2, 3, 3, 2, 3, 2],
#             [2, 3, 3, 2, 3, 2, 2, 2, 2, 2],
#             [2, 3, 2, 2, 3, 2, 3, 3, 2, 2],
#             [2, 2, 2, 2, 2, 3, 2, 2, 2, 1]]


