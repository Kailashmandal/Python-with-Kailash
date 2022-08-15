# how to join two lists
# using + operator as concatenate

fruit1=['apple' , 'orange']
fruit2=['grapes','mango']

#combining both lists
fruit = fruit1+fruit2 # we will get a new list

print(fruit)

# if we have to join the 2nd list in 1st list without
# creating an extra list variable.
# we can use extend method

fruit1.extend(fruit2)

print("fruit1 is "+str(fruit1))

# but in the case of append method fruit2 is get a place by whole elemnt
# e.g. ['apple' , 'orange' , ['grapes','mango']]

fruit1.append(fruit2)

print(f'fruit1 is now {fruit1}')
# Output:
# ['apple' , 'orange', 'grapes','mango', ['grapes','mango']]

###### Data deletion method of the list

# pop( index ) method delete the index element of the list
# if we don't provide any argument it deletes last element of the list

#for example
fruit1.pop()

print(f'fruit1 is now {fruit1}')

#Output:
# ['apple' , 'orange', 'grapes','mango']

# if we provide argumrnt it deletes the specfied element
fruit1.pop(1) # orange will be deleted

# fruit1.pop(500) this will give index of range error
print(f'fruit1 is now {fruit1}')

#Output:
# ['apple' , 'grapes','mango']

fruit1.insert(1,'orange')


### del operator : deletes the specified index element

del fruit1[0] # this will delete the apple from list
print(f'fruit1 is now {fruit1}')

#Output:
# ['orange', 'grapes','mango']

### remove(element name ) :is used to remove 1st element when we don't
# know the position of the element inside the element

fruit1.remove('orange') # this will remove 1st orange element
#if srgument provided doesn't exist in the list
# element not exist error is thrown

fruit = ['apple' , 'apple' , 'oarnge' , 'pear']
# if there exist multiple ele with same name 1st element with 
# given name is deleted with remove method

fruit.remove('apple')
print(f'fruit is {fruit}')

### in keyword : used to find whether an element id present the list or not

is_apple_present = 'apple' in fruit
# if true then apple exist else apple not exist
print(is_apple_present)

if 'pear' in fruit:
    print('Pear is present')
else:
    print("pear doesn't exist")
