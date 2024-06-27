# class
class Employee:
    # name = "Bugs"
    language = "Python"  # class attribute
    salary = 1200000


bugs = Employee()  # object
bugs.name = "Bugs"  # an instance (object) attribute
print(bugs.language, bugs.salary, bugs.name)


manisha = Employee()
manisha.name = "manisha"
print(manisha.salary, manisha.language, manisha.name)


# Here name is instance (object) attribute and salary and language are class attributes as they directly belong to the class.
