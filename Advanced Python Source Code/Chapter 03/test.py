import re
text = "th fox The quick fox fox brown fox jumps over the lazy dog"
pattern = r'^fox'
match = re.search(pattern, text)
if match:
    print(match.group())
else:
    print("No match found")