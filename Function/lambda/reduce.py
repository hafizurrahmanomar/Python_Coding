
##A sum of all elements in a list using lambda and reduce() function wit import func tools

##The code calculates the sum of elements in a list using the ‘reduce' function from the ‘func tools' module. It imports ‘reduce', defines a list, applies a lambda function that adds two elements at a time, and prints the sum of all elements in the list. The output displays the computed sum.

from functools import reduce
print("//Total Value Add=> reduce with lambda function")
lis1 = [5, 8, 10, 20, 50]
Sum = reduce((lambda a, b: a + b), lis1)
print("Sum Used reduce function", Sum)

print("//Multiply=> reduce with lambda function ")
lis2 = [2, 3, 4]
initial_value = 2
Sum = reduce((lambda a, b: a * b), lis2, initial_value)
print("Multiply Used reduce function =", Sum)


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