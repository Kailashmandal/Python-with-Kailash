# how to add data to lists

fruits=[ 'grapes' , 'apple']

fruits.append( 'mango') 
# append method is used to append a value to list
fruits.append('Bnanana')

print( fruits )

###### insert( index , value) method used to insert avlaue a specific position

fruits1=['grapes' , 'apple' ] 
fruits1.insert( 1,'mango') # this will insert mango at 1 in the palce of apple
# and other value get displace by 1 index position

print(fruits1)

fruits1.insert( 4 , 'lemon')#if we provide index greater then the list length 
# value provided will get the last position in the list

print( fruits1 )