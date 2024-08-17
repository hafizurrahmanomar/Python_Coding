class A:
    x = 10
    y = 20

    def showa(self):
        print("Function of A class")

class B(A):
    z = 15
    
    def showb(self):
        print("Function of B class")

class C(B):
    def showc(self):
        print("Function of C class")
obj = C()
obj.showc()