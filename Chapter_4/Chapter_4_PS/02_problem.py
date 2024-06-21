student1 = int(input("Enter Marks Student 1:"))
student2 = int(input("Enter Marks Student 2:"))
student3 = int(input("Enter Marks Student 3:"))
student4 = int(input("Enter Marks Student 4:"))
student5 = int(input("Enter Marks Student 5:"))
student6 = int(input("Enter Marks Student 6:"))
student7 = int(input("Enter Marks Student 7:"))
# allStudentMarks = [
#     student1,
#     student2,
#     student3,
#     student4,
#     student5,
#     student6,
#     student7,
# ]
allStudentMarks = []
allStudentMarks.append(student1)
allStudentMarks.append(student2)
allStudentMarks.append(student3)
allStudentMarks.append(student4)
allStudentMarks.append(student5)
allStudentMarks.append(student6)
allStudentMarks.append(student7)
allStudentMarks.sort()
print(allStudentMarks)
