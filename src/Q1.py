# Question 1
# ----------
# Graphs Time versus Value as initial graph
# Graphs Time versus Delta-Value
# Graphs Time versus z-score of Value

# To Do:
# Dynamically allocate Fig 3 and Fig 4 y-axis range
# Implement zoom-in function for certain ranges
# Fix Fig 2 - 4 display options for x-axis.


import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.dates as dt
from scipy import stats
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from parseCSV import read_file
from datetime import datetime
from parseCSV import read_file

    # -infinity < f <= -3.0     = Red
    # -3.0 <= f <= -2.5         = Yellow
    # -2.5 <= f <= 2.5          = Green
    # 2.5 <= f <= 3.0           = Yellow
    # 3.0 <= f < infinity       = Red


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

# Convert datetime objects to numbers for ploting
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


titleString = "Q1: Time versus "
titleString = titleString + yTitle

# Graph Plot
fig1 = plt.figure()
fig1 = plt.plot(xaxis, yaxis)
plt.title(titleString) # Append variable
plt.xlabel(xTitle)
plt.ylabel(yTitle)

#fig1_size = plt.rcParams["figure.figsize"] = [8,8]

# ------------- Part 2 -------------
# |                                |
# | Graph the change in x-values   |
# | Calculate z-scores for dataset |
# |        Color-Code Range        |
# |                                |
# ----------------------------------

# x_c = x_(t-1)

negInf = -math.inf
posInf = math.inf
deltaY = []
counter = 1
while counter < len(yaxis):         # Find x_c = x_t - x_(t-1)
    changeIn = yaxis[counter] - yaxis[counter - 1]
    deltaY.append(changeIn)
    counter = counter + 1
deltaX = []                         # Create a new array for xAxis
for item in xaxis:
    deltaX.append(item)
deltaX.pop()
                   # Remove the first item

yAxisTitle = "Change in "       # Create the new y-axis title
yAxisTitle = yAxisTitle + yTitle
titlePrtTwo = "Q1: Time versus "
titlePrtTwo = titlePrtTwo + yAxisTitle

# Reverse-Calculate z-score
# x = miu + z(sigma),   where x = score, miu = mean, sigma = stddev

meanY = np.mean(deltaY)
stdDevY = np.std(deltaY)

topRangeZ = (meanY + (3.0 * stdDevY))
highRangeZ = (meanY + (2.5 * stdDevY))
zeroRangeZ = (meanY + (0 * stdDevY))
lowRangeZ = (meanY + (-2.5 * stdDevY))
bottomRangeZ = (meanY + (-3.0 * stdDevY))

# -------
# Convert lists into numpy-readable
x = np.array(deltaX)
y = np.array(deltaY)


cmap = ListedColormap(['r', 'y', 'g', 'y', 'r'])
norm = BoundaryNorm([negInf, bottomRangeZ, lowRangeZ,
                     highRangeZ, topRangeZ, posInf], cmap.N)
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(y)
lc.set_linewidth(1)

fig2 = plt.figure()

plt.title(titlePrtTwo)
plt.axhline(y=topRangeZ, c='r', linestyle='--')
plt.axhline(y=highRangeZ, c='y', linestyle='--')
plt.axhline(y=zeroRangeZ, c='g', linestyle='--')
plt.axhline(y=lowRangeZ, c='y', linestyle='--')
plt.axhline(y=bottomRangeZ, c='r', linestyle='--')
plt.xlabel(xTitle)
plt.ylabel(yAxisTitle)
plt.gca().add_collection(lc)

plt.xlim(x.min()-1, x.max()+1)
plt.ylim(y.min()+(y.min() * 0.1), y.max()+(y.max() * 0.1))

#fig2_size = plt.rcParams["figure.figsize"] = [8,8]

# ------------- Part 3 -------------
# |                                |
# | Graph x-values versus z-score  |
# |        Color-Code Range        |
# |                                |
# ----------------------------------
#graph x values z-score
yzaxis = []
yzaxis = stats.zscore(yaxis)

begTitle = "Q1: Time versus "
midTitle = "z-score of "
midTitle = midTitle + yTitle
begTitle = begTitle + midTitle

# ------ Set Line Colors ------
fig3 = plt.figure()

