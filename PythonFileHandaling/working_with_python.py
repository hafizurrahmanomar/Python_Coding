# Working With file in Python
# File create python command
# The open() function takes two parameters; filename, and mode.


# There are four different methods (modes) for opening a file:

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists
# "+" - Open a file for updating (reading and writing)

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)
#Syntax To open a file for reading it is enough to specify the name of the file:

# f = open("data.txt")
# The code above is the same as:

# f = open("data.txt", "rt")



# f = open("data.txt","x") 
# # At first file crate after run error 

# Exception Handling in Files

try:
    f = open("data.txt","x") 
    f.close()   
except:
    print("File Already Create")
finally:
    print("Finally this code ok")  
    
# Write to file in python 
# myName_add = open("data.txt",'w')  # write in text mode
myName_add = open("data.txt","w")
myName_add.write("My Name is Hafizur Rahman Omar")
myName_add.close()

# Read to file in python
readName = open("data.txt","r")
print(readName.read())
readName.close()

# Data update in file
append_info = open("data.txt","a")
append_info.write("\nI'm Bangladeshi")
append_info.close()

# Use of with...open Syntax
#r+ read and write both permission
with open("data.txt","r+") as f:
    f.write("\nPython Master Class\nDjango Master Class")
    ## Total line print 
    #print(f.read())
    ## Easy Way line by line print
    # for line in f:
    #     print(line)
     ## Other Way line by line print   
    # for line in f.readlines():
    #     print(line)
    ## All line upper case print
    # for line in f:
    #     print(line.upper())
    for line in f:
        if "Hafizur" in line:
             print(line)
         
        