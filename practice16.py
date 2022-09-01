# Write a Python program to compute average of two given lists. 

# l1=[1, 1, 3, 4, 4, 5, 6, 7]
# l2=[0, 1, 2, 3, 4, 4, 5, 7, 8]
# # 3.823529411764706
# s1=0
# s2=0
# len1=len(l1)
# len2=len(l2)

# for x in l1:
#     s1=s1+x

# for x in l2:
#     s2+=x

# avg_of_lists= ((s1/len1)  + (s2/len2) )/ 2

# print( avg_of_lists)




# Write a Python program to count integer in a given mixed list.

list=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

def count_of_integer(list):
    count=0
    for x in list:
        if isinstance(x , int):
            count=count+1
    
    return count

print(
    f"Number of integers in list : {count_of_integer(list) }"
)