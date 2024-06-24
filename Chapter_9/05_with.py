f = open("Chapter_9/file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("Chapter_9/file.txt") as f:
    print(f.read())

# you don't have to explicitly close the file
