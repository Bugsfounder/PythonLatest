f1 = file_path_cp = "Chapter_9/Chapter_9_PS/file1.txt"
f2 = file_path_cp = "Chapter_9/Chapter_9_PS/file2.txt"

with open(f1) as f:
    content1 = f.read()

with open(f2) as f:
    content2 = f.read()

if content1 == content2:
    print("Yes files are identical")
else:
    print("No files are not identical")
