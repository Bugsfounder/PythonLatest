file_path = "Chapter_9/Chapter_9_PS/file.txt"
file_path_cp = "Chapter_9/Chapter_9_PS/file_copy.txt"

data = ""
with open(file_path, "r") as fs:
    data = fs.read()

with open(file_path_cp, "w") as fs:
    fs.write(data)
