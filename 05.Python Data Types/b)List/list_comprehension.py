# # For Loop
name = "Hafizur Rahman Omar"
char_list = []
for chr in name:
    char_list.append(chr)
print("Char_list:", char_list)

num = 21
num_list = []

for number in range(num):
    num_list.append(number)
print("num_list", num_list)

# # List Comprehension as code simplicity
myName = "Hafiz"
myNameList = [chr for chr in myName.upper()]
print("My Name Char: ", myNameList)

my_num = 31
myNumber = [num for num in range(my_num)]
print("My Number List : ", myNumber)
myNumber = [num for num in range(my_num) if num % 2 == 0]
print("My Number List : ", myNumber)
myNumber = [num for num in range(my_num) if num % 2 == 0 if num % 10 == 0]
print("My Number List : ", myNumber)
