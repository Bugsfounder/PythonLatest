sub1 = int(input("Enter Marks of Subject 1: "))
sub2 = int(input("Enter Marks of Subject 2: "))
sub3 = int(input("Enter Marks of Subject 3: "))

totalMarks = sub1 + sub2 + sub3

totalParcentage = (totalMarks / 300) * 100

if totalParcentage > 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print(f"Congratulations!! You have Passed. with {totalParcentage}%")
else:
    print("You Failed")
