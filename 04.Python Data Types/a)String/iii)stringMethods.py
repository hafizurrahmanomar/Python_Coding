myString = "Python is a Popular programming Language."

#String method call
#print(dir(myString))
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'


#String length count with whitespaces

print(len("Python is a Popular programming Language."))

# converts first character to uppercase and others to lowercase
print(myString.capitalize())

#Python String uppercase()
print(myString.upper())

#Python String lowercase()
#convert all characters to lowercase(lower-case same to casefold)

print("PYTHON IS A POPULAR PROGRAMMING LANGUAGE".lower())
print("PYTHON IS A POPULAR PROGRAMMING LANGUAGE".casefold())


#Python String first character uppercase=> title()
print(myString.title())
print(myString)

text = 'Python is fun'

# find the index of is
result = text.index('is')
print(result)

#Python String strip() Method
#Remove spaces at the beginning and at the end of the string
fruits = "     Mango     "

fruits = fruits.strip()

print(fruits, "is my favorite fruits")

b = ",,,,,rrttgg.....banana....rrr"

b = b.strip(",.grt")

print(b)

#Python String join() Method
#Join all items in a tuple into a string, using a star character as separator
myTuple = ("Hafiz", "Toha", "Nayeem")

x = "**".join(myTuple)

print(x)

#Join all items in a dictionary into a string, using the word "##" as separator:

myDict = {"name": "John", "country": "Norway"}
mySeparator = "##"

x = mySeparator.join(myDict)

print(x)
#Python String swapcase()

# converts lowercase to uppercase and vice versa
name = "haFiZur rHmaN"
print(name.swapcase())

#Python String count()
# number of occurrence of 'g'
print(myString.count("G"))
print(myString.count("g"))


#Python String center()
x= "python"
x=x.center(12,"#")
print(x)


#Replace String
a = "I love my country"
replaceString = a.replace("country", "mother")
print(replaceString)
#print(a.replace("country", "mother"))

#Split String

myString ="Hello,Bangladesh"

print(myString.split(","))

#Python String endswith()
print("=====Python String endswith()===Start =====")

# check if the message ends with Bangladesh
message = "Hello,Bangladesh."
print(message.endswith("Bangladesh"))
# returns False
print(message.endswith("Bangladesh."))
# returns True
print(message.endswith("Hello"))
# returns False
print(message.endswith("Hello,Bangladesh."))
# returns True
print(message.endswith("Hello,Bangladesh"))
# returns False

text = "programming is easy"
result = text.endswith(('programming', 'python'))

# prints False
print(result)

result = text.endswith(('python', 'easy', 'java'))

#prints True
print(result)

# With start and end parameter
# 'programming is' string is checked
result = text.endswith(('is'), 0, 14)

# prints True
print(result)

print("=====Python String endswith()===End =====")

#Python String expandtabs()

print("=====Python String expandtabs()===Start =====")

str = 'a\tab\tabc'

# no argument is passed
# default tabsize is 8

result = str.expandtabs()
print(result)

#expandtabs() With Different Argument
print('Original String:', str)

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))

# tabsize is set to 3
print('Tabsize 3:', str.expandtabs(3))

# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))

# tabsize is set to 5
print('Tabsize 5:', str.expandtabs(5))

# tabsize is set to 6
print('Tabsize 6:', str.expandtabs(6))

print("=====Python String expandtabs()===end =====")

