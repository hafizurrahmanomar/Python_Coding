#print(dir(list_intro))
#Methods of List
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

fruits=['apple','banana','cherry','durian','eagle',"nut"]

fruits.append("Woodcocks")
print(fruits)


#Insert Items

fruits.insert(2,"Date")
print(fruits)

#all list items blank
fruits.clear()
print(fruits)

#value add
name=["Hafiz","Nyeem"]
name_copy=name
print(name_copy)
name_copy.append("Toha")
print(name_copy)
print(name)

#Before items value no add
nums=[2,4,5,8,10,12,10,14,10,17,20]
nums_cp=nums.copy()
print(nums_cp)
nums_cp.append(25)
print(nums_cp)
print(nums)

print(nums.count(10))

#Extend List
nums.extend(name)
print(nums)

# Join Two Lists =>same to extend
nums_nam=nums+name
print(nums_nam)

#add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)

fruits_list=['apple','banana','cherry']
fruits_tuple=("Mango","Melon")

fruits_list.extend(fruits_tuple)
print(fruits_list)



#Remove Specified Index
num1=[2,4,28,45,30,5,8,12,14,10,17,20]
num1.pop()
print(num1)

#Remove Specified Item
num1.remove(10)
print(num1)
num1.sort()
print(num1)

num1.reverse()
print(num1)
num2=[2,3,6,8,9,45,67,20]
print(sum(num2))
print(min(num2))
print(max(num2))

fruits=['apple','banana','cherry',"nut","Mango"]

fruits[2] ="Mango"
print(fruits)

#Remove Specified Index
del fruits[2]
print(fruits)

# delete first two items

del fruits[0:2]
print(fruits)






