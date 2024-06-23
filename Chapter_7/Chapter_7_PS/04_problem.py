num = int(input("Enter the Number: "))

isPrime = False
if num == 1:
    print(f"{num} is not a Prime Number.")
elif num > 1:
    for i in range(2, num):
        print(i)
        if num % i == 0:
            isPrime = True
            break
if isPrime:
    print(f"{num} is not a Prime Number.")
else:
    print(f"{num} is a Prime Number.")
