# Question 1
# ----------
# Graphs Time versus Value as initial graph
# Graphs Time versus Delta-Value
# Graphs Time versus z-score of Value

# Need: Hookup with csvInput reader file

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from csvReader import read_file

def getZScore (alist):
    # Returns an array
    zScore = []
    setFlag = 0
    listMean = np.mean(alist)
    listDev = np.std(alist)

    for item in alist:
        zList = (item - listMean)
        if zList < 0:
            setFlag = 1
            zList = zList * -1
        elif zList == 0:
            setFlag = 2
        else:
            setFlag = 0

        if setFlag == 1:
            zList = zList / listDev
            zList = zList * -1
            zScore.append(zList)
        elif setFlag == 2:
            zScore.append(0)
        else:
            zList = zList/listDev
            zScore.append(zList)

    return zScore

    # -infinity < f <= -3.0     = Red
    # -3.0 <= f <= -2.5         = Yellow
    # -2.5 <= f <= 2.5          = Green
    # 2.5 <= f <= 3.0           = Yellow
    # 3.0 <= f < infinity       = Red


# ------------- Part 1 -------------
# |                                |
# | Graph x-values versus y-values |
# |                                |
# ----------------------------------

# Takes in csv file for x-axis and y-axis from csvReader
#xaxisI = ['Time', '2', '4.5', '5', '6.5', '8', '12.5']   # timestamps
#yaxisI = ['Value', '0', '2', '2', '1', '3', '4']   # values

yaxisI, xaxisI = read_file()

# xaxisI = input here
# yaxisI = input here

xTitle = xaxisI.pop(0)
yTitle = yaxisI.pop(0)

# Convert lists to ints
xaxis = list(map(float, xaxisI))
yaxis = list(map(float, yaxisI))

titleString = "Q1: Time versus "
titleString = titleString + yTitle

# Graph Plot
fig1 = plt.figure()
plt.plot(xaxis, yaxis)
plt.title(titleString) # Append variable
plt.xlabel(xTitle)
plt.ylabel(yTitle)



# ------------- Part 2 -------------
# |                                |
# | Graph the change in x-values   |
# | Calculate z-scores for dataset |
# |        Color-Code Range        |
# |                                |
# ----------------------------------

# x_c = x_(t-1)

deltaY = []
counter = 1
while counter < len(yaxis):         # Find x_c = x_t - x_(t-1)
    changeIn = yaxis[counter] - yaxis[counter - 1]
    deltaY.append(changeIn)
    counter = counter + 1

deltaX = []                     # Create a new array for xAxis
for item in xaxis:
    deltaX.append(item)
deltaX.pop()                   # Remove the first item

yAxisTitle = "Change in "      # Create the new y-axis title
yAxisTitle = yAxisTitle + yTitle
titlePrtTwo = "Q1: Time versus "
titlePrtTwo = titlePrtTwo + yAxisTitle

# Reverse-Calculate z-score
# x = z(sigma) + miu,   where x = score, miu = mean, sigma = stddev
meanY = np.mean(yaxis)
stdDevY = np.std(yaxis)

topRangeZ = ((3.0 * meanY) + stdDevY)
highRangeZ = ((2.5 * meanY) + stdDevY)
zeroRangeZ = ((0 * meanY) + stdDevY)
lowRangeZ = ((-2.5 * meanY) + stdDevY)
bottomRangeZ = ((-3.0 * meanY) + stdDevY)

# -------
# Convert lists into numpy-readable
x = np.array(deltaX)
y = np.array(deltaY)


cmap = ListedColormap(['r', 'y', 'lime', 'y', 'r'])
norm = BoundaryNorm([-100.0, bottomRangeZ, lowRangeZ,
                     highRangeZ, topRangeZ, 100.0], cmap.N)
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(y)
lc.set_linewidth(2)

fig2 = plt.figure()

plt.title(titlePrtTwo)
#plt.plot(deltaX, deltaY)
plt.axhline(y=topRangeZ, c='k', linestyle='--')
plt.axhline(y=highRangeZ, c='k', linestyle='--')
plt.axhline(y=zeroRangeZ, c='k', linestyle='--')
plt.axhline(y=lowRangeZ, c='k', linestyle='--')
plt.axhline(y=bottomRangeZ, c='k', linestyle='--')
plt.xlabel(xTitle)
plt.ylabel(yAxisTitle)
plt.gca().add_collection(lc)
plt.xlim(x.min() - 1, x.max() + 1)
plt.ylim(bottomRangeZ - 1, topRangeZ + 1)



# ------------- Part 3 -------------
# |                                |
# | Graph x-values versus z-score  |
# |        Color-Code Range        |
# |                                |
# ----------------------------------
#graph x values z-score
yzaxis = []
yzaxis = getZScore(yaxis)

begTitle = "Q1: Time versus "
midTitle = "z-score of "
midTitle = midTitle + yTitle
begTitle = begTitle + midTitle

# ------ Plot Graph ------
fig3 = plt.figure()

plt.title(begTitle)
plt.plot(xaxis, yzaxis)
plt.axhline(y=3.0, c='k', linestyle='--')
plt.axhline(y=2.5, c='k', linestyle='--')
plt.axhline(y=0, c='k', linestyle='--')
plt.axhline(y=-2.5, c='k', linestyle='--')
plt.axhline(y=-3.0, c='k', linestyle='--')
plt.xlabel(xTitle)
plt.ylabel(midTitle)

# ------ Set Line Colors ------

xzaxis = np.array(xaxis)
yzaxis = np.array(yzaxis)

cmap2 = ListedColormap(['r','y','lime','y','r'])
norm2 = BoundaryNorm([-10.0, -3.0, -2.5, 2.5, 3.0, 10], cmap2.N)

points = np.array([xzaxis, yzaxis]).T.reshape(-1,1,2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

lc2 = LineCollection(segments, cmap=cmap2, norm=norm2)
lc2.set_array(yzaxis)
lc2.set_linewidth(2)

plt.gca().add_collection(lc2)
plt.xlim(xzaxis.min()-1, xzaxis.max()+1)
plt.ylim(-7.0, 7.0)

plt.show()
