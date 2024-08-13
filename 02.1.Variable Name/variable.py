#Variable Names Rules:
#A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (Name, NAME and name are three different variables)

#Keywords in Python are reserved words that can not be used as a variable name, function name, or any other identifier.
'''
and	,as,assert,	break,class,continue,def,del,elif,else,except,False,finally,
for,from,global,if,import,in,is,lambda,None,nonlocal,not,or,pass,raise,return,
True,try,while,with,yield

'''
#Rules for Naming Python Variables
'''
snake_case
MACRO_CASE
camelCase
CapWords

MYVARIABLE
MY_VARIABLE
myvariable
_myvariable
myvariable_
myvariable1
myvariable_1
my_variable
_my_variable
My_Variable
MACRO_CASE
myVariable #camelCase


'''
#Variable names are case-sensitive
# Creates a string variable
name="Nyeem"
Name="Hafizur Rahman Omar"  
NAME="Toha"
print(Name)
print(name)
print(NAME)

#Many Values to Multiple Variables
Name,name,NAME = "Hafizur Rahman Omar", "Nyeem", "Toha"
print(Name)
print(name)
print(NAME)

#One Value to Multiple Variables

Name=name=NAME = "Hafizur Rahman Omar"
print(Name)
print(name)
print(NAME)

# Unpack a list

namesList = ['Hafizur Rahman Omar', 'Nyeem', 'Toha']

Name,name,NAME =namesList
print(Name)
print(name)
print(NAME)


#Output Variables
# Creates an integer variable

result =(5+7+10)
print(result)
x,y,z=5,7,10
print(x,y,z)
print(x+y+z)
print(x*y*z)

# Creates a floating point variable
number  = 1000.0   
print(number)

num1=20
num2=10.5
num1=num2
print(num1)

#Python Local Variable
def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10))

#Global Variables

python = "human readable programing language"

def pythonfunc():
  print("Python is " + python)

pythonfunc()
