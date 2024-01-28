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