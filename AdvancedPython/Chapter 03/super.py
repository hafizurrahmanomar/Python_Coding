# class Parent():
#     def __init__(self):
#         print("Constructor of parent class")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of child class")

# obj = Child()

class A:
    def show(self):
        print("A class")

class B(A):
    def show(self):
        super().show()
        print("B class")

obj = B()
obj.show()

