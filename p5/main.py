from bfs import initBFS
from dfs import initDFS
from aStar import initAStar
from maze import createMaze, showMaze, updateMaze

from codetiming import Timer

def main():
    PROBABILITY_OF_BLOCK = 0.3
    dfsFail = -1
    bfsFail = -1
    astarFail = -1

    t = Timer(name="class")

    underMinute = True

    d = 3635
    # DFS Timing
    while(underMinute):
        d = d + 2
        unsolved = True
        while(unsolved):
            print('DIMENSION: ' + str(d))
            MAZE = createMaze(d, PROBABILITY_OF_BLOCK)  # Create the maze
            t.start()
            if(initDFS(MAZE, d)):
                unsolved = False
            if (t.stop() > 60):
                underMinute = False
                print("DFS Failed 60s Test at dimension d = " + str(d))
                dfsFail = d

    d = 2200
    underMinute = True
    # BFS Timing
    while(underMinute):
        d = d + 22
        unsolved = True
        while(unsolved):
            print('DIMENSION: ' + str(d))
            MAZE = createMaze(d, PROBABILITY_OF_BLOCK)  # Create the maze
            t.start()
            if(initBFS(MAZE, d)):
                unsolved = False
            if (t.stop() > 60):
                underMinute = False
                print("BFS Failed 60s Test at dimension d = " + str(d))
                bfsFail = d

    d = 5000
    underMinute = True
    # AStar Timing
    while(underMinute):
        d = d + 11
        unsolved = True
        while(unsolved):
            print('DIMENSION: ' + str(d))
            MAZE = createMaze(d, PROBABILITY_OF_BLOCK)  # Create the maze
            t.start()
            if(initAStar(MAZE, d)):
                unsolved = False
            if (t.stop() > 60):
                underMinute = False
                print("AStar Failed 60s Test at dimension d = " + str(d))
                astarFail = d


    print('DFS Fail: ' + str(dfsFail))
    print('BFS Fail: ' + str(bfsFail))
    print('A* Fail: ' + str(astarFail))     


main()