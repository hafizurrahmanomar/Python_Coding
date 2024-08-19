#  For Loop
print("// For Loop")
name = "Hafizur Rahman Omar"
char_list = []
for Chr in name:
    char_list.append(Chr)
print("Char_list:", char_list)

print("// For loop with range")
num = 21
num_list = []
for number in range(num):
    num_list.append(number)
print("num_list =", num_list)

# List Comprehension as code simplicity
print("// List Comprehension as code simplicity wit for loop")
myName = "Hafiz"
myNameList = [my_chr for my_chr in myName.upper()]
print("My Name Char= ", myNameList)
print("// List Comprehension as code simplicity with range")
my_num = 31
myNumber = [num for num in range(2,my_num,3)]
print("My Number List = ", myNumber)
print("//even number find out=> List Comprehension  with range one condition")
myNumber = [num for num in range(my_num) if num % 2 == 0]
print("My Number List = ", myNumber)
print("//even number find out=> List Comprehension  with range two condition")
myNumber = [num for num in range(my_num) if num % 2 == 0 if num % 10 == 0]
print("My Number List = ", myNumber)

# Loop Through a List
print("// Loop Through a List")
fruit_list = ['apple', 'banana', 'cherry', 'Mango', 'Melon']
for i in fruit_list:
    print(i)

# Loop Through the Index Numbers and item
print("// Loop Through the Index Numbers and item")
fruit_list = ['apple', 'banana', 'cherry', 'Mango', 'Melon']

for i in range(len(fruit_list)):
    print(i, fruit_list[i])

# List Comprehension
print("// List Comprehension")
new_list = []
for i in fruit_list:
    if "M" in i:
        new_list.append(i)

print(new_list)
