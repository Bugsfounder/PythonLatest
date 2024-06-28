class Vector:
    def __init__(self, lst):
        self.l = lst

    def __len__(self):
        return len(self.l)


# test the implementation
v1 = Vector([1, 2, 3])

print(len(v1))
