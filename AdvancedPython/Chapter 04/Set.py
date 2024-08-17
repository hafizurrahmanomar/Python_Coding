import re
text = "39438DKLKds_"
pattern = "[^\w]"
result = re.search(pattern, text)

if result:
    print("Matched...")
else:
    print("Not matched")