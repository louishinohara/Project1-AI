from node import Node
from queue import Queue

# BFS: takes in a start node and the dimensions (for the goal),
# outputs result node w/ path accessible via result.prev

def initBFS(maze,dimensions):
    bfsResult = BFS(maze, Node(0,0), dimensions)
    if (bfsResult is not None):
        print("--BFS Goal Path--")
        bfsResultsCopy = bfsResult
        # while(bfsResult is not None):
        #     print('(' + str(bfsResult.x) + ', ' + str(bfsResult.y) + ') <- ', end='')   # why does this print only after exiting matplotlib?
        #     bfsResult = bfsResult.prev
        return bfsResultsCopy
    else:
      print("BFS found no solution")
    return None

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







      