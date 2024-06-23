num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))
num4 = int(input("Enter Number 4: "))

greatest = num1

if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
if num4 > greatest:
    greatest = num4

print(greatest)
