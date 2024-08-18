def info(first_name, last_name, age = 46):
    full_name = first_name + " " + last_name
    print(f"Full Name is {full_name} and age is: {age}")
    
info(last_name="Rahman", first_name="Hafizur", age=34)

info(last_name="Rahman", first_name="Hafizur")


def total_numbers(*args): # 1, 23, 234 , ....
    Sum = 0
    for num in args:
        Sum = Sum + num
    print(Sum)

total_numbers(1, 2)
total_numbers(1, 20, 50)
total_numbers(1, 20, 50, 200)
