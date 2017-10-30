# Question 2
# ----------
#
#

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


# ------------- Part i -------------
# |                                |
# |      Call NarrowData.csv       |
# |     Retrieve 10 csv files      |
# |                                |
# ----------------------------------



# ------------- Part 1 -------------
# |                                |
# |  Calculate Pearson Correlation |
# |    Visualize it (Line Graph)   |
# |                                |
# ----------------------------------



# ------------- Part 2 -------------
# |                                |
# |    In-Depth graph of Pearson   |
# |     Correlation (Bar Graph)    |
# |                                |
# ----------------------------------




# ------------- Part 3 -------------
# |                                |
# |  Calculate Cross Correlation   |
# |     Bar Graph of Lag-times     |
# |                                |
# ----------------------------------