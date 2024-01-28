# # A lambda function is a small anonymous function.

# # A lambda function can take any number of arguments, but can only have one expression.

# # Syntax
# # lambda arguments : expression

a = lambda x: x
print(a(10))
a = lambda x: x * 2
print("Double of 10 is :", a(10))

# # Even numbers from the old list
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
after_filter = list(filter(lambda x: (x % 2 == 0), num))
print(after_filter)

after_mapping = list(map(lambda x: x * 2, num))
print(after_mapping)
