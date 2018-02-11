# Using the list retrieved from NarrowData, prepares data (re: arrays)
# to be used in Q2.

from datetime import datetime
import numpy as np

#def shuffleR(filename, lag):
def shuffle(dataX, start, lag):
    # returns x-Axis data, y-Axis data, lag#, and file name, x-axis, y-axis
    #dataX, dataY, xTitle, yTitle = getData(filename)
    #start = getStart()
    #print(start)
    start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    #print("into Loop:")
    count = 0
    for item in dataX:
        #print('')
        if (item == start):
            #print('match!')
            #print(item, start)
            break
        elif (item != start):
            #print('no match!')
            #print(item, start)
            count = count+1

    #print(count)
    # AND NOW WE ROLL
    '''
    print('')
    print('count: ', count)
    print("index: ", index)
    '''
    index = count - lag
    #dataX = np.roll(dataX, index)
    '''
    print('Initial Data:')
    for item in dataX:
       print(item)
    print('')
    '''
    # Delete off rolled stuff
    #print('Deleting off Rolled')
    n = 0
    while (n < index):
        dataX = np.delete(dataX, 0)
        n = n+1

    '''
    for item in dataX:
        print(item)
    '''
    return dataX

# Find out where in the data target[0] timestamp = second data[x]

#oname = 't3.csv'
#shuffle(oname, '2015-12-3 12:12:12', 2)