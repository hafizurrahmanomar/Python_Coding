#Note:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and un-indexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


list_intro=[""] #main condition before list
print(type(list_intro))

myList=["python",10,10.5,True]
print(myList)
print(type(myList))

#The list() Constructor

fruits_list =list(("apple", "banana", "mango","orange","melon")) # note the double round-brackets
print(type(fruits_list))

fruits = ["apple", "banana", "mango","orange","melon"]
#Access List Items
print(fruits[0])
print(fruits[1])
print(fruits[0:2])
print(fruits[:-3])
print(fruits[1:-2])
print(fruits[:])
print(fruits[:-2])
print(fruits[-2:])



