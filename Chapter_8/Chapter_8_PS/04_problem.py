def sum_n_numbers(n):
    if n == 0:
        return 0
    return n + sum_n_numbers(n - 1)


n = int(input("Enter a Number: "))
sum = sum_n_numbers(n)

print(sum)
