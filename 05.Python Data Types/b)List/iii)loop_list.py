#Loop Through a List
fruit_list=['apple', 'banana', 'cherry', 'Mango', 'Melon']
for i in fruit_list:
    print(i)

#Loop Through the Index Numbers and item
fruit_list=['apple', 'banana', 'cherry', 'Mango', 'Melon']

for i in range(len(fruit_list)):
    print(i, fruit_list[i])
    
#List Comprehension
new_list=[]
for i in fruit_list:
    if "M" in i:
        new_list.append(i)

        
print(new_list)
