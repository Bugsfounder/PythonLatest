# dunder methods
# p1 + p2  # p1.__add__(p2)
# p1 - p2  # p1.__sub__(p2)
# p1 * p2  # p1.__mul__(p2)
# p1 / p2  # p1.__truediv__(p2)
# p1 // p2  # p1.__floordiv__(p2)
# __str__() # used to set what gets displayed upon calling str(obj)
# __len__() # used to set what gets displayed upon calling.__len__() or len(obj)


class Number:
    # a = 1
    # b = 2

    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n


n = Number(1)
m = Number(2)

# print(m.n + n.n)
print(m + n)  # throw error if __add__ is not present
