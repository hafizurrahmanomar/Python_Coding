import math
# Sum
print(10 + 3)

# Subtract
print(10 - 3)

# Multiply
print(10 * 3)

# Divide
print(10 / 3)

#find even number or odd number (%), 2, 4, 6,8
print(10 % 3) #reminder
print( 3^2)
print(3**2)
print(4**2)
print(2**3)
print(pow(2,3))

#Square root
print(math.sqrt(9))



# 4. Combining Variables, Input/Output, and Conditionals
print("Combining Variables, Input/Output, and Conditionals")
num1 = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /, %, //, **): ")
num2 = float(input("Enter the second number: "))

# operation = input("Enter the operation (+, -, *, /, %, //, **): ")

if operation == '+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print( result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == '%':
    result = num1 % num2
    print( result)
elif operation == '//':
    result = num1 // num2
    print( result)
elif operation == '**':
    result = num1 ** num2
    print(result)
else:
    print("Invalid operation.")

