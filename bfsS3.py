import time
import copy
import random
from node import Node
from queue import Queue
from maze import showMaze
from firespread import spreadFire

# Account for x amount of fire steps ahead 

def initBFSS3(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS):
    ### CHANGE THIS TO SEE THE PREDICTIONS
    SHOW_VISUALIZATION = False
    RANGE_OF_ITERATIONS_TO_PREDICT = 7          # NEED TO CREATE A FUNCTION TO FIND A GOOD RANGE
    
    ### CONSTANTS
    GOAL = DIMENSIONS -1 
    agentDead = False
    startNode = Node(0,0)
    visited_fire_coordinates = {}               # Remembers where the fire has spread to
    
    predicted_fire_maze = copy.deepcopy(fireMaze)  
    

    while not agentDead:   
        predicted_fire_maze_list = [];
        ##### CREATES A NEW FIRE MAZE WHICH IS RANGE_OF_ITERATIONS_TO_PREDICT STEPS AHEAD OF THE CURRENT MAZE ####
        ##### NOTE: WE PREDICT THE PATH BY SETTING PROBABILITY_OF_PREDICTED_FIRE_SPREAD SPREAD TO 1 WHICH GAURANTEES THAT IT WILL SPREAD IN THAT DIRECTION
        for z in range(RANGE_OF_ITERATIONS_TO_PREDICT): 
            PROBABILITY_OF_PREDICTED_FIRE_SPREAD = 1  
            predicted_fire_maze, predictedFireCoordinates = spreadFireS3(predicted_fire_maze, DIMENSIONS, PROBABILITY_OF_PREDICTED_FIRE_SPREAD) 

            if len(predictedFireCoordinates) != 0:        # Update maze with where the fire has spreaded to
                for fire in predictedFireCoordinates:    
                    fx = fire[0]
                    fy = fire[1]
                    predicted_fire_maze[fx][fy] = 6 if SHOW_VISUALIZATION else 5    # 6 Shows us where the fire spread too for visualization
                predicted_fire_maze_list.append(copy.deepcopy(predicted_fire_maze))   # Add Predicted fire maze to list

        # print('Maze With Predicted Fire Path')
        showMaze(predicted_fire_maze, DIMENSIONS) if SHOW_VISUALIZATION else None


        # print('Run BFS on Maze With Predicted Fire Path')
        pathCoordinates = []                                            # Stores the path that BFS has found
        
        #### THIS PART IS BUGGY BUT ALLOWS FOR OVERRIDE AND TRAVEL TO AREAS WHERE WE PREDICTED THE FIRE WOULD BE ###
        # If the last prediction yields no results, try the maze prior to that
        tryAlternate = True
        mazes = len(predicted_fire_maze_list)
        while tryAlternate and len(predicted_fire_maze_list) != 0:
            bfsResult = BFS(predicted_fire_maze_list[mazes-1], startNode, DIMENSIONS)       # Get path with most recent fire prediction
            
            if bfsResult is not None:   # If we get a path, great                           
                break
            else:                       # If there is no path, try one prediction prior 
                del predicted_fire_maze_list[-1]
                # print('Trying again')
                mazes -= 1
        
        # Update Maze With Current Fire Location (Not The Prediction But Actual)
        if (bfsResult is not None):                                 # If A Path Was Found
            # print("BFS Path Found. Now checking Agent Status vs Fire...")

            while(bfsResult is not None):                           # Store Coordinates For Path Found
                pathCoordinates.append([bfsResult.x,bfsResult.y])
                bfsResult = bfsResult.prev

            ###### UPDATE AGENTS' CURRENT POSITION AND CHECK WHETHER IT REACHED THE GOAL
            pathCoordinates = [ele for ele in reversed(pathCoordinates)]        # Reverse the coordinate path Goal -> Start is not Start -> Goal Path
            agent_x_pos, agent_y_pos = pathCoordinates[1][0], pathCoordinates[1][1]
            fireMaze[agent_x_pos][agent_y_pos] = 4 

            # Check if agent made it to goal
            if agent_x_pos == GOAL and agent_y_pos == GOAL:
                print('Succesffully made it to goal')
                return 1
                break

            # Update agents' next position
            elif len(pathCoordinates) > 1:
                startNode = Node(agent_x_pos, agent_y_pos)   
    

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

            else:   
                print('[]') # If fire didn't spread                   
            
            ### UPDATE NEXT ITERATION WITH THE CURRENT COPY OF THE STATE OF THE AGENT AND FIRE
            predicted_fire_maze = copy.deepcopy(fireMaze)   

        else:   # New fire path results in no possible path to goal
            print('Could not find path where agent survives due to new fire path')
            agentDead = True
        # print("Current Maze")
    # showMaze(fireMaze, DIMENSIONS)

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
                    # elif maze[row][col] == PREDICTED_FIRE_SPACE:
                    #     fringe.put(Node(row, col, curr))

                # elif  (0 <= row < dim and 0 <= col < dim and (maze[row][col] == PREDICTED_FIRE_SPACE) and ((row, col) not in visitedCoords)):           # If their is no other path except the predicted fire path
                #     fringe.put(Node(row, col, curr))



            visitedCoords.add((curr.x, curr.y))                  # mark current node as visited

    # Else: Goal Node not found, fringe empty
    return None

# This allows us to visualize the predicted fire location

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


