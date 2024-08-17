# def add(x, y, z):
#     yield x
#     yield y
#     yield z

# gen = add(10,20,30)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def generate_num(x):
#     for i in range(x):
#         yield i

# gen = generate_num(10)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# def infinite_num():
#     x = 0
#     while True:
#         x += 1
#         yield x

# gen = infinite_num()
# print(next(gen))
# print(next(gen))

# def even_num(n):
#     for i in range(n):
#         if i %2 == 0:
#             yield i

# gen = even_num(10)
# print(next(gen))
# print(next(gen))
# print(next(gen))

def square(n):
    for i in range(n):
        yield i**2

gen = square(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))