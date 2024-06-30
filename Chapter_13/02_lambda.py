def square(n):
    return n * n


print(square(4))

# using lambda
# lambda arguments:expresions
square = lambda x: x * x
sum = lambda a, b, c: a + b + c
print(square(4))
print(sum(1, 2, 4))
