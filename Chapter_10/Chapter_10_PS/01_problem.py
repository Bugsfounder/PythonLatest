class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, language, age):

        self.name = name
        self.salary = salary
        self.language = language
        self.age = age


bugs = Programmer("Bugs", 123000, "Go", 20)

print(bugs.name, bugs.language, bugs.age, bugs.salary)
