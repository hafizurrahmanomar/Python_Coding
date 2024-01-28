class A:
    def showa(self):
        print("A class")

class B():
    def showb(self):
        print("B class")

class C(A, B):
    def showc(self):
        print("C Class")

obj = C()
obj.showb()
obj.showa()
obj.showc()
