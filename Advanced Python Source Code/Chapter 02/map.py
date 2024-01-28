lst = [1,2,3,4,5]
result = map(lambda x: x - 1, lst)
print(list(result))
# x ** 2 => x * x

# Example 2: Converting strings in a list to uppercase using map()
# Example 3: Finding the length of each string in a list using map()
# Example 4: Using map() with multiple iterables

lst = ["pink","yellow","black","white","gold"]
# result  = map(lambda x: x.upper(), lst)
# print(list(result))

result  = map(lambda x: len(x), lst)
print(list(result))

lst1 = [1,2,3]
lst2 = [40,50,60]
product = map(lambda x, y:x*y, lst1, lst2)
print(list(product))