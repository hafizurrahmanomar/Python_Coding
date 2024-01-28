# # String Formatting
# # old way
toha_info ="My Name is {},My Village Name:{}, My Age: {}".format("Toha","Pabna",6)
print(toha_info)

hafiz_info ="My Name is {0},My Village Name:{1}, My Age: {2}".format("Hafiz","Ruppur",36)
print(hafiz_info)

name = input("Please Enter your Name: ")
village = input("Please Enter your Village Name: ")
age = input("Please Enter your Age: ")

# my_info ="My Name is {},My Village Name:{}, My Age: {}".format(name,village,age)
# print(my_info)
## String formatting Easy Way 
my_bio = f"My Name: {name}\nMy Age: {village}\nMy Age: {age}"

print(my_bio)

