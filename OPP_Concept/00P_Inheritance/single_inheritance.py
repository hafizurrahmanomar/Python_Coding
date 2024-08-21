class A:
    def Single(self):
        print("A class")


class B(A):
    def Multi(self):
        print("B class")


obj = B()
obj.Single()
obj.Multi()
obj1=A()
obj1.Single()

