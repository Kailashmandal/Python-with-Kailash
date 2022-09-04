# tuples are data sturcture 
# tuples can store any type of data 
# most important thing tuples are immutable , once a touple is created you can't update it.
# data inside tuple 

example=('one','two','three')
ex=[1,2,3]
# no append , no insert, no pop , no delete/remove
# touple are used when we don't have change any data init
#touples are faster than lists performance

# methods:
# count , index
# len()
# slicing
print(example[0])
print(example[0:2])
print(ex[0:3])

## looping in tuple
num=(1,2,3,4,0,9)
for x in num:
    print(x)

# declaring tuple with one element 
tup=(1,) # insert comma after the first element

print( type(tup) )


## tuple without the paranthesis
guiters='one','two','three',

print( type(guiters) )

## tuple unpacking helps to store the element for tuple in different variables with exact number of variable required

num1,num2,num3=guiters #tuple unpacking 

print(num1,num2,num3+" = ",guiters)


## list inside the tuples
#we can add delete and modify the data inside the list
tup=('one' , [1,2,3,4])
tup[1].pop()

print(tup)

# min() max() sum() sorted() functions 
num=(1,2,3,4,0,9)

print( min(num))

print( max(num))

print(sum(num))

print(sorted(num)) # sorted() function will print the tuple in sorted order