# Question 2
# ----------
# Takes results from NarrowData, shuffles it, and then visualizes it
# Figure 1: Displays data of top-k variables against target variable with lag times
# Figure 2: Displays correlation of top-k variables against target variable correlation
# Figure 3: Displays top-1 correlation values for each lag time

from NarrowData import getID, getTargetID, getTargetFirst
from ParseData import shuffleDate, shuffleY, trimData
from ParseComma import getData, convertData
import matplotlib.pyplot as plt
import numpy as np


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


# set file as another one later.
targetFile = 't4.csv'
tags = [0]
targetX, targetY, titleX, titleY = getData(targetFile)
targetXconv = convertData(targetX)
targetID = getTargetID(targetFile)
targetStart = getTargetFirst(targetID)

#print('fileID:', targetFile, "ID number: ", targetID)
#print('start: ', targetStart)

listOfNarrowDataIDs = getID(targetFile, tags)
if(len(listOfNarrowDataIDs) == 0):
    print('No values found with NarrowData (granularity)')

# Lists to store arbitrary information about csvs
# list = [filename, xaxis, yaxis]
axisData = [[targetFile, titleX, titleY]]

# Arbitrarily set lag as 5
lag = 5

# [target, id#, lag, correlation]
# Pad the multidimensional matrix with 0's
corrMatrix = [[0,0,0,0]]

ctr = lag
for item in listOfNarrowDataIDs:
    numberID = getTargetID(item)
    itemX, itemY, item_TitleX, item_TitleY = getData(item)
    trun = item_TitleY[:6]
    axisData = np.append(axisData, [[item, item_TitleX, item_TitleY]], 0)
    while(ctr >= 0):
        shuffledX = shuffleDate(itemX, targetStart, ctr)
        shuffledX = convertData(shuffledX)
        corr = correlation(shuffledX, targetXconv)

        corrMatrix = np.append(corrMatrix, [[item, numberID, ctr, corr]], 0)
        ctr = ctr-1
    ctr = lag

corrMatrix = np.delete(corrMatrix, 0, 0) # Remove the padded row [0,0,0,0]

# find the top-k variables

corrSort = sorted(corrMatrix, key=lambda x: x[3], reverse=True)


# Arbitrarily set top-k number to 3;
top_k = 3   # Pretend this is user specifying they want top-k of 3
top_k = top_k - 1   # fix up top_k variable to be index 0 instead of 1; done.
ctr = 0
inc = 0
# topCorrValues = length of top_k, [target, id#, lag, correlation]
topCorrValues = [[corrSort[0][0], corrSort[0][1], corrSort[0][2], corrSort[0][3]]]
print('')

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

# create array to hold strings and axis titles
tempString = str(axisData[0][2])
xaxisString = [tempString]
ctr = 1
while(ctr < len(axisData)):
    tempString = str(axisData[ctr][2][:6])
    tempString = tempString + ", lag="
    temp = str(topCorrValues[ctr-1][2])
    tempString = tempString + temp
    xaxisString = np.append(xaxisString, tempString)
    ctr = ctr+1

# --------------------
# Graph values(?)
color = ['k', 'g', 'y', 'r', 'b', 'p'] # Up to top-k of 5
fig1 = plt.figure()

# graph the target)
plt.plot(targetX, targetY, 'k', c='k', lw=1, label=xaxisString[0])
fig2Matrix = [[targetY]]

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

    fig2Matrix = np.append(fig2Matrix, [[itemY]], 0)
    plt.plot(targetX, itemY, 'k--', c=color[ctr], lw=1, label=xaxisString[ctr])
    ctr = ctr+1

legend = plt.legend()
frame = legend.get_frame()

plt.title("Figure 1")
# Graph the values of the top-k values against the target variable
plt.xlabel(titleX)
plt.ylabel(titleY)


# --------------
# part 2: pearson correlation/bar graph
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

# Figure 3: corr value zoom in thing

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


xpart3 = "Fig.3: Comparison of the Correlation Values of " + str(axisData[1][2])
plt.title(xpart3)
plt.ylabel("Correlation Value")
plt.xlabel("Lag")
plt.ylim(0, 1.0)

fig3 = plt.bar(lagNum, corrNum, align='center')
ctr = lag
local = -0.3
while (ctr >= 0):
    plt.text(local, 0.1, str(corrNum[ctr][:6]))
    local = local + 1
    ctr = ctr - 1

plt.show()