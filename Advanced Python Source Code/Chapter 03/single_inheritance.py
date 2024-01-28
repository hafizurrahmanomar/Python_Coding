class A:
    def showa(self):
        print("A class")

class B(A):
    def showb(self):
        print("B class")

obj = B()
obj.showb()
obj.showa()
