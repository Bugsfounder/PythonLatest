try:
    a = int(input("Enter a Number: "))

    print(a)
except ValueError as v:
    print(v)
    print("Hello")
except Exception as e:
    print(e)

print("Done ")
