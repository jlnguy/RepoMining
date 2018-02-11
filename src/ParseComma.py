import csv
from datetime import datetime
import matplotlib.dates as dt

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

def read_file(filename):
    with open(filename) as csvFile:
        readCSV = csv.reader(csvFile, delimiter=",")  # csv = comma separated
        dates = []
        info = []

        for row in readCSV:
            time = row[0]
            data = row[1]

            if time == "." or data == ".":
                # where there's a date with no data put ' . '
                continue

            elif time == " " or data == " ":
                # testing for blanks
                continue

            else:  # only add them in here
                dates.append(time)
                info.append(data)

    return (info, dates)

def getData(filename):
    yaxisI, xaxisI = read_file(filename)

    xTitle = xaxisI.pop(0)
    yTitle = yaxisI.pop(0)

    xaxis_datetime = []
    for x in xaxisI:
        xaxis_datetime.append(datetime.strptime(x, '%Y-%m-%d'))

    '''
    print('getData', xaxis_datetime[1])

    # Convert datetime objects to numbers for plotting
    xaxis = []
    for y in xaxis_datetime:
        xaxis.append(dt.date2num(y))
    '''
    # Convert list to ints
    yaxis = list(map(float, yaxisI))

    return xaxis_datetime, yaxis, xTitle, yTitle

def convertData(xaxis):
# Convert datetime arrays to np arrays to graph
    x = []
    for item in xaxis:
        x.append(dt.date2num(item))

    return x