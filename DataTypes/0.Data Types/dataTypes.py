# ========Data Types===============

# Numeric - int, float, complex
# String - str
# Sequence - list, tuple, range
# Mapping - dict
# Boolean - bool
# Set - set, frozenset
# Binary - bytes, bytearray, memoryview
# None - NoneType

# integer Data type.
x = 20
print(x, "Data type is ", type(x))

# float data type.
y = 20.345
print(y, "Data type is ", type(y))

# complex Data type.
z = 20 + 3j
print(z, "Data type is ", type(z))

# =======Sequence data type Start====

# list Data type.
fruits = ["apple", "banana", "cherry"]
print(fruits, "Data type is ", type(fruits))

# tuple Data type.
fruits = ("apple", "banana", "cherry")
print(fruits, "Data type is ", type(fruits))

# range Data type.
range = range(10)
print(range, "Data type is ", type(range))

# =======Sequence data type End====

# Mapping data type
# Dictionary Data type.

dict_ = {"name": "Hafizur rahman", "age": 36, "address": "Pabna"}
print(dict_, "Data type is ", type(dict_))

# Boolean Data Type.

isTrue = True
isFalse = False
print(isTrue, "Data type is ", type(isTrue))
print(isFalse, "Data type is ", type(isFalse))

# Set data type.

setData = {"Hafizur rahman", "Toha", "Nayem"}
print(setData, "Data type is ", type(setData))

frozensetdata = ({"Hafizur rahman", "Toha", "Nayem"})
print(frozensetdata, "Data type is ", type(frozensetdata))

# bytes data type
a = b"Hello"
print(a, "Data type is ", type(a))

# bytearray data type

b = bytearray(5)
print(b, "Data type is ", type(b))

# memoryview data type

c = memoryview(bytes(5))
print(c, "Data type is ", type(c))

# None data type
d = None
print(d, "Data type is ", type(d))
