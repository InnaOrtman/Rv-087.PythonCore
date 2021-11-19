class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.list = []

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

Vector(7, 8)

print(v1.list)