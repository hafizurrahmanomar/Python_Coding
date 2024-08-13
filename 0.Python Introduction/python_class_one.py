# 1. Variables and Arithmetic Operations
print("Variables and Arithmetic Operations")
a = 5
b = 10
c = a + b  # Addition
d = b - a  # Subtraction
e = a * b  # Multiplication
f = b / a  # Division
g = b % a  # Modulus
h = b // a  # Floor Division
i = a ** 2  # Exponentiation (a raised to the power of 2)

print("a =", a)
print("b =", b)
print("Addition: a + b =", c)
print("Subtraction: b - a =", d)
print("Multiplication: a * b =", e)
print("Division: b / a =", f)
print("Modulus: b % a =", g)
print("Floor Division: b // a =", h)
print("Exponentiation: a ** 2 =", i)
print()

# 2. Input and Output
print("Input and Output")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello,", name + "! You are", age, "years old.")
print()

# 3. Conditionals
age = int(input("Enter your age: "))
print("Conditionals")
if age < 18:
    print("You can't have NID now.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a bura now.")
print()

# 4. Combining Variables, Input/Output, and Conditionals
print("Combining Variables, Input/Output, and Conditionals")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /, %, //, **): ")

if operation == '+':
    result = num1 + num2
    print("The result of", num1, "+", num2, "is", result)
elif operation == '-':
    result = num1 - num2
    print("The result of", num1, "-", num2, "is", result)
elif operation == '*':
    result = num1 * num2
    print("The result of", num1, "*", num2, "is", result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("The result of", num1, "/", num2, "is", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == '%':
    result = num1 % num2
    print("The result of", num1, "%", num2, "is", result)
elif operation == '//':
    result = num1 // num2
    print("The result of", num1, "//", num2, "is", result)
elif operation == '**':
    result = num1 ** num2
    print("The result of", num1, "**", num2, "is", result)
else:
    print("Invalid operation.")
