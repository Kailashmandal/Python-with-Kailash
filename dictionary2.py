print(type({})) # <class 'dict'>

user_info={
    "name":"kailash",
    "age":22,
    "fav_songs":["song1","song2"]
    
}

# adding new key value pair
user_info['height']=177

print(user_info)


# deleting a key value pair
# pop(key) delete a key-value pair from list and return the value 
height=user_info.pop('height')
print(height)
print(user_info)

## popitem() method randomly remove the item from the dictionary
item=user_info.popitem()
print(user_info)
print(item)