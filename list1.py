# lists --> data structur
# lists can store any type of value float ,int, string , boolean , another list etc

number = [ 1,2,3,4,5 ] # this is an easy example of list

print( number ) # this will print our list

words = [ 'kailash' ,'python' ,"UiPath" , "RPA"]

print( words )


# we can access the elements of the list by using indexing from the 0th index

print (
    number[1] # thsi print element prsent at 1st index
)

# we can also slices using [start index , end indx+1 ] like in string

print(
    words[ 0: 3 ]
)

#OR

print(
    words[-1 :-4 : -1] # we can also use step argument here 
)

#OR
print(
    words[::-1] # this will reverse the list
)

## list are muatable can value of any elemt can be changed

number[1]=10

print(
    number # 1st index is updated now
)

#OR

words[1:]=[]
print( 
    words # from index 1 to end is cleared now
)
