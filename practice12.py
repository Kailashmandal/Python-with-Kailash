# Write a Python program to find the second largest number in a list


import sys
# sys.maxsize : represents the maximum integer value
# -sys.maxsize : represents the minimum integer value 

list = [ int(x) for x in input().split()]
lar1=lar2= - sys.maxsize
for x in list:
    if lar1<x:
        lar2=lar1
        lar1=x
    elif lar2<x and lar1>x:
        lar2=x

print( f"second largest number is {lar2}" ) # 1 2 45 67 98 09 87



# Write a Python program to find the second smallest number in a list. 

sm1=sm2=sys.maxsize

for x in list :
    if sm1>x:
        sm2=sm1
        sm1=x
    elif sm2>x and sm1<x:
        sm2=x

print( f"second smallest number is {sm2}")