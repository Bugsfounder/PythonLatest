n = int(input("Enter a Number: "))
for i in range(n):
    print(" " * (n - i), end="")
    print("*" * (i * 2 + 1), end="")
    print()
