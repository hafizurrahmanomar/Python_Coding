my_list = [25, 35, 40]

x = my_list[1] # access
print(x)

my_list[2] = 45 # change/update
print(my_list)

my_list.append(55) # add
print(my_list)

my_list.insert(3, 50) # add in a fixed position/index (index, value)
print(my_list)

my_list.remove(50) # remove (value)
print(my_list)

my_list.pop(2) # remove from a fixed position/index (index)
print(my_list)

for num in my_list:
    num = num - 5
    print(num)