xzaxis = np.array(xaxis)
yzaxis = np.array(yzaxis)

cmap2 = ListedColormap(['r', 'y', 'g', 'y', 'r'])
norm2 = BoundaryNorm([negInf, -3.0, -2.5, 2.5, 3.0, posInf], cmap2.N)

points2 = np.array([xzaxis, yzaxis]).T.reshape(-1,1,2)
segments2 = np.concatenate([points2[:-1], points2[1:]], axis=1)

lc2 = LineCollection(segments2, cmap=cmap2, norm=norm2)
lc2.set_array(yzaxis)
lc2.set_linewidth(1)

plt.gca().add_collection(lc2)
plt.xlim(xzaxis.min()-1, xzaxis.max()+1)

yLowLim = 0.0
yMaxLim = 0.0
#if (yzaxis.min() < -3.0):
#    yLowLim = yzaxis.min() + (yzaxis.min() * 1.1)
#elif (-3.0 < yzaxis.min()):
#    yLowLim = -4.5

#if (yzaxis.max() < 3.0):
#    yMaxLim = 4.5
#elif(3.0 < yzaxis.max()):
#    yMaxLim = yzaxis.max() + (yzaxis.max() * 1.1)
#plt.ylim(yLowLim, yMaxLim)
plt.ylim(-10.0, 10.0)

# ------ Plot Graph ------

plt.title(begTitle)
plt.axhline(y=3.0, c='r', linestyle='--')
plt.axhline(y=2.5, c='y', linestyle='--')
plt.axhline(y=0, c='g', linestyle='--')
plt.axhline(y=-2.5, c='y', linestyle='--')
plt.axhline(y=-3.0, c='r', linestyle='--')
plt.xlabel(xTitle)
plt.ylabel(midTitle)

#fig3_size = plt.rcParams["figure.figsize"] = [8,8]


# ------------- Part 4 -------------
# |                                |
# |   Graph delta-x values versus  |
# |            z-score             |
# |        Color-Code Range        |
# |                                |
# ----------------------------------
#graph x values z-score
dyzaxis = []
dyzaxis = stats.zscore(deltaY)

begTitle = "Q1: Time versus "
midTitle = "z-score of "
midTitle = midTitle + yAxisTitle
begTitle = begTitle + midTitle

# ------ Set Line Colors ------
fig4 = plt.figure()

dxzaxis = np.array(deltaX)
dyzaxis = np.array(dyzaxis)

cmap3 = ListedColormap(['r', 'y', 'g', 'y', 'r'])
norm3 = BoundaryNorm([negInf, -3.0, -2.5, 2.5, 3.0, posInf], cmap3.N)

points3 = np.array([dxzaxis, dyzaxis]).T.reshape(-1,1,2)
segments3 = np.concatenate([points3[:-1], points3[1:]], axis=1)

lc3 = LineCollection(segments3, cmap=cmap3, norm=norm3)
lc3.set_array(dyzaxis)
lc3.set_linewidth(1)

plt.gca().add_collection(lc3)
plt.xlim(dxzaxis.min()-1, dxzaxis.max()+1)

yLowLim2 = 0.0
yMaxLim2 = 0.0
#if (yzaxis.min() < -3.0):
#    yLowLim2 = yzaxis.min() + (yzaxis.min() * 1.1)
#elif (-3.0 < yzaxis.min()):
#    yLowLim2 = -4.5

#if (yzaxis.max() < 3.0):
#    yMaxLim2 = 4.5
#elif(3.0 < yzaxis.max()):
#    yMaxLim2 = yzaxis.max() + (yzaxis.max() * 1.1)
#plt.ylim(yLowLim2, yMaxLim2)
plt.ylim(-10.0, 10.0)

# ------ Plot Graph ------

plt.title(begTitle)
plt.axhline(y=3.0, c='r', linestyle='--')
plt.axhline(y=2.5, c='y', linestyle='--')
plt.axhline(y=0, c='g', linestyle='--')
plt.axhline(y=-2.5, c='y', linestyle='--')
plt.axhline(y=-3.0, c='r', linestyle='--')
plt.xlabel(xTitle)
plt.ylabel(yAxisTitle)

#-------

plt.show()
