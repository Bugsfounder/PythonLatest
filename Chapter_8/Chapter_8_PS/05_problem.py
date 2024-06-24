import sys

print(
    sys.getrecursionlimit()
)  # 1000, if you give n more than 1000 as argument then it will say "maximum recursion depth exceeded while calling a Python object" as error


def pattern(n):
    if n == 0:
        return
    if n > 0:
        print("*" * n, end="")
        print()
        pattern(n - 1)


n = int(input("Enter a Number: "))
pattern(n)
