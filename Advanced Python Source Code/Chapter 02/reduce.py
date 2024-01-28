from functools import reduce 
lst = [1,2,3,4,5,6,7,8,9,10]
result = reduce(lambda x, y:x+y, lst, 10)
print(result)

# Example 3: Finding the maximum element of a list using reduce()
# Example 4: Combining strings in a list using reduce()

# num = [1,2,90,12,344,125,64]
# max = reduce(lambda x, y:x if x>y else y, num)
# print(max)

# lst = ["pink","yellow","black","white","gold"]
# r = reduce(lambda x, y: x+' '+y, lst)
# print(r)