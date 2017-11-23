"""

To-Do: Have different catch cases for csv files.

"""

# Question 1
# ----------
# Graphs Time versus Value as initial graph
# Graphs Time versus z-score of Value
# Graphs Time versus Delta-Value; Displays as bar graph
# Graphs Time versus z-score of Delta-Value; Displays as bar graph


import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.dates as dt
from scipy import stats
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from datetime import datetime
from parseCSV import read_file

# ----- Global Variables -----

negInf = -math.inf
posInf = math.inf

# ----- -----

# ------------- Part i -------------
# |                                |
# |  Convert csv file to readable  |
# |  format for x-axis and y-axis  |
# |                                |
# ----------------------------------

# Takes in csv file for x-axis and y-axis from csvReader

yaxisI, xaxisI = read_file()

xTitle = xaxisI.pop(0)
yTitle = yaxisI.pop(0)

xaxis_datetime = []
for x in xaxisI:
    xaxis_datetime.append(datetime.strptime(x, '%Y-%m-%d'))
    # Add an option to determine which x-data is getting put in; currently the only input that this accepts is month/day/time.
    # Future additions: Be able to parse month-day-year; year-month-day; year/month/day; hour:minute:second
    # (x, '%m-%d-%Y); (x, %Y-%m-%d); (x, %Y/%m/%d); (x, hourminutesecondhere)

# Convert datetime objects to numbers for plotting
xaxis = []
for y in xaxis_datetime:
    xaxis.append(dt.date2num(y))

# Convert list to ints
yaxis = list(map(float, yaxisI))



# ------------- Part 1 -------------
# |                                |
# | Graph x-values versus y-values |
# |                                |
# ----------------------------------


titleString = "Q1 Figure 1: Time versus Values in "
titleString = titleString + yTitle

# Graph Plot
fig1 = plt.figure()
fig1 = plt.plot(xaxis, yaxis, linewidth=1.0)
plt.title(titleString) # Append variable
plt.xlabel(xTitle)
plt.ylabel(yTitle)



# ------------- Part 2 -------------
# |                                |
# | Graph x-values versus z-score  |
# |        Color-Code Range        |
# |                                |
# ----------------------------------

yzaxis = []
yzaxis = stats.zscore(yaxis)

xzaxis = np.array(xaxis)
yzaxis = np.array(yzaxis)

# ----- Create graph title -----
titleFig2 = "Q1 Figure 2: Time versus the "
midTitle = "z-score of "
midTitle = midTitle + yTitle
titleFig2 = titleFig2 + midTitle

# ----- Set Line Colors -----

fig2 = plt.figure()

cmap = ListedColormap(['r','y','g','y','r'])
norm = BoundaryNorm([negInf,-3.0,-2.5,2.5,3.0, posInf], cmap.N)

