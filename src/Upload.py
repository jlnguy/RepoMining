# Asks for the file that the user is uploading
# Tags the file with appropiate tags, adds them to the database
# parses CSV for Q1, Q2, Q3.

from parseCSV import inputFile
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

def getFirstStamp():
    return firstStamp

def getLastStamp():
    return lastStamp

def getTaggedList():
    return tagList

filename = input("Enter file to upload: ")
print("You uploaded: ", filename)
print('')
descp = input("Enter a description to describe the file: ")
print('')
# Program will retrieve the granularity of the file
typeGranularity = input("Granularity of the file (Monthly/Daily/Yearly): ")

# user will be determined by code. Set to admin
username = 'admin'
settype = 'public'

print('')
print("Tag your file so that others can find and use it.")
tag_1 = input("Tag 1: ")
tag_2 = input("Tag 2: ")
tag_3 = input("Tag 3: ")
tag_4 = input("Tag 4: ")

tagList = [tag_1, tag_2, tag_3, tag_4]

# Add items to database
# id# = id# of any section + 1.
col2 = ''
table = ''

c.execute('''SELECT idNUM FROM description 
                    WHERE idNUM = (SELECT max(idNUM) FROM description);'''.\
                     format(idNUM=col2, description=table))
all_rows = c.fetchall()
identity = all_rows[0][0]

identity = identity+1


c.execute('''INSERT INTO description(name, info, idNUM)
              VALUES(?,?,?)''', (filename, descp, identity))

# Timestamps
# Timestamps are not parsed (Still has DATE x x x x format)
y, x = inputFile(filename)
firstStamp = x[1]
lastStamp = x[len(x) - 1]
c.execute('''INSERT INTO granularity(start, end, type, itemNum, IDnum)
              VALUES(?,?,?,?,?)''', (firstStamp, lastStamp, typeGranularity, len(x), identity))

c.execute('''INSERT INTO privacy(user, setting, IDnum)
              VALUES(?,?,?)''', (username, settype, identity))

c.execute('''INSERT INTO tags(tag1, tag2, tag3, tag4, IDnum)
              VALUES(?,?,?,?,?)''', (tag_1, tag_2, tag_3, tag_4, identity))

conn.commit()
conn.close()