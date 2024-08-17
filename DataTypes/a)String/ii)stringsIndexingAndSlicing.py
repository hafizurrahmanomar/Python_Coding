
# Given String 
print("======Given String by positive indexing==============")
 
str = "BANGLADESH"
# Start Oth index to end  
print(str[0:]) #BANGLADESH 
# Starts 1th index to 4th index  
print(str[1:5])  #ANGL
# Starts 2nd index to 3rd index  
print(str[2:4])  #NG
# Starts 0th to 2nd index  
print(str[:3])  #BAN
#Starts 4th to 6th index  
print(str[4:7]) #LAD

#Negative Indexing
print("==================Negative Indexing========================================")

print(str[-1])   #H
print(str[-3])   # E
print(str[-2:])   #SH 
print(str[-4:-1]) #DES 
print(str[-7:-2]) #GLADE 
# Reversing the given string  
print(str[::-1]) #HSEDALGNAB 
print(str[-10])