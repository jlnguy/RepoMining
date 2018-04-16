import csv
from NarrowData import getTargetID, getGranularityType

def initial_file():
    print("Enter file for target variable:")
    # userIn = input() + ".csv"
    with open(input()) as csvFile:
        readCSV = csv.reader(csvFile, delimiter=",")  # csv = comma separated
        # with open(userIn) as csvFile:
        #    readCSV = csv.reader(csvFile, delimiter=",")
        dates = []
        info = []

        for row in readCSV:
            time = row[0]
            data = row[1]

            if time == "." or data == ".":  # where there's a date with no data put ' . '
                continue

            elif time == " " or data == " ":  # testing for blanks
                continue

            else:  # only add them in here
                dates.append(time)
                info.append(data)

    return (info, dates)

def read_file():

    #userIn = input("Enter input file: ")
    print("Enter input file:")
    #userIn = input() + ".csv"
    with open(input()) as csvFile:
        readCSV = csv.reader(csvFile, delimiter=",")  # csv = comma separated
    #with open(userIn) as csvFile:
    #    readCSV = csv.reader(csvFile, delimiter=",")
        dates = []
        info = []

        for row in readCSV:
            time = row[0]
            data = row[1]

            if time == "." or data == ".":  # where there's a date with no data put ' . '
                continue

            elif time == " " or data == " ":  # testing for blanks
                continue

            else:  # only add them in here
                dates.append(time)
                info.append(data)

    return (info, dates)

# Upload Code
def inputFile(filename):
    with open(filename, "r") as csvFile:
        readCSV = csv.reader(csvFile, delimiter=",")
        dates = []
        info = []

        for row in readCSV:
            time = row[0]
            data = row[1]

            if time == "." or data == ".###":  # where there's a date with no data put ' . '
                continue

            elif time == " " or data == " ":  # testing for blanks
                continue

            else:  # only add them in here
                dates.append(time)
                info.append(data)

    return (info, dates)

from datetime import datetime
import matplotlib.dates as dt

def getData(filename):
    yaxisI, xaxisI = read_file(filename)

    xTitle = xaxisI.pop(0)
    yTitle = yaxisI.pop(0)

    xaxis_datetime = []
    identity = getTargetID(filename)
    granu = getGranularityType(identity)
    if (granu == 'Daily'):
        for x in xaxisI:
            xaxis_datetime.append(datetime.strptime(x, '%Y-%m-%d'))
        # Add an option to determine which x-data is getting put in; currently the only input that this accepts is month/day/time.
        # Future additions: Be able to parse month-day-year; year-month-day; year/month/day; hour:minute:second
        # (x, '%m-%d-%Y); (x, %Y-%m-%d); (x, %Y/%m/%d); (x, hourminutesecondhere)
    elif(granu == 'Monthly'):
        for x in xaxisI:
            xaxis_datetime.append(datetime.strptime(x, '%Y-%m'))
    elif(granu == 'Yearly'):
        for x in xaxisI:
            xaxis_datetime.append(datetime.strptime(x, '%Y'))

    # Convert datetime objects to numbers for plotting
    xaxis = []
    for y in xaxis_datetime:
        xaxis.append(dt.date2num(y))

    # Convert list to ints
    yaxis = list(map(float, yaxisI))
    return xaxis, yaxis, xTitle, yTitle
