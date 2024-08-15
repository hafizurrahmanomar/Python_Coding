def print_name_and_city(first_name, last_name, city = "Dhaka"):
    full_name = first_name + " " + last_name + ", "
    print(full_name, city)
    
print_name_and_city("Azmain", "Adel", "Khulna")

print_name_and_city(last_name="Adel", first_name="Azmain")

def sum_numbers(*args): # 1, 23, 234 , ....
    sum = 0
    for num in args:
        sum = sum + num
    print(sum)

sum_numbers(1, 2)
sum_numbers(1, 200, 5050)
sum_numbers(1, 200, 5050, 202)
