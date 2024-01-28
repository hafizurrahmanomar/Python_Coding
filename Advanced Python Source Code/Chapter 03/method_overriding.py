class A:
    def show(self):
        print("JafriCode from A class")

class B(A):
    def show(self):
        # super().show()
        print("JafriCode from B class")

a = A() 
a.show()
b = B()
b.show()