class Test:
    def info(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x)
        print(self.y)
        print("Show function is calling")
    
    def call_method(self):
        self.show()
    
ob = Test()
ob.info(10,20)
ob.call_method()
    


