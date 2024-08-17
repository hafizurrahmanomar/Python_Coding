##Lambda function => Python Lambda Functions are anonymous functions means that the function is without a name
## Syntax 
## lambda arguments :single expression which is evaluated and returned.

# argument(s) - any value passed to the lambda function
# expression - expression is executed and returned

from functools import reduce

print("// Single line expression")
print((lambda a: a)(10))

print("// lambda function assign variable than value add")
x = (lambda a: a)(40)
print(x)

print("// lambda function default value assign variable than value add")
x = lambda a: a + 15
print(x(10))

print("// Single line expression")
print((lambda a, b, c: a + b + c)(10, 15, 25))


print("// lambda function assign variable than value add")
add_num = lambda a, b, c: a + b + c
print("Addition with Lambda:", add_num(10, 15, 25))

print("//multiple=> use lambda function ")
multi = lambda a, b: a * b
print("Number Multiple with Lambda:", multi(10, 15))


print("// declare a lambda function than call lambda function ")
greet = lambda: print('Hello World')
# call lambda function
greet()

print("// function in lambda function but value pass be carefully ")
def my_func(n):
    return lambda a: a * n

my_doubler = my_func(2)
print(my_doubler(23))


print("// lambda function to convert a string to its upper case ")
name = 'Hafizur Rahman Omar'
upper_case = lambda string: string.upper()
print(upper_case(name))


print("// lambda function => Even number ")
even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in even_list:
    print("even_list", item())

even = [lambda arg=x: arg * 2 for x in range(1, 10)]
for i in even:
    print("My Even List", i())

print("//Maximum value find out(only two ) with lambda function;Actual History True(1),False(0)=>index")
Max = lambda a, b: a if (a > b) else b
print("Maximum number define Tricks", Max(10, 20))

print("//Minimum  value find out (only two ) with lambda function;Actual History True(1),False(0)=>index")
Min = lambda a, b: a if (a < b) else b
print("Minimum number define Tricks", Min(100, 20))


## map
## Iterable => String,list,tuple,Dictionary,set
## map syntax => map(function:iterable)
## print(map(function:iterable))=> map object create
## print(list(map(function:iterable)))=> list create

print("// normal function with map function practice")
def multiply(a):
    return a * 2


map_list = [1, 3, 6, 8, 10]
# print((map(multiply, map_list)))
map_final = list((map(multiply, map_list)))
print("Normal function with map data:", map_final)


print("// map with lambda function practice")
map_list = [1, 3, 6, 8, 10]
#print((map(lambda a:a*3,map_list)))
map_final = list((map(lambda a: a * 3, map_list)))
print("Map with lambda function data:", map_final)

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


##A sum of all elements in a list using lambda and reduce() function wit import func tools

##The code calculates the sum of elements in a list using the ‘reduce' function from the ‘func tools' module. It imports ‘reduce', defines a list, applies a lambda function that adds two elements at a time, and prints the sum of all elements in the list. The output displays the computed sum.
print("//Total Value Add=> reduce with lambda function")
lis1 = [5, 8, 10, 20, 50]
Sum = reduce((lambda a, b: a + b), lis1)
print("Sum Used reduce function", Sum)

print("//Multiply=> reduce with lambda function ")
lis2 = [2, 3, 4]
initial_value = 2
Sum = reduce((lambda a, b: a * b), lis2, initial_value)
print("Multiply Used reduce function =", Sum)

import functools
print("//Minimum  value find out list with lambda function;Actual History True(1),False(0)=>index")
list_3 = [1, 3, 100, 5, 6, 2]
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, list_3))
