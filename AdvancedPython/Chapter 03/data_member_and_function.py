class Student:
    # Data Members
    sid = 1
    sname = "Faisal Zamir"

    # Member Function
    def show_std_info(self):
        print("Student ID", self.sid)
        print("Student Name", self.sname)

obj = Student()
obj.sid = 90
obj.sname = "JafriCode"
obj.show_std_info()
obj2 = Student()
obj2.show_std_info()