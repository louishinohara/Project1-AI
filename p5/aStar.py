from node import Node, aStarNode
from queue import PriorityQueue

def initAStar(maze,dimensions):
    aStarResult = aStar(maze, Node(0,0), dimensions)
    if (aStarResult is not None):
        print("--A* Goal Path--")
        # while(aStarResult is not None):
        #     print('(' + str(aStarResult.x) + ', ' + str(aStarResult.y) + ') <- ', end='')   # why does this print only after exiting matplotlib?
        #     aStarResult = aStarResult.prev
        return True
    else:
        print("A* found no solution")
        return False


# aStar: takes in a start node and the dimensions (for the goal),
# outputs result node w/ path accessible via result.prev

def aStar(maze, startNode, dim):
    fringe = PriorityQueue()
    visitedCoords = set()
    qNum = 1    # used for PriorityQueue tiebreaks
    
    aStar_start = aStarNode(startNode.x, startNode.y, 0, dim)
    fringe.put((aStar_start.f, qNum, aStar_start))     # startNode priority = distance from start to goal
    qNum = qNum + 1
    
    # These arrays are used to get row and column
    # numbers of 4 neighbours of a given cell
    # (From GFG: https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/)
    leftRight = [1, 0, 0, -1]
    upDown = [0, 1, -1, 0]

    while(not fringe.empty()):
        curr = fringe.get()[2]

        if(curr.x == (dim-1) and curr.y == (dim-1)):  # Goal Node Found
            return curr

        elif((curr.x, curr.y) not in visitedCoords):  # Process Highest Priority Node's Neighbors
            # # Printing Path (debugging)
            # print("Processing coords: " + str(curr.x) + " " + str(curr.y))
            # aStarResult = curr
            # print('Processing Path: ', end='')
            # while(aStarResult is not None):
            #   print('(' + str(aStarResult.x) + ', ' + str(aStarResult.y) + ') <- ', end='')
            #   aStarResult = aStarResult.prev
            # print()
            
            for i in range(4):
                row = curr.x + upDown[i]
                col = curr.y + leftRight[i]

                # Add valid child to fringe
                if (0 <= row < dim and 0 <= col < dim            # in matrix
                        and (maze[row][col] in (1, 2))           # status = open/goal
                        and ((row, col) not in visitedCoords)):  # not visited
                    childNode = aStarNode(row, col, curr.g+1, dim, curr)
                    fringe.put((childNode.f, qNum, childNode))
                    qNum = qNum + 1

            visitedCoords.add((curr.x, curr.y))                  # mark current node as visited   

    # Else: Goal Node not found, fringe empty
    return None

def aStar1(maze, startNode, dim):
    fringe = PriorityQueue()
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
            # aStarResult = curr
            # print('Processing Path: ', end='')
            # while(aStarResult is not None):
            #   print('(' + str(aStarResult.x) + ', ' + str(aStarResult.y) + ') <- ', end='')
            #   aStarResult = aStarResult.prev
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