name = input("Enter name: ")
marks = int(input("Enter marks: "))
PhoneNumber = int(input("Enter Phone Number: "))

mstr = (
    "The name of the student is {}, his/her marks are {} and phone number is {}".format(
        name, marks, PhoneNumber
    )
)

print(mstr)
