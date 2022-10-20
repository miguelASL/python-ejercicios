class Polygon:
    def perimeter(self):
        print("Perimeter")

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2 * self.length * self.width

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c