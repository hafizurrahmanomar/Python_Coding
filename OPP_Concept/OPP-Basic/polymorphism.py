class Animal:
    name = ""
    age = 0
    color = ""
    
    def make_sound(self):
        print("")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} is saying Meao")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} is saying Bhukbhuk")
        
cat1 = Cat()
cat1.name = "Tom"
cat1.make_sound()

dog1 = Dog()
dog1.name = "Pluto"
dog1.make_sound()
