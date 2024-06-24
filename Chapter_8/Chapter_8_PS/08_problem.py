def multipleTable(n, multiplier=1, limit=10):
    if multiplier > limit:
        return
    print(f"{n} X {multiplier} = {n*multiplier}")
    multipleTable(n, multiplier + 1, limit)


n = int(input("Enter a number: "))
multipleTable(n)
