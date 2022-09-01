# Write a Python program to extract specified size of 
# strings from a give list of string values.
# 

# list = [ x for x in input().split()]
n=8

list1=[]
# Python list exercises practice solution

# for x in list :
#     if len(x)==8:
#         list1.append(x)

# print( list1)


# Write a Python program to find the difference between consecutive numbers in a given list.
# [1, 1, 3, 4, 4, 5, 6, 7]

# temp_list =[1, 1, 3, 4, 4, 5, 6, 7]

# for i in range(1,len(temp_list)):
#     list1.append(temp_list[i]-temp_list[i-1])

# print( list1 )

# Write a Python program to remove all 
# elements from a given list present in another list.

def all_uncommon_element_of_list1(l1,l2):
    result=[x for x in list1 if x not in list2]
    return result


list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2= [2, 4, 6, 8]

lis=all_uncommon_element_of_list1(list1,list2)

print(lis)