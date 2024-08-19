# String interpolation =>string.format()
print("// String formatting old way")
# Use the format() method to insert numbers into strings
name = "Hafizur Rahman"
age = 36
txt = "My name is {}, and age {}"
print(txt.format(name, age))
txt = "My name is {}, and age {}".format(name, age)
print(txt)

# Default order
print("// Default order")
myString = "{} {} {}".format("Hafiz", "Nyeem", "Toha")
print(myString)

# Positional Formatting
print("// Positional Formatting")
myString = "{0} {2} {1}".format("Hafiz", "Nyeem", "Toha")
print(myString)

# Keyword Formatting
print(" // Keyword Formatting")
myString = "{c} {a} {b}".format(a="Hafiz", b="Nyeem", c="Toha")
print(myString)

# Formatting of Integers
print("// Integer formatting ")
num = "{0:b}".format(16)
print("Binary representation of 16 is ")
print(num)

# Formatting of Floats
print('// Formatting of Floats ')
num = "{0:e}".format(103.6458)
print("Exponent representation of 165.6458 is ",num)


# Rounding off Integers
print("// Rounding off Integers")
num = "{0:.2f}".format(10 / 6)
print("Ten-sixth is : ",num)


print("// String alignment")

# String alignment
print(" // String alignment")
address = "|{:<10}|{:^10}|{:>15}|".format("Pabna", "Dhaka", "Bangladesh")
print("right, center and left alignment with Formatting: ")
print(address)

print("// String formatting new way")

myName = input("Enter your name: ")
myFather = input("Enter your father name: ")
myAge = input("Enter your age: ")

# String interpolation =>f-string:string.format()
myInfo = f"My Name is {myName}, My Father is {myFather}, My age  {myAge}"

print("My full Info", myInfo)
name = "Hafiz"
age = 36
print("// Very difficult way")
print("The name is %s and age is %d" % (name, age))
print("The id is %d" % age)