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
        Base.__init__(self, name)
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
        Child.__init__(self, name, age)
        self.address = address

    # To get address
    def getAddress(self):
        return self.address



# Driver code
info = GrandChild("Hafizur rahman Omar",  36,"Pabna")
print(info.getName(), info.getAge(), info.getAddress())
