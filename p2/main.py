from dfs import initDFS
from maze import createMaze, showMaze, updateMaze

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def main():
    DIMENSIONS = 1000
    
    pArray = np.arange(0.0, 1.02, 0.02)
    print(pArray)

    y = []
    
    for p in pArray:
        solved = []
        for _ in range(5):
            MAZE = createMaze(DIMENSIONS, p)  # Create the maze
            
            if (initDFS(MAZE, DIMENSIONS)): # if DFS can solve it
                solved.append(1)
            else:
                solved.append(0)

        y.append(np.mean(solved))   # y contains P(solved with P(blocked) = p)

    fig, ax = plt.subplots()
    ax.plot(pArray, y)

    ax.set(xlabel='Obstacle Density (p)', ylabel='Probability that S can be reached from G’',
        title='Obstacle Density vs Solvability')
    ax.grid()

    fig.savefig("p2.png")
    plt.show()


main()



# # Data for plotting
# t = np.arange(0.0, 1.0, 0.05)
# s = 1 + np.sin(2 * np.pi * t)

# fig, ax = plt.subplots()
# ax.plot(t, s)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()

# fig.savefig("test.png")
# plt.show()