myList = [1, 2, 4, 2, 3]

squaredList = []
for item in myList:
    squaredList.append(item * item)

print(squaredList)


# the same thing can be done easily using list comprehensions

squaredList = [item * item for item in myList]
print(squaredList)
