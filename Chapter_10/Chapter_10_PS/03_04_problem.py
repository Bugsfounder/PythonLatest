class PS_3:
    a = 3

    # problem 4
    @staticmethod
    def hello():
        print("Good morning!")


obj = PS_3()
print(obj.a)  # prints the class attribute because instance attribute is not present
obj.a = 0  # Instance attribute is set
print(obj.a)  # prints the Instance attribute because instance attribute is present
print(PS_3.a)  # but  not changing the class attribute

# problem 4
obj.hello()
PS_3.hello()
