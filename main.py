import os
import matplotlib.pyplot as plt
import time
from dfs import DFS
from dfs import initDFS
from bfs import initBFS
from node import Node
from maze import createMaze, showMaze
from customTimer import customTimer
from firespread import spreadFire


def main():


    #testing out the fire spreading
    testMaze =[]

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





     dimensions = 1000
    probabilityOfBlock = 0.3
    maze = createMaze(dimensions,probabilityOfBlock)
    print(maze)
    start = time.time()
    complete = False
    complete = initDFS(maze,dimensions)
    end = time.time()
    print('The elapsed time is: ' + str(round( end - start)) + ' seconds.' )     
 


    
    #showMaze(maze, dimensions)
    
                   

main()