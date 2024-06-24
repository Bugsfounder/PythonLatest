file_path = "Chapter_9/Chapter_9_PS/log.txt"

with open(file_path, "r") as f:
    data = f.read()
    
if "python" in data:
    print("yes")
else:
    print("No")


