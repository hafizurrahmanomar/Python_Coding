
#Set items are unordered, unchangeable, and do not allow duplicate values.
print("// Set items are unordered, unchangeable, and do not allow duplicate values.")
num_set={1,2,3,4,5,5,6,6,7,8,9,10}

print(num_set)
print(type(num_set))
print(dir(num_set))
print(len(num_set))

#Access Items
print("// Access Items")

for x in num_set:
    print(x)


#Add Items
#Once a set is created, you cannot change its items, but you can add new items.

print("// Once a set is created, you cannot change its items, but you can add new items.")
fruit = {"apple"}
# Add value not assign variable
fruits = fruit.add("Mango")
print(fruit)

# Union
print("// Union")
num_1 = {1,2,3}
num_2 = {4,4,5,3,6}
print(num_1 | num_2)
# print(dir(num_1))

