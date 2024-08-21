# class Base(object):
class Base:
    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

    # Constructor
    def __init__(self, name, age):
        #Base.__init__(self, name)
        super().__init__(name)
        self.age = age

    # To get name
    def getName(self):
        return self.name
    def getAge(self):
        return self.age


# Inherited or Sub class (Note Person in bracket)


class GrandChild(Child):

    # Constructor
    def __init__(self, name, age, address):
        #Child.__init__(self, name, age)
        super().__init__(name, age)
        self.address = address

    # To get address
    def getAddress(self):
        return self.address



# Driver code
info = GrandChild("Hafizur rahman Omar",  36,"Pabna")

print(f'My Name is :{info.getName()},\nage {info.getAge()},\naddress :{info.getAddress()}')
