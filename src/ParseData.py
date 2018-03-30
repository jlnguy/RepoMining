# Using the list retrieved from NarrowData, prepares data (re: arrays)
# to be used in Q2.

from datetime import datetime
import numpy as np

def shuffleDate(dataY, dataX, start, lag):
    # returns x-Axis data
    start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    count = 0
    for item in dataX:
        if (item == start):
            break
        elif (item != start):
            count = count+1

    # AND NOW WE ROLL

    index = count - lag
    #print('index: ', index)
    #dataX = np.roll(dataX, index)

    # Delete off rolled stuff
    n = 0
    while (n < index):
        dataX = np.delete(dataX, 0)
        dataY = np.delete(dataY, 0)
        n = n+1

    return dataX, dataY


def shuffleY(targetY, variableY, lag):
    length = len(variableY) - len(targetY)
    length = length - lag
    ctr = 0
    while (ctr < length):
        variableY.pop()
        ctr = ctr+1

    return variableY

def trimData(targetY, variableY):
    # trim according to how long targetY is.
    # idgaf bout variableY cuase it should be longer from going through NarrowData
    lenTar = len(targetY)
    ctr = len(variableY) - lenTar

    while(ctr > 0):
        variableY.pop()
        ctr = ctr - 1

    return variableY

