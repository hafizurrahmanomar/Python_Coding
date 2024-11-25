import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
my_circle = Circle(5)

print(f"Area of the circle: {my_circle.area():.2f}")

print(f"Perimeter of the circle: {my_circle.perimeter():.2f}")