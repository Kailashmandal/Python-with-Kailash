# Write a Python script to print a dictionary
#  where the keys are numbers between 1 and 15 
# (both included) and the values are square of keys.

from ast import Delete


def dict_gen():
    dic={}
    for i in range(1,16):
        dic[i]=i*i
    return dic

print(
    dict_gen()
)

# Write a Python script to merge two Python dictionaries
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print("dict1 is now ",dic1)
dic1.update(dic2)
print('after updating/merging ')
print(dic1)


# Write a Python program to iterate over dictionaries using for loops.
for key,value in dic1.items():
    print(f'{key}:{value}')

# Write a Python program to remove a key from a dictionary.
dic1.pop(1)
print(dic1)

# Write a Python program to map two lists into a dictionary

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

dic=dict(
    zip(keys,values)
)

print(dic)