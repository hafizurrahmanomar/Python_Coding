
print("// String print")
name = "Hafizur Rahman Omar"
print(name)
print('Hafizur Rahman Omar')
multiLine = """Name:Hafizur Rahman Omar,
Vilage:Ruppur,
Thana:Aminpur,
Dist:Pabna"""

# String Type checking
print("// String Type checking")
print(type(name))
print(multiLine)
print(type(""))
print(type(''))
print(type(""" """))
print("It's not possible")

# Escape Characters

print(" // Escape Characters")
print('It\'s not possible')
print('He says "I am learning python master class"')
print("He says 'I am learning python master class' ")
print("He says \"I am learning python master class\"")

# one backslash return
print("// one backslash return")
backslash = "This will insert one \\ (backslash)."
print(backslash)

# Carriage Return
print("// Carriage Return")

txt1= "Hello\rpython programmer"
txt2= "Hello\rpython\r\rprogrammer"
txt3= "Hello\rpython\r\rprogrammer\r\r\r"
print(txt1)
print(txt2)
print(txt3)

# This example erases one character (backspace):
print("// erases one character (backspace)")
txt = "Hello \bprogrammer!"
print(txt)

# New line and tab

print("// New line and tab ")
print("Name:Hafizur Omar\nVilage:Ruppur\nThana:Aminpur\nDist:Pabna")
print("Name:Hafizur Omar\n\tVilage:Ruppur\n\t\tThana:Aminpur\n\n\t\t\tDist:Pabna")

# Looping Through a String

print("// Looping Through a String ")
for i in "Bangladesh":
    print(i)

# Check String
print("// String Check/find ")

language = "python,javascript,java,PHP"

print("python" in language)
print("python" not in language)
print("HTML" in language)
print("HTML" not in language)
