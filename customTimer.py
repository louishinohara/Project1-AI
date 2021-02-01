import time
import threading
from multiprocessing import Process

# Function to trigger call back to execute after x seconds
def setOneMinuteTimer(keepGoing): 
    keepGoing[0] = False
    return True

# Function to display the ellapsed time
def showElapsedTime(start, keepGoing):
    while keepGoing[0]:
        print(str(round(time.time() - start)) + 'seconds ellapsed.')
        time.sleep(1)

# Function which executes for x seconds 
def timedFunction(func, keepGoing):
    while keepGoing[0]:
        done = func
        if done:
            keepGoing[0] = False
    print('Operation Completed')

def customTimer(func):
    keepGoing = [True]
    start = time.time()
    timer = threading.Timer(60, setOneMinuteTimer, args=(keepGoing,)) 
    timer.start() 

    p1 = Process(target=showElapsedTime(start, keepGoing))
    p2 = Process(target=timedFunction(func, keepGoing))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()
    elapsedTime = end - start
    print('The elapsed time is: ' + str(round(elapsedTime)) + ' seconds.' )    