# class
class Employee:
    language = "Python"  # class attribute
    salary = 1200000

    # dunder method which is automatically called
    def __init__(self, name, salary, language):
        print("I am creating an object")
        self.name = name
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


bugs = Employee("Bugs", 1200000, "Go")  # object
print(bugs.name, bugs.language, bugs.salary)
bugs.getInfo()
