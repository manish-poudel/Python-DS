# Operator overloading concept

class Vector:

    def __init__(self, size):
        self._coordinates = [0] * size

    def __getitem__(self, item):
        return self._coordinates[item]

    def __setitem__(self, key, value):
        self._coordinates[key] = value

    def __len__(self):
        return len(self._coordinates)

    def __add__(self, other):
        if len(self) != len(other):
            return ValueError("Size doesn't match")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __str__(self):
        return '<' + str(self._coordinates)[1: -1] + '>'
