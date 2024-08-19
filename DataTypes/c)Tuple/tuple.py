# Tuple items are ordered, unchangeable, and allow duplicate values.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


# allow duplicate values.
print("// Tuple items are ordered, unchangeable, and allow duplicate values")
num = (1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11)
name = ("Hafiz", "Nyeem", "Toha","Toha", 12, 13, 14, 15.5)
tup = tuple("Hello python")
print(num)
print(name)
print(tup)


# Join Two Tuples
print("// Join Two Tuples")
tuplePlus = num + tup
print(tuplePlus)

# Tuple Length
print("// Tuple Length")
print(len(tup))

# Python - Update Tuples # Very important thing
print("// Python - Update Tuples  tricks# Very important thing")
country = ("BD", "USA", "UK")
countryTuple = list(country)
countryTuple[2] = "china"
country = tuple(countryTuple)
print(country)

# Index value
print("// Index value")
print(name.index("Toha"))

# Access Tuple Items
print("// Access Tuple Items")
print(tup[0])
print(tup[1])

# Range of Indexes
print("// Range of Indexes")
print(tup[2:7])

# Negative Indexing
print("// Negative Indexing")
print(tup[-8:-2])


# Value Count
print("// Value Count")
Name = "Hafizur Rahman"
print(Name.count("a"))

# Unpacking a tuple:Python, we are also allowed to extract the values back into variables. This is called "unpacking"
print('// Unpacking a tuple:Python, we are also allowed to extract the values back into variables. This is called "unpacking"')

fruits = ("apple", "banana", "cherry")

(a, b, c) = fruits

print(a)
print(b)
print(c)

# Loop Through a Tuple
print("// Loop Through a Tuple")
fruits = ("apple", "banana", "cherry","Mango")
for i in fruits:
    print(i)
