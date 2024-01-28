# Python program to
# demonstrate private members
# "__" double underscore represents private attribute.
# Private attributes start with "__".

# Creating a Base class
class Base:
    def __init__(self):
        self.name = "Hafiz"
        self.__passwoard = "@#Hafiz1234@#"


# Creating a derived class
class MyInfo(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__passwoard)


# MyInfo code
MyName = Base()
print(MyName.name)
