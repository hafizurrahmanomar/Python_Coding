import re
# Example 1: Find all occurrences of digits in a string.
mystr = "How are you 20, my name is xyz 23, 89 32 1 and what is this 2 12 43"
p = r"\d+"
# result = re.findall(p, mystr)
# print(result)


# Example 2: Find all occurrences of a specific word in a string.
mystr = "How are you 20, my name is YOU You xyz 23, 89 32 1 and what is this 2 12 43"
p = r"\byou\b"
result = re.findall(p, mystr, re.IGNORECASE)
print(result)