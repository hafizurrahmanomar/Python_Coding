class ComputerInterface:
    def build(self):
        pass
    
    def print_specs(self):
        pass
    
class HpComputer(ComputerInterface):
    def build(self):
       print("This is mY computer")
c = HpComputer()
c.build()
c.print_specs()
        