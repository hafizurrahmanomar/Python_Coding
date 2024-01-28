import re
text = "How are you Ali ! Price of X mobile is $230203"
pattern = r"\$"
result = re.sub(pattern, 'Rs-/', text)
print(result)