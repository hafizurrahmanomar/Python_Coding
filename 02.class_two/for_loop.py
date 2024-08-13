name = "BongoDev"

for character in name:
    character = character + 'a'
    print(character)
    

number_list = [1, 2, 3, 45, 34, 34, 23, 123, 123, 4]
sum = 0

for n in number_list:
    sum = sum + n
    
print(sum)

# range(start, stop, step)

# start default 0
# stop
# step default 1

print("----------------")
for num in range(1, 500, 2):
    print(num)

print("----------------")
for num1 in range(1, 6):
    for num2 in range(1, 4):
        print(f"num1 is {num1} and num2 is {num2}")