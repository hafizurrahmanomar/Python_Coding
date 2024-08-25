# Calculate of triangle using heron's formula
# Step 1: Calculate "s" (half of the triangles perimeter): s = a+b+c/2
# Step 2: Then calculate the area= sqrt(s*(s-a)*(s-b)*(s-c))
a = float(input("Enter first side of triangle:"))
b = float(input("Enter second side of triangle:"))
c = float(input("Enter third side of triangle:"))
s = (a+b+c)/2
print("Half of the triangles perimeter=",s)
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Calculate the triangle Area=",area)
