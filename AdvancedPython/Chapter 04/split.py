import re
text = "pink,r e.d,bl ue,gr.e en"
pattern = r"\."
result = re.split(pattern, text)
print(result)