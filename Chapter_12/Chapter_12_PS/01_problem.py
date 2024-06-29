try:
    with open("Chapter_12/Chapter_12_PS/1.txt") as f1:
        print(f1.read())
except FileNotFoundError as e:
    print(e)
except FileNotFoundError as e:
    print(e)

try:
    with open("Chapter_12/Chapter_12_PS/2.txt") as f2:
        print(f2.read())
except FileNotFoundError as e:
    print(e)
except FileNotFoundError as e:
    print(e)

try:
    with open("Chapter_12/Chapter_12_PS/3.txt") as f3:
        print(f3.read())
except FileNotFoundError as e:
    print(e)
except FileNotFoundError as e:
    print(e)

print("Done")
