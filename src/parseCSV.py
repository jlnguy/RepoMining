import csv

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

            if time == "." or data == ".":  # where there's a date with no data put ' . '
                continue

            elif time == " " or data == " ":  # testing for blanks
                continue

            else:  # only add them in here
                dates.append(time)
                info.append(data)

    return (info, dates)