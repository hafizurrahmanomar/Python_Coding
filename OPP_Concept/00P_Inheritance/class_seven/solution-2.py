import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Example usage
if __name__ == "__main__":
    # Circle
    circle = Circle(5)
    print("Circle:")
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}")

    # Triangle
    triangle = Triangle(3, 4, 5)
    print("\nTriangle:")
    print(f"Area: {triangle.area():.2f}")
    print(f"Perimeter: {triangle.perimeter():.2f}")

    # Square
    square = Square(4)
    print("\nSquare:")
    print(f"Area: {square.area():.2f}")
    print(f"Perimeter: {square.perimeter():.2f}")
    
    
    
    
    
    
    
    
    