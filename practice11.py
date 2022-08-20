# Write a Python program to get the difference between the two lists.

# list1=[1,2,3,4]
# list2=[2,5,6,7]

# list=[]

# for x in list1:
#     if x not in list2 and x not in list:
#         list.append(x)

# print(list)

#  Write a Python program to convert a list of characters into a string.

# list = [ x for x in input().split()]

# str=''

# for x in list:
#     str= str+x

# print( str )

# Write a Python program to find the index of an item in a specified list.

list=[1 , 55, 67,8,2 ,4]

def find_index( lis,a):
    for i in range(len(lis)-1):
        if a==lis[i]:
            return i
    
    return "not present"

print( 
    find_index(list , 52)
)