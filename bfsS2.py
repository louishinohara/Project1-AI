import time
import copy
from bfs import BFS
from node import Node
from queue import Queue
from maze import showMaze
from firespread import spreadFire


def initBFSS2(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS):
    GOAL = DIMENSIONS -1 
    agentDead = False
    startNode = Node(0,0)
    visited_fire_coordinates = {}           # Remembers where the fire has spread to

    while not agentDead:                    
        pathCoordinates = []                                        # Stores the path that BFS has found
        bfsResult = BFS(fireMaze, startNode, DIMENSIONS)          # Call BFS

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
