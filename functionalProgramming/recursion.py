## Python Recursive Function
## Recursion function means that a function calls itself.
def factorial(n):
    if n==1:
        return 1
    else: return n*factorial(n-1)
print(factorial(6))

# user input
num = 3
 
# check if the input is valid or not
if num < 0:
  print("Invalid input ! Please enter a positive number.")
elif num == 0:
  print("Factorial of number 0 is 1")
else:
  print("Factorial of number", num, "=",factorial(num))

'''
factorial(3)          # 1st call with 3
3 * factorial(2)      # 2nd call with 2
3 * 2 * factorial(1)  # 3rd call with 1
3 * 2 * 1             # return from 3rd call as number=1
3 * 2                 # return from 2nd call
6                       # return from 1st call

'''
## recursive() itself call 996 times
# def recursive():
#     return recursive()
# recursive()
##Using a recursive function to calculate the sum of a sequence
## Q: 1+2+3+....+100 =?
def sum(n):
    return n + sum(n-1) if n > 0 else 0


result = sum(100)
print(result)
