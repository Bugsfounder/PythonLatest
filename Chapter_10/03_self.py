# class
class Employee:
    language = "Python"  # class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


bugs = Employee()  # object
bugs.language = "GoLang"
bugs.getInfo()
bugs.greet()
