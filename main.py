import os
import matplotlib.pyplot as plt

from maze import createMaze, showMaze, updateMaze
from customTimer import customTimer
from firespread import igniteFire, spreadFire
from node import Node, aStarNode

from dfs import initDFS
from bfs import initBFS
from bfsS1 import initBFSS1  # BFS for Strategy 1
from bfsS2 import initBFSS2  # BFS for Strategy 2
from bfsS3 import initBFSS3  # BFS for Strategy 3


def main():
    DIMENSIONS = 12
    PROBABILITY_OF_BLOCK = 0.3
    MAZE = createMaze(DIMENSIONS, PROBABILITY_OF_BLOCK)  # Create the maze

    # firstSection(MAZE, DIMENSIONS,PROBABILITY_OF_BLOCK)
    secondSection(MAZE, DIMENSIONS)


def firstSection(MAZE, DIMENSIONS, PROBABILITY_OF_BLOCK):
    # List of functions to store in array and execute in for loop on next line
    # Store as function to call with param as our maze and the dimensions of the maze
    # DFS Maze Function, BFS Maze Function
    funcList = [initDFS(MAZE, DIMENSIONS), initBFS(MAZE, DIMENSIONS)]

    for func in funcList:
        # Returns Completed Maze and if path is found
        completedMaze, foundPath = updateMaze(MAZE, func, DIMENSIONS)
        if foundPath:
            showMaze(completedMaze, DIMENSIONS)
        else:
            break


def secondSection(MAZE, DIMENSIONS):
    # fireMaze = igniteFire(MAZE, DIMENSIONS)                             # Gets a maze with ignited fire
    # showMaze(fireMaze, DIMENSIONS)
    PROBABILITY_OF_FIRE_SPREAD = 0.3
    fireMaze = [[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],   # For consistent testing
                [2, 2, 2, 2, 2, 3, 2, 5, 3, 2, 2, 2],
                [2, 2, 2, 2, 2, 3, 2, 3, 2, 2, 2, 2],
                [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 2],
                [3, 3, 2, 2, 2, 3, 3, 2, 3, 2, 2, 2],
                [2, 3, 3, 2, 3, 2, 2, 2, 2, 2, 2, 2],
                [2, 3, 2, 2, 3, 2, 3, 3, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]]

    # Agent doesn't modify path and dies
    initBFSS1(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS)     
    
    # Agent only predicts one step ahead. Therefore will follow path and die. However if the flame peaks ahead, it will dodge it (Need to test repeatedly because it depends on probability of fire spread)
    initBFSS2(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS)
    
    initBFSS3(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS)


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

# This matrix for BFSS2 shows that the agent will pick an alternate path
# Without the 5 in [1,7], the agent will travel along the edge of the matrix
# However once the fire blocks the path, the agent will choose an alternate path to adapt
# DIM = 10
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

# TEST MATRIX FOR BFFSS3
