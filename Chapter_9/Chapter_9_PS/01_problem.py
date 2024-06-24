with open("Chapter_9/Chapter_9_PS/poems.txt") as f:
    data = f.read()
    # print(data)
    if "twinkle" in data:
        print("Yes, There is twinkle in file.")
    else:
        print("twinkle is not present")
