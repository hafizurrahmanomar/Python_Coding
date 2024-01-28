##Lambda function => Python Lambda Functions are anonymous functions means that the function is without a name
## Syntax 
## lambda arguments :single expression which is evaluated and returned.

# argument(s) - any value passed to the lambda function
# expression - expression is executed and returned
from functools import reduce

print((lambda a:a)(10))
x=(lambda a:a) (40)
print(x)
x=lambda a:a+15
print(x(10))
## Addition
add_num =lambda a,b,c:a+b+c
print("Addition with Lambda:",add_num(10,15,25))

## multiple
multi =lambda a,b:a*b
print("Number Multiple with Lambda:",multi(10,15))

# declare a lambda function
greet = lambda : print('Hello World')
# call lambda function
greet()



## Use Lambda Functions
def my_func(n):
     return lambda a : a * n
# my_doubler = my_func(2),10
# print(my_doubler)
my_doubler = my_func(2)
print(my_doubler(23))

##  lambda function to convert a string to its upper case
name = 'Hafizur Rahman Omar'
upper_case = lambda string: string.upper()
print(upper_case(name))



## Even number
even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in even_list:
    print("even_list",item())
    
even = [lambda arg=x: arg * 2 for x in range(1,10)]
for i in even:
    print("My Even List",i())
    
## Maximum 
## Actual History True(1),False(0)=>index
Max = lambda a, b : a if(a > b) else b
print("Maximum number define Tricks",Max(10, 20))
## Minimum 
Min = lambda a, b : a if(a < b) else b
print("Minimum number define Tricks",Min(100, 20))




## map
## Iterable => String,list,tuple,Dictionary,set
## map syntax => map(function:iterable)
## print(map(function:iterable))=> map object create
## print(list(map(function:iterable)))=> list create

##normal function with map function practice
def multiply(a):
    return a*2
map_list=[1,3,6,8,10]
#print((map(lambda a:a*3,map_list)))
map_final =list((map(multiply,map_list)))
print("Normal function with map data:",map_final)



##map with lambda function practice
map_list=[1,3,6,8,10]
#print((map(lambda a:a*3,map_list)))
map_final =list((map(lambda a:a*3,map_list)))
print("Map with lambda function data:",map_final)

## filter function=>same to map() condition apply
## filter logical match than return but map function total iterable return


# Example 2: Using filter() 
# With user defined function
## Syntax of filter()
## syntax=> filter(function, iterable)
num_list = [1,2,3,10,30,4,5,6,7,8]
def even(i):
    return (i%2 == 0)
print("filter normal function used:",list(filter(even, num_list)))

## Even Number
num_list = [1,2,3,10,30,4,5,6,7,8]
final_list = list(filter(lambda x:(x % 2 == 0),num_list))
print("filter Lambda function used:",final_list)

## Even Number with rang used
final_list = list(filter(lambda x:(x % 15 == 0),range(2,51)))
print("filter Lambda function wit range used:",final_list)


## Odd Number
num_list = [3,5, 7, 20, 100,21,77, 23, 73, 61]
final_list = sorted(list(filter(lambda x:(x % 2 != 0),num_list)))
print("Odd Number:",final_list)

## Filter list from another list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
filter_list = [3,5,7,8]
result = list(filter(lambda x: x not in filter_list, numbers))
print(result) 

## Output: 
## [1, 2, 4, 6]


##A sum of all elements in a list using lambda and reduce() function wit import functools

##The code calculates the sum of elements in a list using the ‘reduce' function from the ‘functools' module. It imports ‘reduce', defines a list, applies a lambda function that adds two elements at a time, and prints the sum of all elements in the list. The output displays the computed sum.

lis1 = [5, 8, 10, 20, 50]
sum = reduce((lambda x, y: x + y), lis1)
print("Sum Used reduce function",sum)

lis2 = [2,3,4]
initial_value = 2
sum = reduce((lambda x, y: x*y), lis2,initial_value)
print("Multiply Used reduce function =",sum)

import functools

list_3 = [1, 3,100,5, 6, 2]
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, list_3))


