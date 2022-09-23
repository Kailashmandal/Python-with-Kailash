# Write a Python program to get the maximum and
#  minimum value in a dictionary.

def get_min_max_value(dic):
    dic1={}
    dic1=dic.copy()
    min1= min(dic1.values())
    max1= max(dic1.values())
    return min1,max1

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic3.update(dic2)
print('dic3 is',dic3)
print(
    f'min , max value in dic3 are :',get_min_max_value(dic3)
)


# Write a Python program to remove 
# duplicates from Dictionary.

dic={
    1:10, 
    2:20 ,
    3:30, 
    4:40 , 
    5:50,
    6:60 ,
    1:10, 
    2:20 ,
    3:30
}

result={}

for key,value in dic.items():
    if key not in result:
        result[key]=value

print('\ndictionary without duplicates : ')
print( result )