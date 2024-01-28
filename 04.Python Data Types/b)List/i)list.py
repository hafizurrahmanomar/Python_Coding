#Note:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and un-indexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


list_intro=[""] #main condition before list
print(type(list_intro))

#print(dir(list_intro))
#Methods of List
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

myList=["python",10,10.5,True]
print(myList)
print(type(myList))

#The list() Constructor

fruits =list(("apple", "banana", "mango","orange","melon")) # note the double round-brackets
print(type(fruits))

#Access List Items
print(fruits[0])
print(fruits[1])
print(fruits[0:2])
print(fruits[:-3])
print(fruits[1:-2])
print(fruits[:])
print(fruits[:-2])
print(fruits[-2:])

#Change Item Value
fruits[0] = "nut"
print(fruits)
print(fruits)

