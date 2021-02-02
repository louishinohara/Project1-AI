import os

import time
from dfs import DFS
from bfs import initBFS
from node import Node
from maze import createMaze, showMaze
from customTimer import customTimer


def main():
    dimensions = 1000
    probabilityOfBlock = 0.3
    maze = createMaze(dimensions,probabilityOfBlock)
    print(maze)
    # DFS(maze)
    start = time.time()
    complete = False
    complete = initBFS(maze,dimensions)
    end = time.time()
    print('The elapsed time is: ' + str(round( end - start)) + ' seconds.' )    
 


    
    showMaze(maze, dimensions)
    
                   

main()