import os


from dfs import DFS
from bfs import BFS
from node import Node
from maze import createMaze, showMaze

def main():
    dimensions = 10
    probabilityOfBlock = 0.4
    maze = createMaze(dimensions,probabilityOfBlock)
    print(maze)
    # DFS(maze)

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