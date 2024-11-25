import math
class Circle:
    circleCount = 0
    
    def __init__(self, radius):
        self.radius = radius
        Circle.circleCount += 1
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    @staticmethod
    def count():
        return Circle.circleCount
    
    # counter = staticmethod(count)

# Example usage
print(Circle.counter())

my_circle = Circle(5)
my_circle_2 = Circle(10)

print(my_circle_2.counter())