import os

# Directory whose content you want to list
directoryPath = "/home/bugsfounder/workspace"

# contents of the directory
contents = os.listdir(directoryPath)

# iterating over contents list and printing all items items
for item in contents:
    print(item)
