import os
from dfs import DFS
from node import Node
from dfs import initDFS
from bfs import initBFS
import matplotlib.pyplot as plt
from maze import createMaze, showMaze, updateMaze
from customTimer import customTimer
from firespread import spreadFire


def findPath(func, maze, DIMENSIONS):     # Params are the function, the unaltered maze, dimensions of maze  
    coordinates = func
    return updateMaze(maze, coordinates, DIMENSIONS)    # Returns the altered maze after calling function


def main():
    DIMENSIONS = 300
    PROBABILITY_OF_BLOCK = 0.2

    testMaze = []    #testing out the fire spreading
    maze = createMaze(DIMENSIONS, PROBABILITY_OF_BLOCK) # Create the maze

    # List of functions to store in array and execute in for loop on next line
    # Store as function to call with param as our maze and the dimensions of the maze
    funcList = [initDFS(maze, DIMENSIONS), initBFS(maze, DIMENSIONS)]   #DFS Maze Function, BFS Maze Function

    for func in funcList:
        completedMaze, foundPath = findPath(func, maze, DIMENSIONS) 
        if foundPath:
            showMaze(completedMaze, DIMENSIONS)
        else:
            break
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