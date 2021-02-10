import time
import copy
from node import Node
from queue import Queue
from maze import showMaze
from firespread import spreadFire

# Account for x amount of fire steps ahead 

def initBFSS3(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS):
    GOAL = DIMENSIONS -1 
    RANGE_OF_ITERATIONS_TO_PREDICT = 3
    agentDead = False
    startNode = Node(0,0)
    visited_fire_coordinates = {}           # Remembers where the fire has spread to
    
    predicted_fire_maze = copy.deepcopy(fireMaze)  
    predicted_visited_fire_coordinates = {}

    while not agentDead:   
        
        #### NOTE: NEED TO ACCOUNT FOR EDGE CASE THAT PREDICTION LEADS TO NO PATH EVEN THO THAT SPOT IS NOT ON FIRE YET BECAUSE IT IS PREDICTION
        #### NOTE: HOWEVER ACCORIDNG TO THE CURRENT ALGORITHM, THAT SPACE WILL 'BE ON FIRE' SO IT WON'T TAKE THAT ROUTE

        ##### CREATE A NEW FIRE MAZE WHICH IS RANGE_OF_ITERATIONS_TO_PREDICT STEPS AHEAD OF THE CURRENT MAZE ####
        ##### NOTE: WE PREDICT THE PATH BY SETTING PROBABILITY_OF_PREDICTED_FIRE_SPREAD SPREAD TO 1 WHICH GAURANTEES THAT IT WILL SPREAD IN THAT DIRECTION
        for z in range(RANGE_OF_ITERATIONS_TO_PREDICT):  # This loop could give us the maze which is x steps ahead
            PROBABILITY_OF_PREDICTED_FIRE_SPREAD = 1  # Want to maximize possibility that the fire is spreading
            predicted_fire_maze, predictedFireCoordinates = spreadFire(predicted_fire_maze, DIMENSIONS, PROBABILITY_OF_PREDICTED_FIRE_SPREAD) 
            # Update Fire Location and Check if agent is still alive
            if len(predictedFireCoordinates) != 0:        # Update maze with where the fire has spreaded too
                for fire in predictedFireCoordinates:    
                    fx = fire[0]
                    fy = fire[1]
                    print(predictedFireCoordinates)
                # Check if visited or not
                    if fx not in predicted_visited_fire_coordinates:                  # Create and add coordinate key
                        predicted_visited_fire_coordinates[fx] = [fy]
                    else:
                        predicted_visited_fire_coordinates[fx].append(fy)             # Add visited value

                    predicted_fire_maze[fx][fy] = 5        # Otherwise spot is now on fire
            print('Creating Fire Maze with Predicted Values')
            showMaze(predicted_fire_maze, DIMENSIONS)


        print('BFS Search with predicted fire maze')
        pathCoordinates = []                                      # Stores the path that BFS has found
        bfsResult = BFS(predicted_fire_maze, startNode, DIMENSIONS)   # Call BFS        -> Send in a modified version of the fireMaze where we account for 2 - 3 steps ahead
                                                                  # However we still need to account for the original fire maze
        # Update Maze With Current Fire Location (Not The Prediction But Actual)
        predicted_fire_maze = copy.deepcopy(fireMaze)
        if (bfsResult is not None):                                 # If A Path Was Found
            print("BFS Path Found. Now checking Agent Status vs Fire...")

            while(bfsResult is not None):                           # Store Coordinates For Path Found
                pathCoordinates.append([bfsResult.x,bfsResult.y])
                bfsResult = bfsResult.prev

            ###### UPDATE AGENTS' CURRENT POSITION AND WHETHER IT REACHED THE GOAL
            pathCoordinates = [ele for ele in reversed(pathCoordinates)]        # Reverse the coordinate path Goal -> Start is not Start -> Goal Path
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
    



            ######################### UPDATE FIRE LOCATION AND CHECK AGENTS' STATUS #######################
            updatedFireMaze, newFireCoordinates = spreadFire(fireMaze, DIMENSIONS, PROBABILITY_OF_FIRE_SPREAD)    # Get FireMaze For This Iteration

            if len(newFireCoordinates) != 0:        
                for fire in newFireCoordinates:     # Update maze with where the fire has spreaded to 
                    fx = fire[0]
                    fy = fire[1]

                # Check if visited or not
                    if fx not in visited_fire_coordinates:                  # Create and add coordinate key
                        visited_fire_coordinates[fx] = [fy]
                    else:
                        visited_fire_coordinates[fx].append(fy)             # Add visited value

                # Check if Agent is Burned Else That Spot Is On Fire  
                    if agent_x_pos in visited_fire_coordinates and agent_y_pos in visited_fire_coordinates[fx]: 
                        agentDead = True
                        print('Agent Burned at x: ' + str(fx) + ' y: ' + str(fy))

                    else:
                        fireMaze[fx][fy] = 5        # Otherwise spot is now on fire


                print('Reseting Firemaze to Actual Maze')
            else:   
                print('[]') # If fire didn't spread                   

        else:   # New fire path results in no possible path to goal
            print('Could not find path where agent survives due to new fire path')
            agentDead = True

        showMaze(fireMaze, DIMENSIONS)


# Have our BFS Algorithm which takes in the fire maze -> Returns path to goal
# New param into our BFS algorithm is the fire maze but 2 - 3 steps ahead. 
# Or just assume that 3 spaces around each area on fire is already burning


def BFS(maze, startNode, dim):
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
                if (0 <= row < dim and 0 <= col < dim and (maze[row][col] in (1, 2, 4)) and ((row, col) not in visitedCoords)):  # in matrix # status = open/goal # not visited
                    fringe.put(Node(row, col, curr))

            visitedCoords.add((curr.x, curr.y))                  # mark current node as visited

    # Else: Goal Node not found, fringe empty
    return None