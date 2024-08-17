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



import functools
print("//Minimum  value find out list with lambda function;Actual History True(1),False(0)=>index")
list_3 = [1, 3, 100, 5, 6, 2]
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, list_3))
