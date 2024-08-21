# parent class
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


# child class
class Student(Person):
    def __init__(self, name, age, dob):
        self.sName = name
        self.sAge = age
        self.dob = dob
        # inheriting the properties of parent class
        super().__init__("",0)

    def displayInfo(self):
        print(self.sName, self.sAge, self.dob)


obj = Student("Hafiz", 36, "16-03-1986")
obj.display()
obj.displayInfo()
