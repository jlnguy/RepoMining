# NarrowData.py
# --------
# Using Target Variable from Input.py and Search Tags,
# Go through Database and retrieve 10 or less csv files
# That either:  1.) Match 2+ tags
#               2.) Have something to do with the description
# OR Have this:
#           1.) Time range of the stored csv files occuring
#                5+ timestamps before uploaded csv file

# Currently NarrowData.py wants to do:
#       1.) If data matches the timestamp of the uploaded file, add to list
#       2.) If data matches 2+ tags targeted, add to list
#       3.) If data tags match description, add to list



from Input import getInput, getSearchTags
from Upload import getFirstStamp, getLastStamp, getTaggedList


import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

target = getInput()
searchTags = []
searchTags = getSearchTags()
print(target)
print(searchTags)

uploadTagList = getTaggedList()



# for item in searchTags, search Database for match.
# Store match in dict with a number of matches
# Return the items with the highest # of matches
# dict[n, g, m] where n = name, g = (Y/N) granularity is correct, m = # of matches

