l = [1, 4, 6, 234, 6, 764]

for i in l:
    print(i)

t = (6, 231, 43, 54, 2, 43)
for i in t:
    print(i)


s = "bugs"

for c in s:
    print(c)

d = {1: 3, 5: 3, "name": "bugs"}

# for key in d:
for key in d.keys():
    print(key, d[key])
