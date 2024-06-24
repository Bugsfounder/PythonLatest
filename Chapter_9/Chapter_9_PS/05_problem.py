lst = ["Jack", "donkey", "games", "often"]
file_path = "Chapter_9/Chapter_9_PS/file.txt"


def findAndReplaceDonkey(filePath, lst):
    dataRep = ""
    data = ""
    with open(filePath, "r") as fs:
        data = fs.read()

    dataRep = data
    for item in lst:
        dataRep = dataRep.replace(item, "#" * len(item))

    with open(filePath, "w") as fs:
        fs.write(dataRep)


findAndReplaceDonkey(file_path, lst)
