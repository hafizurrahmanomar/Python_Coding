#print(dir(list_intro))
#Methods of List
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

fruits=['apple','banana','cherry','durian','eagle',"nut"]
print("// List ID Check")
print(id(fruits))
print("// append")
fruits.append("Woodcocks")
print(fruits)
print("//After append List ID Check,So List Mutable")
print(id(fruits))
print("// change/update")
fruits=['apple','banana','cherry','durian','eagle',"nut"]
fruits[3]="Mango"
print(fruits)

#Insert Items
print("// Insert=> add in a fixed position/index (index, value)")
fruits.insert(2,"Date")
print(fruits)

#all list items blank
print("// clear")
fruits.clear()
print(fruits)

#value add

name=["Hafiz","Nyeem"]
print("//value assign")
name_copy=name
print(name_copy)
print("// Value assign than append before item value add")
name_copy.append("Toha")
print(name_copy)
print(name)

#Before items value no add

nums=[2,4,5,8,10,12,10,14,10,17,20]
print("//copy=>Before items value no add")
nums_cp=nums.copy()
print(nums_cp)
print("// Value copy than append")
nums_cp.append(25)
print(nums_cp)
print(nums)
print("// Same item count")
print(nums.count(10))

#Extend List
print("//Value extend but not assign new variable,any iterable object (tuples, sets, dictionaries etc.)")
nums.extend(name)
print(nums)


# Join Two Lists =>same to extend
print("// Join Two or other Lists =>same to extend")
nums_nam=nums+name
print(nums_nam)

#add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)

fruits_list=['apple','banana','cherry']
fruits_tuple=("Mango","Melon")
print("//List extend with tuple")
fruits_list.extend(fruits_tuple)
print(fruits_list)



#Remove Specified Index
print("// pop last index of items")
num1=[2,4,28,45,30,5,8,12,14,10,17,20]
num1.pop()
print(num1)
print("// remove by pop from a fixed position/index (index)=>pop(12)")
num1=[2,4,28,45,30,5,8,12,14,10,17,20]
num1.pop()
print(num1)

#Remove Specified Item
print("//remove Specified Item (value)")
num1.remove(10)
print(num1)
print("// sort=>1 to 10 .. and a to z")
num1.sort()
print(num1)

num1.reverse()
print("//reverse=> Z to a")
print(num1)
num2=[2,3,6,8,9,45,67,20]
print("// sorted=> reverse=True , Sorting in descending order")
num3=[2,3,6,8,9,45,67,20]
num4=sorted(num3, reverse=True)
print(num4)

print("// sum ")
print(sum(num3))
print("// min ")
print(min(num3))
print("// max")
print(max(num3))

#Remove Specified Index
num3=[2,3,6,8,9,45,67,20]
print("Remove Specified Index by del[2]")
del num3[2]
print(num3)

# delete first two items
print(" remove slice by del[0:2]=>delete first two items")

del num3[0:2]
print(num3)






