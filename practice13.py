# Write a Python program to get the frequency of the elements in a list.

from itertools import count


list = [int(x) for x in input().split()]
list1=[]
st=''

# for x in list:
#     if str(x) not in st:
#         print(f"count of {x} is {list.count(x)}")
#         st=st+str(x)


# 3 4 5 6 7 7 8 9 9 9 0 1 3 4
# # Write a Python program to get unique values from a list.
# for x in list:
#     if str(x) not in st:
#         list1.append(x)
#         st=st+str(x)

# print(list1)


# Write a Python program to create a list by 
# concatenating a given list which range goes from 1 to n

# n= int( input("enter the value of n "))

# # ['p','q']-> ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# for i in range(1,6):
#     for x in list:
#         list1.append(x+str(i))

# print(list1)

# Write a Python program to find common items from two lists.

l1=[1,2,3,4,5,6,7,8,9,0,12,23]

for x in list:
    if x in l1 and str(x) not in st:
        st=st+str(x)
        list1.append(x)

print( list1)