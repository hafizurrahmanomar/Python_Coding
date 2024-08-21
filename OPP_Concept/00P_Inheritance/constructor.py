def my_function():
    print("Hello")

class Test:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.sum = self.x + self.y 
        print(self.sum)
        print("This is the constructor")

obj = Test(20,20)
my_function()
