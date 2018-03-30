# Question 2
# ----------
# Takes results from NarrowData, shuffles it, and then visualizes it
# Figure 1: Displays data of top-k variables against target variable with lag times
# Figure 2: Displays correlation of top-k variables against target variable correlation
# Figure 3: Displays top-1 correlation values for each lag time

# To do: Color code negative correlation(?) Milestone 6

from NarrowData import getID, getTargetID, getTargetFirst, getGranularityType
from ParseData import shuffleDate, shuffleY, trimData
from ParseComma import getData, convertData
from Q3 import calculateTarget
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def correlation(xlist, ylist):
    xbar = np.mean(xlist)
    ybar = np.mean(ylist)
    xstd = np.std(xlist)
    ystd = np.std(ylist)
    num = 0.0

    lenX = len(xlist) - 1
    lenY = len(ylist) - 1
    '''
    print(len(xlist), len(ylist))
    print(lenX, lenY)'''
    count = 0
    comp = 0
    if (lenX < lenY):
        comp = lenX
    elif(lenY < lenX):
        comp = lenY

    while (count < comp):
        num = num + (xlist[count] - xbar) * (ylist[count] - ybar)
        count = count+1
    corr = num / ((len(xlist) - 1) * xstd * ystd)
    return corr


# ------------- Part i -------------
# |                                |
# |        Perform NarrowData      |
# |      Calculate correlation     |
# |                                |
# ----------------------------------

# set file as another one later.
targetFile = 't15.csv'
# Run with t18, t7, t4, or t15

# Works with t7 and t4. Date: 1/11/18
# Works with Q2_DJIA.csv, Q2_NASDAQ.csv. Date: 2/25/18
tags = [0]
targetX, targetY, titleX, titleY = getData(targetFile)
targetXconv = convertXData(targetX)
targetID = getTargetID(targetFile)
granularity = getGranularityType(targetID)
targetStart = getTargetFirst(targetID)
yStart = targetY[0]

'''
print('targetX: ', targetX)
print('targetY: ', targetY)
print('')

print('granularity: ', granularity)
'''

# Arbitrarily set lag as 5
#lag = 5
lag = 3

# Arbitrarily set top-k number to 3;
top_k = 3   # Pretend this is user specifying they want top-k of 3
top_k = top_k - 1   # fix up top_k variable to be index 0 instead of 1; done.

#print('fileID:', targetFile, "ID number: ", targetID)
#print('start: ', targetStart)

#listOfNarrowDataIDs = getID(targetFile, granularity, tags, lag)
listOfNarrowDataIDs = getID(targetFile, tags, lag, granularity)

print('List of Files: ', listOfNarrowDataIDs)
print('Number of files to be analyzed: ', len(listOfNarrowDataIDs))
print('')

if(len(listOfNarrowDataIDs) == 0):
    print('No values found with NarrowData (granularity)')
if(len(listOfNarrowDataIDs) < top_k):
    print('Not enough values found with NarrowData (granularity)')
# Lists to store arbitrary information about csvs
# list = [filename, xaxis, yaxis]
axisData = [[targetFile, titleX, titleY]]

# [target, id#, lag, correlation]
# Pad the multidimensional matrix with 0's
corrMatrix = [[0,0,0,0,0]]

ctr = lag
for item in listOfNarrowDataIDs:
    '''print('---------------')'''
    numberID = getTargetID(item)
    itemX, itemY, item_TitleX, item_TitleY = getData(item)
    trun = item_TitleY[:6]
    axisData = np.append(axisData, [[item, item_TitleX, item_TitleY]], 0)
    '''
    print('')
    print('itemX: ', itemX)
    print('itemY: ', itemY)
    print('initial length: ', len(itemX), len(itemY))
    print('')

    print('item: ', item)'''
    while(ctr >= 0):
        tempY = itemY
        tempX = itemX
        shuffledX, shuffledY = shuffleDate(tempY, tempX, targetStart, ctr)
        shuffledX = convertXData(shuffledX)
        '''print('shuffledX: ', shuffledX)
        print('shuffledY: ', shuffledY)
        print('Lag: ', ctr)

        print('lengthX: ', len(shuffledX),'lengthY: ', len(shuffledY))
        '''
        corr = correlation(shuffledY, targetY)

        # True if positive, False if negative
        if (corr > 0):
            color = True
        elif (corr < 0):
            color = False

        # Absolute Value
        corr = abs(corr)
        '''print('correlation: ', corr)'''

        corrMatrix = np.append(corrMatrix, [[item, numberID, ctr, corr, color]], 0)
        ctr = ctr-1
    ctr = lag

