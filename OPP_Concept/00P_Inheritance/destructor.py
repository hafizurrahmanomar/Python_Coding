class Test:
    def __del__(self):
        print("This is the destructor")
    
    def __init__(self):
        print("This is the constructor")
    
    def Show(self):
        print("Hafizur")

obj = Test()
obj.Show()