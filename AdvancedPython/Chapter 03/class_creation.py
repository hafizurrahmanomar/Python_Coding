# class Jafri:
#     a = 10 # data memebr
#     b = 20 # data member
#     def myfun(self):    # memebr function
#         print("This is my functioin ")

# # Object creation 
# myobj = Jafri()
# myobj.myfun()
# print(myobj.a)
# print(myobj.b)

class Add:
    a = None
    b = None
    def adding(self):
        self.a = 10
        self.b = 20
        return self.a + self.b

obj = Add()
print(obj.adding())


