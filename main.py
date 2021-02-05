import os
from dfs.dfs import initDFS 
from dfsS1 import initDFSS1 # DFS for Strategy 1
from bfs.bfs import initBFS
import matplotlib.pyplot as plt
from maze import createMaze, showMaze, updateMaze
from customTimer import customTimer
from firespread import igniteFire, spreadFire

def main():
    DIMENSIONS = 10
    PROBABILITY_OF_BLOCK = 0.3
    MAZE = createMaze(DIMENSIONS, PROBABILITY_OF_BLOCK) # Create the maze

    # firstSection(MAZE, DIMENSIONS,PROBABILITY_OF_BLOCK)
    secondSection(MAZE, DIMENSIONS)

def firstSection(MAZE, DIMENSIONS,PROBABILITY_OF_BLOCK):
    # List of functions to store in array and execute in for loop on next line
    # Store as function to call with param as our maze and the dimensions of the maze
    funcList = [initDFS(MAZE, DIMENSIONS), initBFS(MAZE, DIMENSIONS)]   #DFS Maze Function, BFS Maze Function

    for func in funcList:
        completedMaze, foundPath = updateMaze(MAZE, func, DIMENSIONS)   # Returns Completed Maze and if path is found
        if foundPath:
            showMaze(completedMaze, DIMENSIONS)
        else:
            break


def secondSection(MAZE, DIMENSIONS):
    fireMaze = igniteFire(MAZE, DIMENSIONS)                             # Gets a maze with ignited fire
    showMaze(fireMaze, DIMENSIONS)
    PROBABILITY_OF_FIRE_SPREAD = 0.3

    # initDFSS1(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS)



main()





















"""    for x in range(10):
        col = []
        for y in range(10):
            col.append(2)
        testMaze.append(col)
    testMaze[0][0] = 0
    testMaze[9][9] = 1
    testMaze[4][5] = 4
    print(testMaze)

    for x in range(2):
        testMaze = spreadFire(testMaze, 10, 0.3)
        for y in range(10):
            print(testMaze[y])
        print("---------") """