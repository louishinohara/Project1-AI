import time
from node import Node
from queue import Queue


# DFS: takes in a start node and the dimensions (for the goal),
# outputs result node w/ path accessible via result.prev

def initDFS(maze,dimensions):
    start_time = time.time() 
    dfsResult = DFS(maze, Node(0,0), dimensions)
    print("--- %s seconds ---" % (time.time() - start_time))
    if (dfsResult is not None):
        print("--DFS Goal Path--")
        dfsResultsCopy = dfsResult
        # while(dfsResult is not None):
        #     print('(' + str(dfsResult.x) + ', ' + str(dfsResult.y) + ') <- ', end='')   # why does this print only after exiting matplotlib?
        #     dfsResult = dfsResult.prev
        return dfsResultsCopy        # Return Result of Coordinates
    else:
      print("DFS found no solution")
    return None                 # Return Result as None

def DFS(maze, startNode, dim):
    fringe = []
    fringe.append(startNode)
    visitedCoords = set()

    # These arrays are used to get row and column
    # numbers of 4 neighbours of a given cell
    # (From GFG: https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/)
    leftRight = [1, 0, 0, -1]
    upDown = [0, 1, -1, 0]

    while(len(fringe) != 0):
        curr = fringe.pop()

        if(curr.x == (dim-1) and curr.y == (dim-1)):  # Goal Node Found
            return curr

        elif((curr.x, curr.y) not in visitedCoords):  # Process New Node's Neighbors

            # # Printing Path (debugging)
            # print("Processing coords: " + str(curr.x) + " " + str(curr.y))
            # dfsResult = curr
            # print('Processing Path: ', end='')
            # while(dfsResult is not None):
            #   print('(' + str(dfsResult.x) + ', ' + str(dfsResult.y) + ') <- ', end='')
            #   dfsResult = dfsResult.prev
            # print()

            
            for i in range(4):
                row = curr.x + upDown[i]
                col = curr.y + leftRight[i]

                # Add valid child to fringe
                if (0 <= row < dim and 0 <= col < dim            # in matrix
                        and (maze[row][col] in (1, 2))           # status = open/goal
                        and ((row, col) not in visitedCoords)):  # not visited
                    fringe.append(Node(row, col, curr))

            visitedCoords.add((curr.x, curr.y))                  # mark current node as visited

    # Else: Goal Node not found, fringe empty
    return None