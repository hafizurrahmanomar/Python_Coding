class Test:
    id = 10
    name = "JafriCode"
    def info(self):
        print("Student Id", self.id)
        print("Student Name", self.name)
    
    def display(self):
        self.info()

class Test2(Test):

    def show(self):
        self.info()


obj = Test2()
obj.info()
