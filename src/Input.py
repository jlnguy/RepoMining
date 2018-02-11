# Input.py
# --------
# Asks user what target variable is
# Asks user additional tags are; parse this into list

def getInput():         # Returns user Input
    userIn = input()
    return userIn

def getSearchTags():    # Returns user determined search tags in list
    return listOfTags
    return

def userIn(bool):
    if (bool == True):
        target = input("Enter target variable")
    return target

def putTags (bool):
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

    return newTag

listOfTags = putTags(bool)

print('What is your target variable?')
select = input()
print("Your target variable is: ", select)

# search through DB for target variable (including name, tags, description)
# Return and display items

def searchDB(t_var):
    results = [0, 0, 0]
    return results

alist = searchDB(select)

if (alist[1] == 0):
    print('No results found.')
    print('Would you like to upload files to support your analysis?')
    uploadQ = input('Y/N:    ')
    if (uploadQ == 'Y'):
        # upload
        print('Call Upload.py')
    elif (uploadQ == 'N'):
        print('User did not want to upload data.')
        # do nothings