points = np.array([xzaxis, yzaxis]).T.reshape(-1,1,2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(yzaxis)
lc.set_linewidth(1)

plt.gca().add_collection(lc)
plt.xlim(xzaxis.min()-5, xzaxis.max()+5)

# Dynamic Allocation of y-limits
yLowLim = 0.0
yHighLim = 0.0

if(yzaxis.max() < 3.0):
    yHighLim = 3.5
elif(3.0 < yzaxis.max()):
    yHighLim = yzaxis.max() + (yzaxis.max() * 0.1)

if(yzaxis.min() < -3.0):
    yLowLim = yzaxis.min() + (yzaxis.min() * 0.1)
elif(-3.0 < yzaxis.min()):
    yLowLim = -3.5

plt.ylim(yLowLim, yHighLim)

# ----- Plot Graph Labels / Lines -----

plt.title(titleFig2)
plt.axhline(y=3.0,  c='r',  linestyle='--')
plt.axhline(y=2.5,  c='y',  linestyle='--')
plt.axhline(y=0,    c='g',  linestyle='--')
plt.axhline(y=-2.5, c='y',  linestyle='--')
plt.axhline(y=-3.0, c='r',  linestyle='--')
plt.xlabel(xTitle)
plt.ylabel(midTitle)



# ------------- Part 3 -------------
# |                                |
# |  Graph the change in x-values  |
# | Calculate z-scores for dataset |
# |      Color-Code Range (?)      |
# |           Bar Graph            |
# |                                |
# ----------------------------------

deltaY = []
counter = 1
while counter < len(yaxis):         # Find x_c = x_t - x_(t-1)
    changeIn = yaxis[counter] - yaxis[counter - 1]
    deltaY.append(changeIn)
    counter = counter + 1
deltaX = []                         # Create a new array for xAxis
for item in xaxis:
    deltaX.append(item)
deltaX.pop()        # Remove the first item

midTitle_3 = "Change in "       # Create the new y-axis title
midTitle_3 = midTitle_3 + yTitle
title_3 = "Q1 Figure 3: Time versus the "
title_3 = title_3 + midTitle_3


# Reverse-Calculate z-score
# x = miu + z(sigma),   where x = score, miu = mean, sigma = stddev

meanY = np.mean(deltaY)
stdDevY = np.std(deltaY)

topRangeZ = (meanY + (3.0 * stdDevY))
highRangeZ = (meanY + (2.5 * stdDevY))
zeroRangeZ = (meanY + (0 * stdDevY))
lowRangeZ = (meanY + (-2.5 * stdDevY))
bottomRangeZ = (meanY + (-3.0 * stdDevY))

# ----- Worky Calc Thing -----
deltaX = np.array(deltaX)
deltaY = np.array(deltaY)

num = len(deltaX)
fig3 = plt.figure()
fig3 = plt.bar(deltaX, deltaY, 1.0, color='b')

# ----- Plot Graph Labels -----
"""
plt.axhline(y=topRangeZ,    c='r', linestyle='--')
plt.axhline(y=highRangeZ,   c='y', linestyle='--')
plt.axhline(y=zeroRangeZ,   c='g', linestyle='--')
plt.axhline(y=lowRangeZ,    c='y', linestyle='--')
plt.axhline(y=bottomRangeZ, c='r', linestyle='--')
"""

plt.title(title_3)
plt.xlabel(xTitle)
plt.ylabel(midTitle_3)

plt.xlim(deltaX.min()-5, deltaX.max()+5)



# ------------- Part 4 -------------
# |                                |
# |   Graph delta-x values versus  |
# |            z-score             |
# |           Bar Graph            |
# |       Color-Code Range(?)      |
# |                                |
# ----------------------------------

#deltaY_zscore = []
deltaY_zscore = stats.zscore(deltaY)
deltaY_zscore = np.array(deltaY_zscore)
deltaX_zscore = np.array(deltaX)

# ----- Create Title -----
midTitle_4 = "z-score of the "
titleFig4 = "Q1 Figure 4: Time versus the "
titleFig4 = titleFig4 + midTitle_4 + midTitle_3

# ----- Create 4 additonal lists, for yellow and red ranges -----
testList = []
yellowCx = np.array(testList)
yellowCy = np.array(testList)
redCx = np.array(testList)
redCy = np.array(testList)
length = len(deltaY_zscore)
i = 0
while (i < length):
    if(deltaY_zscore[i] >= 2.5):
        if(deltaY_zscore[i] < 3.0):
            yellowCy = np.append(yellowCy, deltaY_zscore[i])
            yellowCx = np.append(yellowCx, deltaX_zscore[i])
        else:
            redCy = np.append(redCy, deltaY_zscore[i])
            redCx = np.append(redCx, deltaX_zscore[i])

    elif (deltaY_zscore[i] <= -2.5):
        if(deltaY_zscore[i] > -3.0):
            yellowCy = np.append(yellowCy, deltaY_zscore[i])
            yellowCx = np.append(yellowCx, deltaX_zscore[i])
        else:
            redCy = np.append(redCy, deltaY_zscore[i])
            redCx = np.append(redCx, deltaX_zscore[i])

    i = i+1

# ------ Plot Graph Labels -----

fig4 = plt.figure()
fig4 = plt.bar(deltaX_zscore, deltaY_zscore, 1.0, color='g')
fig4 = plt.bar(yellowCx, yellowCy, 1.0, color='y')
fig4 = plt.bar(redCx, redCy, 1.0, color='r')


plt.title(titleFig4)
plt.xlabel(xTitle)
plt.ylabel(midTitle_3)

plt.axhline(y=3.0,  c='r', linestyle='--')
plt.axhline(y=2.5,  c='y', linestyle='--')
plt.axhline(y=0,    c='g', linestyle='--')
plt.axhline(y=-2.5, c='y', linestyle='--')
plt.axhline(y=-3.0, c='r', linestyle='--')

# Dynamic Allocation of y-limits
yLowLim = 0.0
yHighLim = 0.0

if(deltaY_zscore.max() < 3.0):
    yHighLim = 3.5
elif(3.0 < deltaY_zscore.max()):
    yHighLim = deltaY_zscore.max() + (deltaY_zscore.max() * 0.1)

if(deltaY_zscore.min() < -3.0):
    yLowLim = deltaY_zscore.min() + (deltaY_zscore.min() * 0.1)
elif(-3.0 < deltaY_zscore.min()):
    yLowLim = -3.5

plt.ylim(yLowLim, yHighLim)
plt.xlim(deltaX_zscore.min()-5, deltaX_zscore.max()+5)



# -------- Display Graphs --------

plt.show()
