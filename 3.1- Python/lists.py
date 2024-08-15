num_list = [50, 20, 10, 40, 30]
print(num_list)
for num in num_list:
    print(num)

for index, num in enumerate(num_list):
    print(index, num)

num_list.sort(reverse=True)
print(num_list)

name_list = ['Alif', 'Rakib', 'Zahid', 'Bakul']
name_list.sort()
new_name_list = sorted(name_list)
print(new_name_list)


num_list = [50, 20, 10, 40, 30]
name_list = ['Alif', 'Rakib', 'Zahid', 'Bakul']

combined_list = num_list + name_list
print(combined_list)

combined_list_2 = num_list.extend(name_list)
print(num_list)
