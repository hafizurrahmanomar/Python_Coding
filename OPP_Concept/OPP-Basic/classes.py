class Cat:
    name = ""
    age = 0
    color = ""

cat1 = Cat()
cat1.name = "Tom"
cat1.age = 7
cat1.color = "Blue"





class CatBetter:
    def __init__(self, name_input, age_input, color_input):
        self.name = name_input
        self.age = age_input
        self.color = color_input

cat2 = CatBetter("Tom2", 7, "Blue")