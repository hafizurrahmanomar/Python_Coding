
d1 = {
    "key1": "A",
    "key2": "B"
}

print(d1["key1"])
print(d1.get("key3"))
print(d1.get("key3", ""))


d1["key1"] = "C"
print(d1["key1"])

# Adding
d1["key3"] = "D"
print(d1)

d1.update({"key4": "E", "key5": "F"})
print(d1)

del d1["key3"]
print(d1)

d1.pop("key4")
print(d1)

print(d1.keys())
print(d1.values())
print(d1.items())

for key, value in d1.items():
    print(key, value)
    
d1.setdefault("key7", [])
print(d1)
d1["key7"] = 90
print(d1)
