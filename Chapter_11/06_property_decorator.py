class Employee:
    a = 1

    @classmethod
    def show(self):
        print(f"The class attribute value of a is {self.a}")

    @property
    def name(self):
        return f"Name: {self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

    @property
    def age(self):
        print(self.mage)

    @age.setter
    def age(self, age):
        self.mage = age


e = Employee()
e.a = 45
e.name = "Bugs Founder"
print(e.name)
e.show()


e.age = 32
e.age
