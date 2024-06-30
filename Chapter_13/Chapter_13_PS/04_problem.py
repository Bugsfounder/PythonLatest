lst = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

fLst = filter(lambda x: True if x % 5 == 0 else False, lst)

print(list(fLst))
