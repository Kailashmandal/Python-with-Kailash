# set is collection
# elements are unordered collection of unique items
# unordered-> no indexing
# unique -> no duplicate
s={1,2,3} # this is a set
print(s)

# set is often used to remove duplicate from list

l=[1,2,3,4,2,3,4]

#1. convert list into set 2.convert set into list

s=set(l) # this will remove all the duplicates elements
l=list(s) # converting set to list
print(l)


#adding an item to set
s.add(4)
s.add(5)
s.add(4) #this will not be added

print(s)

s.remove(4) # this will remove 4 

s.discard(5) # this will also remove 5

s1=s.copy() # this will copy the set into s1

s.clear() # used for clearing the set

print(s)