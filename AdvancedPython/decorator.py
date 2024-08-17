# def deco(func):
#     def wrapper():
#         print("There are different websites to learn IT, like")
#         func()
#         print("Also you can follow others")
#     return wrapper

# @deco
# def jafri():
#     print("Udemy.com")
# jafri()
# # result = deco(jafri)
# # result()


def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase
def jafri1():
    return "faisal zamir"
# wrper = uppercase(jafri1)
# print(wrper())
print(jafri1())