class Test:
    id = 10
    name = "JafriCode"
    def _info(self):
        print("Student Id", self.id)
        print("Student Name", self.name)
    
    def display(self):
        self._info()

class Test2(Test):

    def show(self):
        self._info()


# obj = Test2()
# obj.show()
obj = Test()
obj._info()
