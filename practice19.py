# Write a Python script to concatenate following
#  dictionaries to create a new one
#Sample Dictionary :
from turtle import update


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

# Expected Result :
#  {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic={}
## iterating over three dictionary and updating 
# the key value pair in the required dic 
for x in (dic1,dic2,dic3):dic.update(x)
print(dic)

# Write a Python script to check whether a given 
# key already exists in a dictionary.
if 7 in dic:
    print("7 exist")
else:
    print("7 not exist")


# Write a Python program to
# iterate over dictionaries using for loops.

for key in dic:
    print(f"{key}:{dic[key]}")

#OR iterating over the values only
for value in dic.values():
    print(value)
