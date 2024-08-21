class Test:
    id = 10
    name = "Hafizur Rahman"
    def __info(self):
        print("Student Id", self.id)
        print("Student Name", self.name)
    
    def display(self):
        self.__info()

class Test2(Test):

    def show(self):
        self.__info()

print("// Test ")
obj = Test()
obj.display()
print(obj.id)


print("// Test2 ")
obj2 = Test2()
obj2.show()