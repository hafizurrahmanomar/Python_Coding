class A:
    def showa(self):
        print("A class")

class B(A):
    def showb(self):
        print("B class")

class C(A):
    def showb(self):
        print("B class")
    def showc(self):
        print("C class")
    
obj = C()
obj.showc()
obj.showa()
obj = B()
obj.showa()
obj.showb()