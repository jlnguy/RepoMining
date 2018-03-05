# Asks for the file that the user is uploading
# Tags the file with appropiate tags, adds them to the database
# parses CSV for Q1, Q2, Q3.

from datetime import datetime
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

def getFileName():
    return filename

filename = input("Enter file to upload: ")
print("You uploaded: ", filename)
print('')
descp = input("Enter a description to describe the file: ")
print('')
tar = input("Enter target variable description for file: ")
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
'''
col2 = ''
col3 = ''
table = ''
'''
#c.execute('''SELECT IDnum FROM description
#                    WHERE IDnum = (SELECT max(IDnum) FROM description);'''.\
#                     format(IDnum=col2, description=table))

#c.execute('''SELECT MAX(IDnum) AS IDnum FROM description''')
c.execute('''SELECT COALESCE(MAX(IDnum), 0) FROM description''')
#c.execute('''SELECT IDnum FROM description WHERE IDnum = (SELECT MAX(IDnum) FROM description)''')

temp = ''

for item in c:
    temp = item[0]

identity = temp

identity = identity + 1


c.execute('''INSERT INTO description(name, target, info, IDnum)
              VALUES(?,?,?,?)''', (filename, tar, descp, identity))
# Timestamps
# Timestamps are not parsed (Still has DATE x x x x format)
y, x = inputFile(filename)
fi = x[1]
la = x[(len(x) - 1)]

if (typeGranularity == 'Daily'):
    firstStamp = datetime.strptime(fi, '%Y-%m-%d')
    lastStamp = datetime.strptime(la, '%Y-%m-%d')
elif(typeGranularity == 'Monthly'):
    firstStamp = datetime.strptime(fi, '%Y-%m')
    lastStamp = datetime.strptime(la, '%Y-%m')
elif(typeGranularity == 'Yearly'):
    firstStamp = datetime.strptime(fi, '%Y')
    lastStamp = datetime.strptime(la, '%Y')
else:
    print("Incorrect format. Granuarity must be in 'Daily/Monthly/Yearly' format.")
    firstStamp = 0
    laststamp = 0

c.execute('''INSERT INTO granularity(first, last, type, itemNum, IDnum)'''
             '''VALUES(?,?,?,?,?)''', (firstStamp, lastStamp, typeGranularity, len(x), identity))

c.execute('''INSERT INTO privacy(user, setting, IDnum)'''
              '''VALUES(?,?,?)''', (username, settype, identity))

c.execute('''INSERT INTO tags(tag1, tag2, tag3, tag4, IDnum)'''
              '''VALUES(?,?,?,?,?)''', (tag_1, tag_2, tag_3, tag_4, identity))

conn.commit()
conn.close()

print('Your file has been uploaded. Thank you!')
