# Write a Python program to remove duplicates from a list.


# list = [ int(x) for x in input().split()]

# # 2 3 3 4 5 2 5 -> 2 3 4 5

# final_list=[]

# st=''
# for x in list:
#     if str(x) not in st:
#         st = st+str(x)
#         final_list.append(x)

# print(final_list)

# Write a Python program to check a list is empty or not

# list = [ int(x) for x in input().split()]
# list1=[]
# if list==[]:
#     print("empty list")
# else:
#     print("not empty")



# Write a Python program to clone or copy a list
# list = [ int(x) for x in input().split()]
# list1=[]

# list1=list.copy()
# print(list1)

# Write a Python program to find the list of words that are longer than n from a given list of words.

# list = [x for x in input().split()]

# n= int(
#     input("enter the n ")
# )
# list1=[]
# for x in list :
#     if len(x)>n:
#         list1.append(x)

# print(f"Required list is {list1}")


# Write a Python function that takes two lists and returns True if they have at least one common member.

# def is_any_commom_member(l1,l2):
#     for x in l1:
#         if x in l2:
#             return True
            
#     return False

# list1=[1,2 ,3,4]
# list2=[0,9,745,41]

# print( is_any_commom_member(list1, list2))

#  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# 0,4,5

# list =[ int(x) for x in input().split()]
# list1=[]
# for i in range(len(list)-1):
#     if i==0 or i==4 or i==5:
#         pass
#     else:
#         list1.append( list[i])

# print(list1)

# Write a Python program to print the numbers of a specified list after removing even numbers from it.


# list =[ int(x) for x in input().split()]
# list1=[]

# for x in list:
#     if x%2==0:
#         list.remove(x)

# print(list)


# Write a Python program to generate all permutations of a list in Python.
import itertools
listx =[ int(x) for x in input().split()]
list1=[]

print(  list(itertools.permutations( listx ) ))