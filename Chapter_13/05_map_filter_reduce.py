from functools import reduce

# map example
l = [1, 2, 3, 4, 5]

square = lambda x: x * x

sqLst = map(square, l)

print(list(sqLst))


# filter example
def even(n):
    if n % 2 == 0:
        return True
    return False


onlyEven = filter(even, l)
print(list(onlyEven))


# reduce example
def sum(a, b):
    return a + b


def mul(a, b):
    return a * b


print(reduce(sum, l))
print(reduce(mul, l))
