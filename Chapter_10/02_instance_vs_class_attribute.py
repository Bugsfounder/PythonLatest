# class
class Employee:
    language = "Python"  # class attribute
    salary = 1200000


bugs = Employee()  # object
bugs.language = "GoLang"  # an instance (object) attribute
print(bugs.language, bugs.salary)

# instance attribute always take place over class attributes
