#some general method to operate over the list
# count method is use to count the element present in the list

import numbers


fruits =['bnanana' , 'apple', 'orange','mango','pear']

count_apple= fruits.count('apple')
print(count_apple) #this will give 1

# sort method is used to sort the list acending order
numbers = [3,5,8,1,2,10,9,7]

numbers.sort() #this will sort the elements in original list

print(numbers)

#if we jsut want to print the sorted oreder of a list
#we can use the sorted fuction to just printing purpose
print( sorted( fruits)) #this will print fruits in sorted order


### clear method : makes a list empty(delete all the elements)
fruits.clear()

print(fruits) #fruits is empty now []

### copy method : is used to copy an entire list

numbers_copy = numbers.copy()
print(numbers_copy)