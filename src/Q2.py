# Question 2
# ----------
# Calculates lag times for 3 different files and
# Compares that to the target file
# Currently files are located locally and will need to be
# Integrated with the DataBase

# Best example: RU/DJIA/SP/WILL

#SP djia ru will

import numpy as np
import matplotlib.dates as dates
import matplotlib.pyplot as plt
from parseCSV import read_file, initial_file
from datetime import datetime as dt

def shuffle(ylist, lag, maxLag):
    # Shuffles list over by n = lag, returns shuffled list
    ylist = np.roll(ylist, lag)

    # Remove first three items from rolled list
    n = 0
    while (n < maxLag):
        ylist = np.delete(ylist, 0)
        n = n+1

    return ylist

def parse (xlist, ylist):

    ti_x = xlist.pop(0)     # Title of X
    ti_y = ylist.pop(0)     # Title of Y

    x_dates = []
    for thing in xlist:
        x_dates.append(dt.strptime(thing, '%Y-%m-%d'))

    x = []
    for thing in x_dates:
        x.append(dates.date2num(thing))

    y = list(map(float, ylist))

    return x, y, ti_x, ti_y


def correlation(xlist, ylist):
    xbar = np.mean(xlist)
    ybar = np.mean(ylist)
    xstd = np.std(xlist)
    ystd = np.std(ylist)
    num = 0.0

    for i in range(len(xlist)):
        num = num + (xlist[i] - xbar) * (ylist[i] - ybar)

    corr = num / ((len(xlist) - 1) * xstd * ystd)
    return corr


# ------------- Part i -------------
# |                                |
# |  Convert csv file to readable  |
# |  format for x-axis and y-axis  |
# |                                |
# ----------------------------------

""" 
Files passed through as of 11-11-17 have the same start time and end time.
"""

# Takes in csv file for x-axis and y-axis from csvReader

# Initial Target Variable
target_y, target_x = initial_file()
target_x, target_y, targetTitle_x, targetTitle_y = parse(target_x, target_y)

corrMatrix = [0, targetTitle_y, 1]      # [Lag#, yTitle, Correlation]

# Delete x amounts off the end of the target list for number of lag calculations
lag = 6         # Lag is Number_of_Lags - 1
n = 0
while(n < lag):
    # Delete from the end of the array
    # target_y = np.delete(target_y, 0)
    # Also delete first 3 values from x-list
    target_x.pop(0)
    target_y.pop(0)
    n = n + 1

target = np.array(target_y)       # Raw list without lag# or title in it; Used to calculate correlation

target_y.insert(0, targetTitle_y)
target_y.insert(0, 0)       # [Lag#, yTitle, Values....]
targetMatrix = target_y

# ------------- Part i -------------
# |                                |
# |      Call NarrowData.csv       |
# |     Retrieve 10 csv files      |
# |                                |
# ----------------------------------

# Currently parses csv files according to the time frame of target
"""target_timestamp = target_x[0]
len_targetx = len(target_x)
len_targety = len(target_y)
print("Target Timestamp: ", target_timestamp)
"""

# Operates under the assumption of 5 csvs currently
csv_num = 0
# appendTarget = y
# appendCorr = [0, ti_y, 0]
# csv_num = how many csv files are being read
# Currently only have 4 csvs in database, so the number of analysis is only 3
while (csv_num < 3):
    print('')
    v_y, v_x = read_file()

    xlist, ylist, title_x, title_y = parse(v_x, v_y)

    appendList = []
    n = 0
    while (n < lag):
        # shuffle parses and shifts array over by the lag
        appendList = shuffle(v_y, n, lag)
        # Add shuffled list to placeholder list
        append = list(map(float, appendList))


        # Calculate Correlation
        corrValue = correlation(target, append)
        appendCorr = [n, title_y, corrValue]        # Has the full length of string

        title_yTrim = title_y[:6]       # Cuts off string at certain length for easier comparison
        appendList = np.insert(appendList, 0, title_yTrim)
        appendList = np.insert(appendList, 0, n)
        # Append placeholder list to targetMatrix
        targetMatrix = np.row_stack((targetMatrix, appendList))
        # Append correlation, lag, and title to corrMatrix
        corrMatrix = np.row_stack((corrMatrix, appendCorr))

        n = n+1

    csv_num = csv_num + 1