corrMatrix = np.delete(corrMatrix, 0, 0) # Remove the padded row [0,0,0,0]

#print(corrMatrix)

# find the top-k variables

corrSort = sorted(corrMatrix, key=lambda x: x[3], reverse=True)

# ------------- Part ii ------------
# |                                |
# |        Find top-k values       |
# |                                |
# ----------------------------------

ctr = 0
inc = 0
# topCorrValues = length of top_k, [target, id#, lag, correlation]
# Assume top_k is 3.
topCorrValues = [[corrSort[0][0], corrSort[0][1], corrSort[0][2], corrSort[0][3]]]
#topCorrValue[0] is target variable

while(inc < top_k):
    if (inc >= 1):
        if (topCorrValues[inc][0] != corrSort[ctr][0] and topCorrValues[inc-1][0] != corrSort[ctr][0]):
            topCorrValues = np.append(topCorrValues,
                                  [[corrSort[ctr][0], corrSort[ctr][1],
                                    corrSort[ctr][2], corrSort[ctr][3]]], 0)
            inc = inc+1
    else:
        if (topCorrValues[inc][0] != corrSort[ctr][0]):
            topCorrValues = np.append(topCorrValues,
                                  [[corrSort[ctr][0], corrSort[ctr][1],
                                    corrSort[ctr][2], corrSort[ctr][3]]], 0)
            inc = inc+1
    ctr = ctr+1

# graph the top-k variables, graph the correlation values, graph the values of top-k

# graph top-k variables
# Retrieve data for top-k variables

'''print('topCorrValues: ', topCorrValues)
print('')
print('xaxisData: ', axisData)'''
# create array to hold strings and axis titles
tempString = str(axisData[0][2])
xaxisString = [tempString]
ctr = 1
while(ctr <= top_k + 1):
    tempString = str(axisData[ctr][2][:6])
    tempString = tempString + ", lag="
    temp = str(topCorrValues[ctr-1][2])
    tempString = tempString + temp
    xaxisString = np.append(xaxisString, tempString)
    ctr = ctr+1

'''print('xaxisString: ', xaxisString)'''

# ------------- Part 1 -------------
# |                                |
# |   Visualize top-k values with  |
# |   Target Variable (Line Graph) |
# |                                |
# ----------------------------------

color = ['k', 'g', 'y', 'r', 'b', 'p'] # Up to top-k of 5
fig1 = plt.figure()

# graph the target)
plt.plot(targetX, targetY, 'k', c='k', lw=1, label=xaxisString[0])
q3Matrix = [targetY]
# add items to matrix via columns or rows.. iunno
# q3Matrix[0] has first values of target. Dates will be passed via function call.

ctr = 1
while(ctr < len(xaxisString)):
    # Open file, retrieve X-data
    # graph x-data against target data
    filename = axisData[ctr][0]     # Retrieve file name from axisData
    variableX, variableY, var_TitleX, var_TitleY = getData(filename)

    lagTime = int(topCorrValues[ctr-1][2])

    varShuY = shuffleY(targetY, variableY, lagTime)  # Shuffle according to lag#
    # trim shuVarY into the same size as targetY
    itemY = trimData(targetY, varShuY)

    q3Matrix.append(itemY)

    '''df2 = pd.DataFrame({var_TitleY:itemY})
    frames = [df, df2]
    df = pd.concat(frames)
    '''
    plt.plot(targetX, itemY, 'k--', c=color[ctr], lw=1, label=xaxisString[ctr])
    ctr = ctr+1

