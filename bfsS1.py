import time
from node import Node
from queue import Queue
from maze import showMaze
from firespread import spreadFire
import copy

def initBFSS1(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS):
    fireMazeCopy = copy.deepcopy(fireMaze)
    agentDead = False
    pathCoordinates = []
    fireCoordinates = []

    bfsResult = BFSS1(fireMaze, Node(0,0), DIMENSIONS)

    if (bfsResult is not None):                 # If path was succesfully found
        print("BFS Path Found. Now checking Agent Status vs Fire...")

        while(bfsResult is not None):           # Getting coordinates for path
            pathCoordinates.append([bfsResult.x,bfsResult.y])
            bfsResult = bfsResult.prev

        for i in range(len(pathCoordinates)):   # Create Fire Spread and get the spots it spreads to for each iteration
            updatedFireMaze, newFireCoordinates = spreadFire(fireMaze,DIMENSIONS,PROBABILITY_OF_FIRE_SPREAD)    # Get fire maze matrix and coordinates that it spread to per iteration
            fireCoordinates.append(newFireCoordinates)  # Save the coordinate it spread to for that iteration
            fireMaze = updatedFireMaze.copy()           # Update the returned maze with fire

        pathCoordinates = [ele for ele in reversed(pathCoordinates)]        # Reverse the coordinate path Goal -> Start is not Start -> Goal Path
        visited_fire_coordinates = {}                                       # Remembers where the fire has spread to

        for j in range(len(fireCoordinates)):   # Iterate through fire spread coordinates to see if there is intersection with agent
            if agentDead:       # End loop with agent is dead
                break

            agent_x_pos = pathCoordinates[j][0]
            agent_y_pos = pathCoordinates[j][1]
            fireMazeCopy[agent_x_pos][agent_y_pos] = 4  # Update Agent's current location

            curr_fire = fireCoordinates[j]              # Get the current location where the fire is spreading to

            if (len(curr_fire) != 0):                   # If the fire spread this iteration
                print("Fire spread to " + str(curr_fire) )                        # Coordinate's it spread to

                for c in curr_fire:                     # Each coordinate it spread to
                    fx = c[0]   # X Fire Coord
                    fy = c[1]   # Y Fire Coord

                    if fx not in visited_fire_coordinates:                  # Create and add coordinate key
                        visited_fire_coordinates[fx] = [fy]
                    else:
                        visited_fire_coordinates[fx].append(fy)             # Add visited value

                    if agent_x_pos in visited_fire_coordinates and agent_y_pos in visited_fire_coordinates[fx]: # Check if current agent is on a spot on fire
                        agentDead = True
                        print('Agent Burned at x: ' + str(fx) + ' y: ' + str(fy))
                        break
                    else:
                        fireMazeCopy[fx][fy] = 5        # Otherwise spot is now on fire
            
            else:
                print('[]')     # Fire did not spready this iteration
            
            showMaze(fireMazeCopy,DIMENSIONS)

        if not agentDead:
            print('Agent Has Succesffuly Made It Out Of Maze')
    else:
      print("BFS found no solution")
    return None

# Function to create the BFS Path
def BFSS1(maze, startNode, dim):
    fringe = Queue()
    fringe.put(startNode)
    visitedCoords = set()

    leftRight = [1, 0, 0, -1]
    upDown = [0, 1, -1, 0]

    while(not fringe.empty()):
        curr = fringe.get()

        if(curr.x == (dim-1) and curr.y == (dim-1)):  # Goal Node Found
            return curr

        elif((curr.x, curr.y) not in visitedCoords):  # Process New Node's Neighbors
            
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
    