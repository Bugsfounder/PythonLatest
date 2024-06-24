file_path = "Chapter_9/Chapter_9_PS/log.txt"

with open(file_path, "r") as f:
    data = f.readline()
    line = 1
    while data != "":
        data = f.readline()
        line += 1
        if "python" in data:
            print(line)
            break
    else:
        print("no")
