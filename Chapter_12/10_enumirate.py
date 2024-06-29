l = [3, 534, 54, 23, 423]

index = 0
for item in l:
    print(f"the item number {index} is {item}")
    index += 1

# this can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"the item number {index} is {item}")
