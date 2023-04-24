# Write a Python program to create a tuple. 
# touple=(1,2,3)
# num1,num2,num3=touple
# print(num1)


# Write a Python program to add an item in a tuple.

tuplex=(1,2,3,4)
listx= list(tuplex) # convert tuple into list
listx.append(6) #append item in list

print(listx) 
tuplex= tuple(listx) #convert tuple in list
print(tuplex) # print tuple

