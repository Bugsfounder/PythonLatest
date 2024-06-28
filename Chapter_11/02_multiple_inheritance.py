class Employee:
    company = "ITC"
    name = "default name"

    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")


class Coder:
    language = "Python"

    def printLanguages(self):
        print(f"Our of all the languages here is your language: {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def showLanguage(self):
        print(
            f"The name is {self.company} and he is good with {self.language} language."
        )


a = Employee()
b = Programmer()

# print(a.company, b.company) 

b.show()
b.printLanguages()
b.showLanguage()
