import time
from node import Node
from queue import Queue
from maze import showMaze

def initBFS(maze,dimensions):
    start_time = time.time() 
    bfsResult = BFS(maze, Node(0,0), dimensions)
    print("--- %s seconds ---" % (time.time() - start_time))

    if (bfsResult is not None):
        print("--BFS Goal Path Found--")
        bfsResultsCopy = bfsResult
        # while(bfsResult is not None):     # Prints coordinates to path
        #     print('(' + str(bfsResult.x) + ', ' + str(bfsResult.y) + ') <- ', end='')  
        #     bfsResult = bfsResult.prev
        return bfsResultsCopy
    else:
      print("BFS found no solution")
    return None

def BFS(maze, startNode, dim):
    fringe = Queue()
    fringe.put(startNode)
    visitedCoords = set()

    # Arrays for neighbor access (right, down, up, left)
    rightLeft = [1, 0, 0, -1]
    upDown = [0, 1, -1, 0]

    while(not fringe.empty()):
        curr = fringe.get()

        if(curr.x == (dim-1) and curr.y == (dim-1)):  # Goal Node Found
            return curr

        elif((curr.x, curr.y) not in visitedCoords):  # Process New Node's Neighbors

            for i in range(4):
                row = curr.x + upDown[i]
                col = curr.y + rightLeft[i]

                # Add valid child to fringe
                if (0 <= row < dim and 0 <= col < dim                   # in matrix
                        and (maze[row][col] in (1, 2, 4 ))              # status = open/goal
                        and ((row, col) not in visitedCoords)):         # not visited
                    fringe.put(Node(row, col, curr))

            visitedCoords.add((curr.x, curr.y))                         # mark current node as visited

    # Else: Goal Node not found, fringe empty
    return None