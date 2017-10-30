# NarrowData.py
# --------
# Using Target Variable from Input.py and Search Tags,
# Go through Database and retrieve 10 or less csv files
# That either: 1.) Match 2+ tags
# 2.) Have something to do with the description
# OR Have this: 1.) Time range of the stored csv files occuring 5+ timestamps before uploaded csv file

from Input import getInput, getSearchTags

target = getInput()
searchTags = []
searchTags = getSearchTags()
print(target)
print(searchTags)

# for item in searchTags, search Database for match.
# Store match in dict with a number of matches
# Return the items with the highest # of matches
# dict[n, g, m] where n = name, g = (Y/N) granularity is correct, m = # of matches

