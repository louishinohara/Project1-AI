import time
import copy
# from bfs import BFS
from node import Node
from queue import Queue
from maze import showMaze
from firespread import spreadFire

# Account for x amount of fire steps ahead 

def initBFSS3(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS):
    GOAL = DIMENSIONS -1 
    agentDead = False
    startNode = Node(0,0)
    visited_fire_coordinates = {}           # Remembers where the fire has spread to

    while not agentDead:                    
        pathCoordinates = []                                      # Stores the path that BFS has found
        bfsResult = BFS(fireMaze, startNode, DIMENSIONS)          # Call BFS        -> Send in a modified version of the fireMaze where we account for 2 - 3 steps ahead
                                                                  # However we still need to account for the original fire maze

        if (bfsResult is not None):                                 # If A Path Was Found
            print("BFS Path Found. Now checking Agent Status vs Fire...")

            while(bfsResult is not None):                           # Store Coordinates For Path Found
                pathCoordinates.append([bfsResult.x,bfsResult.y])
                bfsResult = bfsResult.prev

            # Update agent's current position
            pathCoordinates = [ele for ele in reversed(pathCoordinates)]        # Reverse the coordinate path Goal -> Start is not Start -> Goal Path
           #  print(pathCoordinates)
            agent_x_pos, agent_y_pos = pathCoordinates[1][0], pathCoordinates[1][1]
            fireMaze[agent_x_pos][agent_y_pos] = 4 

            # Check if agent made it to goal
            if agent_x_pos == GOAL and agent_y_pos == GOAL:
                print('Succesffully made it to goal')
                break

            # Update agents' next position
            elif len(pathCoordinates) > 1:
                startNode = Node(agent_x_pos, agent_y_pos)   
                print('Set new start node as x: ' + str(agent_x_pos) + 'y: ' + str(agent_y_pos))
    
            updatedFireMaze, newFireCoordinates = spreadFire(fireMaze, DIMENSIONS, PROBABILITY_OF_FIRE_SPREAD)    # Get fire maze matrix and coordinates that it spread to per iteration

            ##### CREATE A NEW FIRE MAZE WHICH IS 2 - 3 STEPS AHEAD OF THE CURRENT MAZE ############
            predictFireMaze = copy.deepcopy(updatedFireMaze)
            for i in range(3):  # This loop could give us the maze which is x steps ahead
                PROBABILITY_OF_FIRE_SPREAD = 1  # Want to maximize possibility that the fire is spreading
                predictFireMaze, predictedFireCoordinates = spreadFire(predictFireMaze, DIMENSIONS, PROBABILITY_OF_FIRE_SPREAD) 
            #### NEED TO ACCOUNT FOR EDGE CASE THAT PREDICTION LEADS TO NO PATH EVEN THO THAT SPOT IS NOT ON FIRE YET BECAUSE IT IS PREDICTION
            #### HOWEVER ACCORIDNG TO THE CURRENT ALGORITHM, THAT SPACE WILL 'BE ON FIRE' SO IT WON'T TAKE THAT ROUTE
            #### 



            # Update Fire Location and Check if agent is still alive
            # print(newFireCoordinates)
            if len(newFireCoordinates) != 0:        # Update maze with where the fire has spreaded too
                for fire in newFireCoordinates:    
                    fx = fire[0]
                    fy = fire[1]

                # Check if visited or not
                    if fx not in visited_fire_coordinates:                  # Create and add coordinate key
                        visited_fire_coordinates[fx] = [fy]
                    else:
                        visited_fire_coordinates[fx].append(fy)             # Add visited value

                # Check if current agent is on a spot on fire   
                    if agent_x_pos in visited_fire_coordinates and agent_y_pos in visited_fire_coordinates[fx]: 
                        agentDead = True
                        print('Agent Burned at x: ' + str(fx) + ' y: ' + str(fy))

                    else:
                        fireMaze[fx][fy] = 5        # Otherwise spot is now on fire
                        print('Coordinate Added')

            else:   # If fire didn't spread
                print('[]')                         

        else:   # New fire path results in no possible path to goal
            print('Could not find path where agent survives due to new fire path')
            agentDead = True

        showMaze(fireMaze,DIMENSIONS)


# Have our BFS Algorithm which takes in the fire maze -> Returns path to goal
# New param into our BFS algorithm is the fire maze but 2 - 3 steps ahead. 
# Or just assume that 3 spaces around each area on fire is already burning


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
                        and (maze[row][col] in (1, 2, 4 ))       # status = open/goal
                        and ((row, col) not in visitedCoords)):  # not visited
                    fringe.put(Node(row, col, curr))

            visitedCoords.add((curr.x, curr.y))                  # mark current node as visited

    # Else: Goal Node not found, fringe empty
    return None