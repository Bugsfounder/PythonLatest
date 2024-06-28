class Vector_2D:

    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")


class Vector_3D(Vector_2D):
    def __init__(self, i, j, k) -> None:
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")


a = Vector_2D(1, 2)
b = Vector_3D(4, 2, 3)
a.show()
b.show()
