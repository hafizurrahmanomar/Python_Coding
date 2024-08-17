class Test:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.sum = self.x + self.y 
        print(self.sum)
        print("This is the construcotr...")
    def other(self):
        print("Hello")

obj = Test(20,20)
obj.other()
    