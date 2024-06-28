class Employee:
    a = 1

    def __init__(self):
        print("Constructor of Employee")


class Programmer(Employee):
    b = 2

    def __init__(self):
        print("Constructor of Programmer")


class Manager(Programmer):
    c = 3

    def __init__(self):
        super().__init__()
        print("Constructor of Manager")


# obj1 = Employee()
# obj2 = Programmer()
obj3 = Manager()

# print(obj1.a)  # output: 1

# # print(a.b)  # output: error
# print(obj2.a)  # output: 1
# print(obj2.b)  # output: 2

# print(obj3.a)  # output: 1
# print(obj3.b)  # output: 2
# print(obj3.c)  # output: 3
