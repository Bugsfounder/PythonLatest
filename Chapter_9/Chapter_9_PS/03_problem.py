import os


def generateTable(n):
    dir_paths = "Chapter_9/Chapter_9_PS/tables"
    if not os.path.isdir(dir_paths):
        os.mkdir(dir_paths)

    table = ""
    for i in range(10):
        table += f"{n} X {i+1} = {n*(i+1)}\n"

    with open(f"{dir_paths}/{n}_table.txt", "w") as fs:
        fs.write(table)


for i in range(1, 20):
    table = generateTable(i + 1)