"""
print('')
print('Target Matrix:', targetMatrix)
print('')
print('Correlation Matrix:', corrMatrix)
print('')
"""

# ------------- Part ii -------------
# |                                |
# |  Find top-k values k = 3   |
# |                                |
# ----------------------------------

# Sort corrMatrix from ascending order
# Currently does not work with negative numbers;
# may have to set a column in CorrMatrix indicating Negative and Positive Flags


corrSort = sorted(corrMatrix, key=lambda x: x[2], reverse=True)

"""
print('')
print("CorrSort: ", corrSort)
print('')
"""

# Retrieve the top 3 correlations
top1CorrValue = corrSort[1]         # corrSort[0] being the target variable
top2CorrValue = corrSort[2]
top3CorrValue = corrSort[3]

# Retrieved from targetMatrix; will contain the values of the array
value1 = []
value2 = []
value3 = []

i = 0
while(i < len(corrSort)):
    # Values in targetMatrix get cut off after index[0] for string names
    # [:7] works for NASDAQ, [:6] for WILL
    trun1 = top1CorrValue[1][:6]
    trun2 = top2CorrValue[1][:6]
    trun3 = top3CorrValue[1][:6]

    """
    print(top1CorrValue[0], targetMatrix[i][0], trun1, targetMatrix[i][1])
    """

    if(top1CorrValue[0] == targetMatrix[i][0] and trun1 == targetMatrix[i][1]):
        value1 = targetMatrix[i]
        value1[1] = top1CorrValue[1]
    elif(top2CorrValue[0] == targetMatrix[i][0] and trun2 == targetMatrix[i][1]):
        value2 = targetMatrix[i]
        value2[1] = top2CorrValue[1]
    elif(top3CorrValue[0] == targetMatrix[i][0] and trun3 == targetMatrix[i][1]):
        value3 = targetMatrix[i]
        value3[1] = top3CorrValue[1]
    i = i+1

"""
print('Top Correlation Values: ', top1CorrValue, top2CorrValue, top3CorrValue)
print('Values: ', value1, value2, value3)
"""

# ------------- Part 1 -------------
# |                                |
# |   Visualize top-k values with  |
# |   Target Variable (Line Graph) |
# |                                |
# ----------------------------------

# create the strings for each top-k value
value1Title = str(top1CorrValue[1]) + ', Lag=' + str(value1[0])
value1 = np.delete(value1, 0)
value1 = np.delete(value1, 0)

value2Title = str(top2CorrValue[1]) + ', Lag=' + str(value2[0])
value2 = np.delete(value2, 0)
value2 = np.delete(value2, 0)

value3Title = str(top3CorrValue[1]) + ', Lag=' + str(value3[0])
value3 = np.delete(value3, 0)
value3 = np.delete(value3, 0)


targetTitle = 'Target Variable: ' + str(target_y[1])
fig1Title = 'Fig.1: ' + targetTitle
"""
fig, ax1 = plt.subplots()
ax1.plot(target_x, target, 'k', label=targetTitle)
ax1.plot(target_x, value1, 'k--', label=value1Title)
ax1.plot(target_x, value2, 'k:', label=value2Title)
ax1.plot(target_x, value3, 'k-.', label=value3Title)

legend = ax1.legend()
frame = legend.get_frame()

ax1.set_xlabel(targetTitle_x)
ax1.set_title("Line graph of Top-K values versus Target variable", size=8)
ax1.set_ylabel("Value")

"""

fig1 = plt.figure()
fig1 = plt.plot(target_x, target, 'k', lw=1, label=targetTitle)
fig1 = plt.plot(target_x, value1, 'k--', c='g', lw=1, label=value1Title)
fig1 = plt.plot(target_x, value2, 'k--', c='y', lw=1, label=value2Title)
fig1 = plt.plot(target_x, value3, 'k--', c='r', lw=1, label=value3Title)

