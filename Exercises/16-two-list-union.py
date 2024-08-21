# Program to find common elements in two lists with the help of set operations

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list1 = set(list1)
list2 =set(list2)

list3 = (list1 | list2)
print(list(list3))
