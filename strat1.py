import time
import copy
from bfs import BFS
from node import Node
from queue import Queue
from maze import showMaze
from firespread import spreadFire


def initStrat1(fireMaze, PROBABILITY_OF_FIRE_SPREAD, DIMENSIONS):
    agentDead = False
    pathCoordinates = []
    fireCoordinates = []
    fireMazeCopy = copy.deepcopy(fireMaze)      # Want to save original maze
    result = BFS(fireMaze, Node(0,0), DIMENSIONS)

    if (result is not None):                 # If path was succesfully found
        print("BFS Path Found. Now checking Agent Status vs Fire...")

        while(result is not None):           # Getting coordinates for path
            pathCoordinates.append([result.x,result.y])
            result = result.prev

        # Reverse the coordinate path Goal -> Start is not Start -> Goal Path
        pathCoordinates = [ele for ele in reversed(pathCoordinates)]        
        del pathCoordinates[0]                          # Want the first move to be the agent moving      

        for i in range(len(pathCoordinates)):           # Create Fire Spread and get the spots it spreads to for each iteration
            updatedFireMaze, newFireCoordinates = spreadFire(fireMazeCopy, DIMENSIONS, PROBABILITY_OF_FIRE_SPREAD)    # Get fire maze matrix and coordinates that it spread to per iteration
            fireCoordinates.append(newFireCoordinates)  # Save the coordinate it spread to for that iteration
            fireMazeCopy = updatedFireMaze.copy()           # Update the returned maze with fire

        visited_fire_coordinates = {}           # Remembers where the fire has spread to

        for j in range(0,len(fireCoordinates)):   # Iterate through fire spread coordinates to see if there is intersection with agent
            if agentDead:      
                print('Agent Died')
                break

            agent_x_pos = pathCoordinates[j][0]
            agent_y_pos = pathCoordinates[j][1]
            fireMaze[agent_x_pos][agent_y_pos] = 4  # Update Agent's current location

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
                        fireMaze[fx][fy] = 5        # Otherwise spot is now on fire
            
            else:
                print('[]')     # Fire did not spready this iteration
            
        showMaze(fireMaze,DIMENSIONS)

        if not agentDead:
            print('Agent Has Succesffuly Made It Out Of Maze')
            return 1
    else:
      print("BFS found no solution")
    return None