legend = plt.legend()
frame = legend.get_frame()

#plt.title(fig1Title)
plt.title("Figure 1")
plt.xlabel("Time")
plt.ylabel("Value")

# ------------- Part 2 -------------
# |                                |
# |    In-Depth graph of Pearson   |
# |     Correlation (Bar Graph)    |
# |                                |
# ----------------------------------
"""
fig, ax2 = plt.subplots()
barXTitle = "Correlation Value (abs)"
yBarData = [targetTitle, value1Title, value2Title, value3Title]

yBarTemp = [0, 1, 2, 3]
yBarValues = [float(corrMatrix[0][2]), float(corrMatrix[1][2]),
              float(corrMatrix[2][2]), float(corrMatrix[3][2])]
yBarValues = np.array(yBarValues)

ax2.barh(yBarTemp, yBarValues)
# Font size needs help on yticks.
ax2.set_title("Correlation value of Top-K variables")
ax2.set_yticks(yBarTemp, yBarData)
ax2.set_xlabel(barXTitle)
ax2.set_xlim(0, 1.0)
"""

fig2 = plt.figure()
barXTitle = "Correlation Value (abs)"
targetFig2 = "Target Variable = " + str(target_y[1])
yBarData = [targetTitle, value1Title, value2Title, value3Title]

yBarTemp = [4,3,2,1]
yBarValues = [float(corrMatrix[0][2]), float(corrMatrix[1][2]),
              float(corrMatrix[2][2]), float(corrMatrix[3][2])]
yBarValues = np.array(yBarValues)

fig2 = plt.barh(yBarTemp, yBarValues)
# Font size needs help on yticks.
plt.title("Fig.2: Correlation value of Top-K variables")
plt.yticks(yBarTemp, yBarData, wrap=True, size=6)

n = 4
i = 0
while (n > 0):
    plt.text(0.1, n, str(corrMatrix[i][2])[:6])
    n = n-1
    i = i+1

plt.xlabel(barXTitle)
plt.xlim(0, 1.0)

# ------------- Part 3 -------------
# |                                |
# |  Calculate Cross Correlation   |
# |     Bar Graph of Lag-times     |
# |                                |
# ----------------------------------

# Graphs target variable correlation and highest variable
"""
fig, ax3 = plt.subplots()
ax3.set_title("Bar Graph Fix Later")
ax3.set_xlabel("Correlation Value")
ax3.set_ylabel("Lag")

matchy = top1CorrValue[1][:6]
n = 0
lagNum = []
while (n < lag):
    lagNum.append(n)
    n = n+1

corrNum = []
n = 0
while(n < len(corrMatrix)):
    comp = corrMatrix[n][1][:6]
    if (matchy == corrMatrix[n][1]):
        corrNum.append(corrMatrix[n][2])
    n = n + 1

print(corrNum)

#ax3.bar(x=lagNum, height=0.5, bottom=corrNum, align='center')
"""
fig3 = plt.figure()

matchy = top1CorrValue[1][:6]
n = 0
lagNum = []
while (n < lag):
    lagNum.append(n)
    n = n+1

corrNum = []
n = 0
while(n < len(corrMatrix)):
    comp = corrMatrix[n][1][:6]
    if (matchy == comp):
        corrNum.append(corrMatrix[n][2])
    n = n + 1

"""
print(corrNum)
"""

#ax3.bar(x=lagNum, height=0.5, bottom=corrNum, align='center')

xpart3 = "Fig.3: Comparison of the Correlation Values of " + str(top1CorrValue[1])
plt.title(xpart3)
plt.ylabel("Correlation Value")
plt.xlabel("Lag")
plt.ylim(0, 1.0)

fig3 = plt.bar(lagNum, corrNum, align='center')
n = 0
local = -0.3
while (n < lag):
    plt.text(local, 0.1, str(corrNum[n][:6]))
    local = local + 1
    n = n + 1


plt.show()
