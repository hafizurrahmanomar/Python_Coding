class Student:
    # Data Members
    id = 1
    name = "Hafizur Rahman Omar"

    # Member Function
    def show_std_info(self):
        print("Student ID:", self.id)
        print("Student Name:", self.name)


obj = Student()
obj.id = 90
obj.name = "Hafizur"
obj.show_std_info()
obj2 = Student()
obj2.show_std_info()
