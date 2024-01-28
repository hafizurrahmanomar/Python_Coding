import re 
text = "asyouew asdow asyours sdyourd #ar$e* you _12  94_898-34^@80 YOU yoU  J\n fri   Code *&#92 82 43 13 fjas askld wlek ds8238 823 sdlfjas"
# .
# s will match space, tab or newline
# word Character -> A- Z, a-z, 0- 9, _
pattern = r"\Byou\B"
list_matches = re.findall(pattern, text, re.IGNORECASE)
print(list_matches)

"""
* zero or more
+ one or more
? zero or one
{n} n time
{n,} at least n time
{n,m} between n and m
{,m} at most m time
{0,} zero or more like *
"""


