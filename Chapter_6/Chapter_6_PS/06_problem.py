marks = int(input("Enter Your Marks: "))

if marks < 0 and marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("Ex")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("F")
