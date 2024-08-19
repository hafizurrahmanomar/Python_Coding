name = "bangladesh, Dhaka"

print(name.capitalize())
print(name.upper())
print(name.lower())

print()

name = "   Hello   "
print(name.strip())

print()

name = "United States"
print(name.split(' '))

full_name = "Abdus Salam"
name_list = full_name.split(' ') # ['Abdus', 'Salam']

first_name = full_name.split(' ')[0]
last_name = full_name.split(' ')[1]

print()

id = "123"
print(id.isnumeric())

print()
old = "Python is the the worst"

new = old.replace("worst", "best")
print(new)

print()
print(new.count("best"))