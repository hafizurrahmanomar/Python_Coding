numbers = [1, 2, 3, 3, 3, 4]
print(numbers)

num_set = set(numbers) # list to set conversion
print(num_set) # {1, 2, 3, 4}

numbers = list(num_set) # set to list conversion
print(numbers) # [1, 2, 3, 4]


num_set_2 = {5, 8, 9}

print()
print(num_set | num_set_2)

for num in num_set:
    print(num)
    
print()
print()
print()


num_set = {1, 2}
print(num_set)

num_set.add(3)
print(num_set)

num_set.add(3)
print(num_set)