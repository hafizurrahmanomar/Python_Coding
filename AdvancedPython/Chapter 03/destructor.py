class Test:
    def __del__(self):
        print("This is the destructor...")
    
    def __init__(self):
        print("This is the construcotr...")
    
    def show(self):
        print("JafriCode")

obj = Test()
obj.show()