class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Testing vector addition
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print("v1:", v1)
print("v2:", v2)
print("v1 + v2 =", v3)
