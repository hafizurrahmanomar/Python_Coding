
class Student:

    # __init__ is known as the constructor
    def __init__(self, name, Class, id_number):
        self.name = name
        self.Class = Class
        self.id_number = id_number


    def display(self):
        print(self.name)
        print(self.Class)
        print(self.id_number)


    # def details(self):
    #     print("Student name is {}".format(self.name))
    #     print("Student Class Name: {}".format(self.Class))
    #     print("Student IdNumber: {}".format(self.id_number))
    def details(self):
        print(f"Student name is {self.name}")
        print(f"Student Class Name: {self.Class}")
        print(f"Student IdNumber: {self.id_number}")


Toha = Student("Mhamud Hasan Toha","Five","01")
# Toha.display()
Toha.details()
Nyeem = Student("Hossain Ahmed Nayeem","Haffez","02")
Nyeem.details()
Tohura = Student("Tohura Hafiz Tasnim","One","02")
print(Tohura.name)


