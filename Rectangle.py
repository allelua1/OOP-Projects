class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

r1 = Rectangle(5,3)
print(f"Area of rectangle is: {r1.area()}")