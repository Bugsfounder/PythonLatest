try:
    a = int(input("Enter Number a: "))
    b = int(input("Enter Number b: "))
    print(a / b)
except ZeroDivisionError as er:
    print("Infinite")

except Exception as err:
    print(err)
