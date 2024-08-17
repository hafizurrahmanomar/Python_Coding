def operations(Sum, x, y):
    return Sum(x, y)

def add(a, b):
    Sum = a + b
    return Sum


print(operations(add, 2, 3)) # sum(x, y)
