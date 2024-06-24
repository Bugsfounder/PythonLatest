def greatest(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max


max = greatest(2, 3, 4)
print(max)
