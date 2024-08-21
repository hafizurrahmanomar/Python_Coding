# Problem-02: Take two numbers as input, print “Zamala” if one is negative and one is positive. Else print “Thik Ase”
# Solution:

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
    print("Zamala")
else:
    print("Thik Ase")