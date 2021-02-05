import time
from node import Node
from queue import Queue
from firespread import spreadFire
from maze import showMaze

def initDFSS1(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS):
    startNode = Node(0,0)
    fringe = []
    visitedCoords = set()
    keepGoing = True
    start_time = time.time() 


    # Keeps goign while length of fringe is not empty
    while (keepGoing):                                                # Spreads fire. Need to modify path finding alg code to do certain things
        testMaze = spreadFire(fireMaze, DIMENSIONS, PROBABILITY_OF_FIRE_SPREAD)
        dfsResult = DFSS1(fireMaze, startNode, DIMENSIONS, fringe, visitedCoords)
                    # Return fireMaze, currentNode, dimensions, fringe, visitedCOords? and status (Found, Unfound, fire)
        fireMaze = testMaze.copy()
        showMaze(fireMaze, DIMENSIONS)




    print("--- %s seconds ---" % (time.time() - start_time))

    if (dfsResult is not None):
        print("--DFS Goal Path--")
        dfsResultsCopy = dfsResult

        return dfsResultsCopy        # Return Result of Coordinates
    else:
      print("DFS found no solution")
    return None                 # Return Result as None

def DFSS1(maze, startNode, dim, fringe, visitedCoords):     # Need to somehome iterate while fringe is not empty
    GOAL_NODE_NOT_FOUND = -1
    fringe.append(startNode)
                                # Also must return start node

    # Coordinate Stuff
    leftRight = [1, 0, 0, -1]
    upDown = [0, 1, -1, 0]

    curr = fringe.pop()

    if(curr.x == (dim-1) and curr.y == (dim-1)):    # Goal Node Found
        return curr

    elif((curr.x, curr.y) not in visitedCoords):    # Process New Node's Neighbors
        
        for i in range(4):
            row = curr.x + upDown[i]
            col = curr.y + leftRight[i]

            # Add valid child to fringe
            if (0 <= row < dim and 0 <= col < dim            # in matrix
                    and (maze[row][col] in (1, 2))           # status = open/goal
                    and ((row, col) not in visitedCoords)):  # not visited
                fringe.append(Node(row, col, curr))

        visitedCoords.add((curr.x, curr.y))                  # mark current node as visited

    elif (len(fringe == 0)):    # Goal Node Not Found
        return GOAL_NODE_NOT_FOUND

        # Elif: Goal Node not found, fringe empty ( Fringe == 0)
        # Elif we reach a node that has fire 


    return None



# Outer loop runs until goal is found, not found or encounter fire  -> Return Found, Not Found, Dead
# Pass in fire maze -> DFS Runs One Step -> returns fringe, startNode, visitedCoords
# Update fire maze -> Next Iteration -> DFS Runs -> Pass in previous fringe, start node, visited coords





      