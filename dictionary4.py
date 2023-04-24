# more about get method in dictionary
user={
    'name':"kailash",
    'age':22,
    'age':45
}

#get method is used to get the value from a key
print( user.get('name'))
# if the key is not present it will return the None
# bu we can overide of the None 

# FOR E.g.

print(
    user.get('key','Not found')
    # this will return the Not found key is not present
)

## if we have same key multiple times then the last ocurrence of the key got counted always
# FOR E.g. 'age' is present twice
user={
    'name':"kailash",
    'age':22,
    'age':45 # this value will be counted as key-value pair 
}

print( user.get('age'))


## excercise

def cube_finder(n):
    dic={}
    for i in range(1,n+1):
        dic[i]=i*i*i
    return dic


n= int(
    input("enter a number: ")
)
print( 
    cube_finder(n)
)



##excercise 2
# count alphbets in the strings

str="hdijiskahejnzjajbbsjbduiwhdjeuebbdh"

def alphabet_counter(s):
    dic={}
    for i in s:
        dic[i]=s.count(i)
    return dic

print(
    alphabet_counter(str)
)
