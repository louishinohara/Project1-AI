import time
import copy
import random
from node import Node
from queue import Queue
from maze import showMaze
from firespread import spreadFire

# Account for x amount of fire steps ahead 

def initBFSS3(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS):
    GOAL = DIMENSIONS -1 
    RANGE_OF_ITERATIONS_TO_PREDICT = 2
    agentDead = False
    startNode = Node(0,0)
    visited_fire_coordinates = {}           # Remembers where the fire has spread to
    
    predicted_fire_maze = copy.deepcopy(fireMaze)  
    predicted_visited_fire_coordinates = {}

    while not agentDead:   
        
        ##### CREATE A NEW FIRE MAZE WHICH IS RANGE_OF_ITERATIONS_TO_PREDICT STEPS AHEAD OF THE CURRENT MAZE ####
        ##### NOTE: WE PREDICT THE PATH BY SETTING PROBABILITY_OF_PREDICTED_FIRE_SPREAD SPREAD TO 1 WHICH GAURANTEES THAT IT WILL SPREAD IN THAT DIRECTION
        for z in range(RANGE_OF_ITERATIONS_TO_PREDICT):  # This loop could give us the maze which is x steps ahead
            PROBABILITY_OF_PREDICTED_FIRE_SPREAD = 1  # Want to maximize possibility that the fire is spreading
            predicted_fire_maze, predictedFireCoordinates = spreadFireS3(predicted_fire_maze, DIMENSIONS, PROBABILITY_OF_PREDICTED_FIRE_SPREAD) 
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

                    predicted_fire_maze[fx][fy] = 6        # Otherwise spot is now on fire
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

#### NOTE: IN BFS NEED TO MAKE THE AGENT PASS THROUGH A PREDICTED FIRE SPACE IF THAT IS THE ONLY OPTION AVAILABLE
# THIS BFS HAS A PREFERENCE TO WHICH NODES IT CHOOSES TO MOVE TO
def BFS(maze, startNode, dim):
    fringe = Queue()
    fringe.put(startNode)
    visitedCoords = set()
    GOAL = 1
    OPEN_SPACE = 2
    AGENT_PATH = 4
    PREDICTED_FIRE_SPACE = 6


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
                if (0 <= row < dim and 0 <= col < dim and (maze[row][col] in (GOAL, OPEN_SPACE, AGENT_PATH)) and ((row, col) not in visitedCoords)):  # in matrix # status = open/goal # not visited
                    
                    if maze[row][col] in (GOAL, OPEN_SPACE): # Prefer nodes that are goal -> open -> current path -> predicted fire path, 
                        fringe.put(Node(row, col, curr))
                    elif maze[row][col] == AGENT_PATH:
                        fringe.put(Node(row, col, curr))

                # elif  (0 <= row < dim and 0 <= col < dim and (maze[row][col] == PREDICTED_FIRE_SPACE) and ((row, col) not in visitedCoords)):           # If their is no other path except the predicted fire path
                #     fringe.put(Node(row, col, curr))



            visitedCoords.add((curr.x, curr.y))                  # mark current node as visited

    # Else: Goal Node not found, fringe empty
    return None


def spreadFireS3(maze, dimensions, q):    # Params are the maze (and updated fire maze from last iteration), dimensions, probability of fire spread
    mazeCopy = copy.deepcopy(maze)      # Need to make copy so current iteration results don't affect results of current iterations' coordinates that appear later 
    FREE_SPACE = 2
    BLOCKED_SPACE = 3
    FIRE_SPACE = 5
    PREDICTED_FIRE_SPACE = 6
    fire_coordinate = []            # Coordinates of where the fire spread to this iteration
    for x in range(dimensions):     # Mapping through entire matrix for coord on fire
        for y in range(dimensions):

            coordinate = maze[x][y] 
            
            if (coordinate == FREE_SPACE and coordinate != BLOCKED_SPACE and coordinate != FIRE_SPACE): # Only applies for free spaces, unblock spaces, and non fire spaces

                #for each cell, check how many neighbors on fire
                neighbors_on_fire = 0
                leftRight = [1, 0, 0, -1]
                upDown = [0, 1, -1, 0]

                for i in range(4):
                    row = x + upDown[i]
                    col = y + leftRight[i]

                    if (0 <= row < dimensions and 0 <= col < dimensions and (maze[row][col] == FIRE_SPACE or maze[row][col] == PREDICTED_FIRE_SPACE)): # in Matrix and status = on fire or predicted fire space
                        neighbors_on_fire += 1

                prob = 1 - ((1 - q) ** neighbors_on_fire)   # Probability that this coord will catch on fire

                if (random.random() <= prob):               # Execute probability
                    mazeCopy[x][y] = FIRE_SPACE
                    fire_coordinate.append([x,y]) 
    return mazeCopy, fire_coordinate 