legend = plt.legend()
frame = legend.get_frame()

plt.title("Figure 1")
# Graph the values of the top-k values against the target variable
plt.xlabel(titleX)
plt.ylabel(titleY)

# ------------- Part 2 -------------
# |                                |
# |    In-Depth graph of Pearson   |
# |     Correlation (Bar Graph)    |
# |                                |
# ----------------------------------

fig2 = plt.figure()
barXTitle = "Correlation Value (abs)"
targetFig2 = "Target Variable = " + str(axisData[0][0])

yBarTemp = [4,3,2,1]

yBarValues = [1.0]      # Put in 1.0 for target variable having 1.0 correlation - with itself
yaxisTitle = [axisData[0][0]]
ctr = 0
while(ctr < len(topCorrValues)):
    temp = topCorrValues[ctr][3]
    yBarValues = np.append(yBarValues, temp)
    ctr = ctr+1

#yBarValues = yBarValues.astype(float)
#print('yBarValues: ', yBarValues)


fig2 = plt.barh(yBarTemp, yBarValues)
# Font size needs help on yticks.
plt.title("Fig.2: Correlation value of Top-K variables")
# Bar graph showing top-3 correlation values, with their value name and lag-#
plt.yticks(yBarTemp, xaxisString, wrap=True, size=8)    # Default is size = 6

ctr=0
while(ctr < len(xaxisString)):
    plt.text(0.1, yBarTemp[ctr], xaxisString[ctr])
    ctr = ctr+1

plt.xlabel(barXTitle)
plt.xlim(0, 1.0)


# ------------- Part 3 -------------
# |                                |
# |  Calculate Cross Correlation   |
# |     Bar Graph of Lag-times     |
# |                                |
# ----------------------------------

fig3 = plt.figure()
# Retrieve top-1 value

top_1 = topCorrValues[0][0][:6]
corrNum = []
lagNum = []
local = -0.3
ctr = 0
while(ctr < len(corrMatrix)):
    comp = corrMatrix[ctr][0][:6]
    if (top_1 == comp):
        corrNum.append(corrMatrix[ctr][3])
        lagNum = np.append(lagNum, int(corrMatrix[ctr][2]))
    ctr = ctr+1

#print('lagNum', lagNum)

xpart3 = "Fig.3: Comparison of the Correlation Values of " + str(axisData[1][2])
plt.title(xpart3)
plt.ylabel("Correlation Value")
plt.xlabel("Lag")
plt.ylim(0, 1.0)

fig3 = plt.bar(lagNum, corrNum, align='center')
ctr = lag
local = -0.2
while (ctr >= 0):
    plt.text(local, 0.1, str(corrNum[ctr][:6]))
    local = local + 1
    ctr = ctr - 1

plt.show()

# ----- Call Q3 using q3Matrix -----

'''
lenM = len(q3Matrix[0])
temp = np.array(q3Matrix[1]).reshape(lenM,1)
stack = np.hstack(temp)
ctr=2
while(ctr < len(q3Matrix)):
    temp = np.array(q3Matrix[ctr]).reshape(lenM, 1)
    #print(temp)
    stack = np.column_stack((stack, q3Matrix[ctr]))
    ctr=ctr+1
'''
lenM = len(q3Matrix[0])
temp = np.array(q3Matrix[1]).reshape(lenM,1)
stack = np.hstack(temp)
ctr=2
while(ctr<len(q3Matrix)):
    temp = np.array(q3Matrix[ctr]).reshape(lenM,1)
    stack = np.column_stack((stack, q3Matrix[ctr]))
    ctr=ctr+1
#print('')
#print(stack)

df = pd.DataFrame(stack)

#calculateTarget(q3Matrix, targetX, titleX, titleY)
calculateTarget(df, targetY, targetX, titleX, titleY, granularity)
