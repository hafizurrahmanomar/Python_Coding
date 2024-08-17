import re
# Example 1: Search for the first occurrence of a word in a string.

text = "How are you Faisal Zamir."
pattern = r"\bFaisal\b"
match = re.search(pattern, text)
if match:
    print(f"Data is present at {match.group()} at position of {match.start()}")
else:
    print("Not matching...")    

# Example 2: Search for the first occurrence of a digit in a string.

mystr = "price of new laptop is $2903209."
pattern = r"\d"
match = re.search(pattern, mystr)
if match:
    print(f"Price is present that is {match.group()} at position of {match.start()}")
else:
    print("Not matching...")    

