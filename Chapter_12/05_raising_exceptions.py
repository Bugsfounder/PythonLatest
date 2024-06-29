a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
if b == 0:
    raise ZeroDivisionError("Our program is not meant to divide numbers by zero")

print(f"The division a/b is {a/b}")


