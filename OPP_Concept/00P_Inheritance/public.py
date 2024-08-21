class Test:
    id = 10
    name = "Hafizur Rahman Omar"
    def info(self):
        print("Student Id", self.id)
        print("Student Name", self.name)
    
    def display(self):
        self.info()

class Test2(Test):

    def show(self):
        self.info()

obj = Test()
print("// Same result")
obj.display()
print("// Same result")
obj.info()
obj = Test2()
print("// Same result")
obj.info()
