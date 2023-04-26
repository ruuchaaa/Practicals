from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())
