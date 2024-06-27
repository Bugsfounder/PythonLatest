import math


class Calculator:
    def __init__(self, number) -> None:
        self.number = number

    def square(self):
        # a*a
        return self.number**2

    def cube(self):
        # a*a*a
        return self.number**3

    def squareRoot(self):
        # return math.sqrt(self.number)
        return self.number ** (1 / 2)


cal = Calculator(4)

print(cal.squareRoot(), cal.cube(), cal.square())
