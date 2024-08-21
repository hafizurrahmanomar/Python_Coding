class Test:
    def __init__(self):
        self.f_name = ""
        self.l_name = None

    def info(self, firstName, lastName):
        self.f_name = firstName
        self.l_name = lastName

    def show(self):
        print(self.f_name)
        print(self.l_name)
        print("Show function is calling=> f_name and l_name")

    def name_calling(self):
        self.show()
        print(f"My Name is:{self.f_name} {self.l_name}")
        # print(self.f_name + self.l_name)



ob = Test()
ob.info("Hafizur Rahman", "Omar")
ob.name_calling()
