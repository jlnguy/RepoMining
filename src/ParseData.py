# Using the list retrieved from NarrowData, prepares data (re: arrays)
# to be used in Q2.

from datetime import datetime
import numpy as np

def shuffleDate(dataX, start, lag):
    # returns x-Axis data, y-Axis data, lag#, and file name, x-axis, y-axis
    start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    count = 0
    for item in dataX:
        if (item == start):
            break
        elif (item != start):
            count = count+1

    # AND NOW WE ROLL

    index = count - lag
    #dataX = np.roll(dataX, index)

    # Delete off rolled stuff
    n = 0
    while (n < index):
        dataX = np.delete(dataX, 0)
        n = n+1

    return dataX

def shuffleY(targetY, variableY, lag):
    length = len(variableY) - len(targetY)
    length = length - lag
    ctr = 0
    while (ctr < length):
        variableY = np.delete(variableY, 0)
        ctr = ctr+1

    return variableY

def trimData(targetY, variableY):
    # trim according to how long targetY is.
    # idgaf bout variableY cuase it should be longer from going through NarrowData
    lenTar = len(targetY)
    ctr = len(variableY) - lenTar
    while(ctr > 0):
        variableY = np.delete(variableY, len(variableY) - 1)
        ctr = len(variableY) - lenTar
    return variableY
