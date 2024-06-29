n = int(input("Enter a number: "))

tblLst = [f"{n} X {i+1} = {n* (i + 1)}\n" for i in range(10)]

print(tblLst)


try:
    with open("Chapter_12/Chapter_12_PS/table.txt", "a") as f:
        tblStr = f"\nTable of {n}\n"
        for item in tblLst:
            tblStr += item
        f.write(tblStr)
        # print(tblStr)
except Exception as err:
    print(err)
