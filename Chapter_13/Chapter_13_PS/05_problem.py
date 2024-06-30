from functools import reduce

lst = [49, 7, 14, 21, 28, 35, 70, 42, 56, 63]


# def maximum(lst):
#     max = 0
#     for item in lst:
#         if item > max:
#             max = item
#     return max

# print(maximum(lst))

maxN = 0
maximumNum = reduce(lambda a, b: a if a > b else b, lst)
print(maximumNum)
