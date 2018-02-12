# NarrowData.py
# --------
# Using Target Variable from Input.py and Search Tags,
# Go through Database and retrieve 10 or less csv files

# Currently NarrowData.py to do:
#       Pulls the file from Upload.py, since the Data Consumer goes through Upload.py first.
#       1.) If data occurs before target timestamp, add to list
#               a.) Must be at least lag# timestamps behind.
#       2.) If data matches tags targeted, add to list

# Update: 1/11/18

from datetime import datetime, timedelta

def getID(target, tags, lag):
    import sqlite3
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    number = getTargetID(target)
    beg = getTargetFirst(number)
    end = getTargetLast(number)
    
    beg = datetime.strptime(beg, '%Y-%m-%d %H:%M:%S')
    beg = beg - timedelta(days=lag)

    # Query: Select all IDnumbers that occur before targetFirstStamp and after targetLastStamp.
    c.execute('''SELECT IDnum FROM granularity ''' 
            ''' WHERE first < ? AND last >= ?''',
              (beg, end))

    rows = c.fetchall()

    idList = []
    for item in rows:
        potato = item[0]
        idList.append(potato)

    temp = 0
    nameList = []
    while (temp < len(idList)):
        IDinLoop = idList[temp]
        c.execute('''SELECT name FROM description '''
                ''' WHERE IDnum = ?''', (IDinLoop,))
        rows = c.fetchall()
        nameTemp = rows[0][0]
        nameList.append(nameTemp)
        temp = temp+1

    # Select IdNUM from tags where
        # targetFirstStamp > targetFirstStamp of DB && targetLastStamp > targetLastStamp of DB + 5

    # select from IdNUM from tags where
        # tag 1 of taglist = tag1 of db or tag2 of db or tag3 of db or tag4 of db
        # else remove
    #c.execute('''''')

    #conn.commit()
    conn.close()
    return nameList

def getTargetID(fileName):
    import sqlite3
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    c.execute('''SELECT IDnum FROM description '''
            ''' WHERE name = ?''', (fileName,))

    rows = c.fetchall()
    fileID = rows[0][0]

    conn.close()
    return fileID

def getTargetFirst(ID):
    import sqlite3
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    c.execute('''SELECT first from granularity WHERE IDnum = ?''', (ID,))

    rows = c.fetchall()
    fileFirst = rows[0][0]

    conn.close()
    return fileFirst

def getTargetLast(ID):
    import sqlite3
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    c.execute('''SELECT last from granularity WHERE IDnum = ?''', (ID,))

    rows = c.fetchall()
    fileLast = rows[0][0]

    conn.close()
    return fileLast


#Prompt to upload file, or pick target variable

# target = 't4.csv'
targetTagList = ['a', 'b', 'c', 'd']

''' tempID = getTargetID(target)
tempFirst = getTargetFirst(tempID)
tempLast = getTargetLast(tempID)

fileList = getID(target, targetTagList)
# List of files that fall within the start/end timestamps
'''
