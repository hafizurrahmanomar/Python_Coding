
## filter function=>same to map() condition apply
## filter logical match than return but map function total iterable return

# Example 2: Using filter()
# With user defined function
## Syntax of filter()
## syntax=> filter(function, iterable)

num_list = [1, 2, 3, 10, 30, 4, 5, 6, 7, 8]
def even(a):
    return a % 2 == 0
print("//Even Number=> filter normal function used")
print("filter normal function used:", list(filter(even, num_list)))

print("//Even Number=> filter lambda function used")
num_list = [1, 2, 3, 10, 30, 4, 5, 6, 7, 8]
final_list = list(filter(lambda a: (a % 2 == 0), num_list))
print("filter Lambda function used:", final_list)

'''
print("//Even Number=> map=> lambda function used return true and false")
num_list = [1, 2, 3, 10, 30, 4, 5, 6, 7, 8]
final_list = list(map(lambda a: (a % 2 == 0), num_list))
print("map=> Lambda function used:", final_list)
'''

print("//Even Number with rang used=> filter => lambda function used")
final_list = list(filter(lambda a: (a % 15 == 0), range(2, 51)))
print("filter Lambda function wit range used:", final_list)

print("//odd Number=> filter => lambda function used")
num_list = [3, 5, 7, 20, 100, 21, 77, 23, 73, 61]
final_list = sorted(list(filter(lambda a: (a % 2 != 0), num_list)))
print("Odd Number:", final_list)


print("//Filter list from another list")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
filter_list = [3, 5, 7, 8]
result = list(filter(lambda a: a not in filter_list, numbers))
print(result)

## Output:
## [1, 2, 4, 6]

lst = [1,2,3,4,5,6,7,8,9,10]
result = filter(lambda x: x % 2 == 0, lst)
print(list(result))

# Example 2: Filtering out strings that contain a specific substring using filter()
# Example 3: Filtering out negative numbers from a list using filter()
# Example 4: Filtering out empty strings from a list using filter()
# Example 5: Using filter() with multiple conditions

# lst = ["pink","yellow","black","white","gold"]
# result = list(filter(lambda x: 'a' not in x, lst))
# print(result)

# nm = [1,2,0,-3,3,-5,-9]
# obj  = filter(lambda x: x>=0, nm)
# result = list(obj)
# print(result)

# lst = ["pink","","yellow","","black","white","gold"]
# result = list(filter(lambda x: x!="", lst))
# print(result)

num = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,13]
obj  = filter(lambda x: x>3 and x<10, num)
result = list(obj)
print(result)