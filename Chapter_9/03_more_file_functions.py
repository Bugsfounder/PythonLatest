f = open("Chapter_9/file.txt")

# print(f.read())
# print(f.readline())  # first line
# print(f.readline())  # second line
# print(f.readline())  # third line
# print(f.readline())  # fourth line
# print(f.readline())  # fifth line if not return empty string
# print(f.readline())  # if not return empty string
# print(f.readline())  # if not return empty string
# print(f.readlines())

# lines = f.readlines()
# print(lines, type(lines))  # type <List>

# read file using while loop
line = f.readline()
while line != "":
    line = f.readline()
    print(line)
f.close
