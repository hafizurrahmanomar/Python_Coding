nums = [1, 2]

#print(nums[3])
y = 0

# noinspection PyBroadException
try:
    x = 3 / y
    print(x)
except Exception:
    print("cant do")
finally:
    print("THE END")
    


print()
print()
try:
    x = 6
    if x % 2 == 0:
        raise Exception("I wont allow this")
except Exception as e:
    print(e)
    
    