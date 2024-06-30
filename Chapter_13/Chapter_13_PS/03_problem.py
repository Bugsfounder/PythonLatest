lst = [str(7 * i) for i in range(1, 11)]

lstStr = ""

for index, item in enumerate(lst):
    lstStr += str(item)
    if index < len(lst) - 1:
        lstStr += "\n"

print(lstStr)

# second way
s = "\n".join(lst)
print(s)
