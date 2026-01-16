class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    

r1 = Rectangle(5, 3)
r2 = Rectangle(4, 5)

print(r1.area())
print(r1.perimeter())

print(r2.area())
print(r2.perimeter())