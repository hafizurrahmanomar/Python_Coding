# Given the list num_list = [1, 4, 5, 23, 10, 12, 15, 19, 25]
# Loop through the list and print the numbers that are divisible by 5
# Solution:

num_list = [1, 4, 5, 23, 10, 12, 15, 19, 25]
for num in num_list:
    if num % 5 == 0:
        print(num)
