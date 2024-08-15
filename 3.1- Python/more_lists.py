num_list = [50, 20, 10, 40, 30]
print(num_list)

num_list.clear() # empties the list
print(num_list)

num_list = [50, 20, 10, 40, 30, 10]
x = num_list.index(40)
print(x)

count = num_list.count(10)
print(count)

print(len(num_list))

new_list = num_list.copy()