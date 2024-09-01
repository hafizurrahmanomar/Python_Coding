file = open("test.txt", "r")
# file.read()
print(file.read())

file.close()

l = ["a", "b", "c"]
with open("test.txt", "w+") as file:
    file.writelines(l)
    print(file.read())

# noinspection PyBroadException
try:
    file = open("wrong.txt", "r")
except Exception:
    print("Error occurred")
finally:
    file.close()

print("TEST")