# how to compare two list
# == , is 

fruits1=['orange' , 'apple' , 'pear']
fruits2=['banana','kiwi','apple']
fruits3=['orange' , 'apple' , 'pear']

# == checks wether the values are same or not

print( fruits1==fruits3 ) # True because elements of the fruits1 and fruits3 are same

# is used to check wether the objects are sam eor not

print( fruits1 is fruits3) # fruits1 and fruits3 are different obejcts so false


### split() method : converts the string into list by a breaking character

#for e.g.

list_str= 'k a i l a s h'.split()

print( list_str)
#we can also store the differnet values in different variables

name,age='kailash 22'.split()
print( name , age)

### join() method : is used to join the different ele of string list
## means join method convert a list into string
list=['ka','il','as','h']
str= ' '.join(list)
# for joining we can also use 'space' , 'comma' etc. as well

print(str)

str2=",".join(['k','a','i','l','a','s','h'])
print(str2)