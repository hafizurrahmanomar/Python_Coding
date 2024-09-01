class SecretFile:
    _balance = 10000
    name = ""
    
    def print_balance(self):
        print(f"The balance is {self._balance}")
    
    def set_balance(self, new_value):
        if new_value < 2000:
            print("Not allowed")
        else:
            self._balance = new_value
    
file1 = SecretFile()
file1.name = "Test"

# print(file1.balance)
file1.print_balance()
file1.set_balance(200)
file1.print_balance()
