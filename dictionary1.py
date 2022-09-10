# dictionary are unordered collections of 
# data in key : value pair.


user ={ 'name': 'Harshit' , 
        'age':24
    }

#OR

user1= dict(name='kailash' , age=22)
print( type(user))

print('user1 is :',user1)

# acessing data from dictionary
# Note - There is no indexing because of unoredred collection of data

print(
    user['name'],user['age']
)

## creating an empty dictionary
user_info ={}

##adding key value pair to the dictionary
user_info['name']='kailash'
user_info['fav_movies']=['3idiots','xmen','Infinty war']
user_info['age']=24

print(user_info)


##we can store the dictionary inside the dictionary

users={
    'user1':{ },
    'user2':{ }
}


# check if key exist in dictionary
if 'name' in user_info:
    print('present')
else:
    print('not present')

# check if the value in dictionary
if 26 in user_info.values():
    print('present')
else:
    print('not prsent ')


## loops in dictionaries

## print all keys
for i in user_info:
    print(i)


## printing all values
for i in user_info.values():
    print(i)

# .values() method returns the values in dict_value type (like a list)
# but we can add  the data like list in dict_values type 

# .keys() method return all keys in dict_keys type (like a list )


### printing a ll values
print('printing all values ....')
for keys in user_info:
    print( user_info[keys])


## .items() method returns the all items present in 
# dictionary like list of tuples [(key1,value1) , (key2, value2) ,(key3,value3)]
# this is called dict_item type

## looping on  key and value both

for i in user_info.items():
    print(i)

## since i is tuple here we can unpack the tuple there
for key, value in user_info.items():
    print(f"{key}: {value}")

## key,value= (i) since i is tuple 