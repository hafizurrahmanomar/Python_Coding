class A:
    def showa(self):
        print("A class")

class B(A):
    def showb(self):
        print("B class")

class C(B):
    def showc(self):
        print("C class")


class D(C):
    def showd(self):
        print("D class")


obj = D()
obj.showb()
obj.showa()
obj.showd()
