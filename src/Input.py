# Input.py
# --------
# Asks user what target variable is
# Asks user additional tags are; parse this into list

def getInput():         # Returns user Input
    return userIn

def getSearchTags():    # Returns user determined search tags in list
    return searchTags
    return

userIn = input("Enter target variable: ")
addTags = input("Enter additional search tags (Seperated by ','): ")
searchTags = addTags.split(",")

getInput()
getSearchTags()


