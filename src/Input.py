# Input.py
# --------
# Asks user what target variable is
# Asks user additional tags are; parse this into list

def getInput():         # Returns user Input
    return userIn

def getSearchTags():    # Returns user determined search tags in list
    return newTag
    return

userIn = input("Enter target variable: ")
addTags = input("Enter additional search tags (limit 4); Seperated by ',': ")
searchTags = addTags.split(",")

# We only search through 4 tags
newTag = [0,0,0,0]
if(len(searchTags) > 4):
    newTag[0] = searchTags[0]
    newTag[1] = searchTags[1]
    newTag[2] = searchTags[2]
    newTag[3] = searchTags[3]

elif(len(searchTags) <= 4):
    n = 0
    while (n < len(searchTags)):
        newTag[n] = searchTags[n]
        n = n + 1


getInput()
getSearchTags()





