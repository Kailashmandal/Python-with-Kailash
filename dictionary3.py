from webbrowser import get


user_info ={}

##adding key value pair to the dictionary
user_info['name']='kailash'
user_info['fav_movies']=['3idiots','xmen','Infinty war']
user_info['age']=24
user_info[1]=30
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

# update function will update the new values into a dictionary by the another dictionary
user_info.update(dic1)
print(user_info)
## if new key conflict previous key value will be changed only


##fromkeys method : is used to create a dictionary

d={'name':'unknown','age':'unknown'} # all the keys 
# which can have the same value

dic=dict.fromkeys(['name','age','fav'],'unknown')
print(dic)

#fromkeys([list of keys/tuple of keys],value)
d1=dict.fromkeys(range(1,11),"first moon")
print(d1)


## get method : used to access the key of a dictionary
# if key not present it return 'None' means key not persent
print( 
    #dic.get(any key)
    d1.get(2)
)

if d1.get('name'):
    print('present')
else:
    print('not present')


## clear method : dic.clear() will make the dictionary empty
d1.clear()
print(d1) # will return an empty dictionary


## copy() : used to copy a dictionary and clears the current data
dic1=dic2.copy()
print(dic1)

## dic1= dic2 equating two dictionary will only creat
# one more reference for the same dictionary

dic7=dic1
print('dic7 is',dic7)

#poping one element from dic1
dic1.pop(4)

print('now dic7 is',dic7) #{3:30} is printed means they refer to same dictionary in memory
print(dic1 is dic7)



