file_path = "Chapter_9/Chapter_9_PS/file.txt"


def findAndReplaceDonkey(filePath, word):
    dataRep = ""
    with open(filePath, "r") as fs:
        data = fs.read()
        dataRep = data.replace(word, "######")

    with open(filePath, "w") as fs:
        fs.write(dataRep)


findAndReplaceDonkey(file_path, "Donkey")
