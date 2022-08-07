# range(initial value , End value , step)

# we can add step argument to range function to jump accordingly we need

for i in range( 1, 11 , 2): # this will allocate alternate value to i
    print(f"The value of i is {i}") 

print("\nloop1 ened here ##########\n")

for i in range( 1 , 100 ,3):#we can also jump 3 or as many we want within the range
    print(f"The value of i is {i}")

print("\n loop2 end here \n")
##################################################

#if we are iterating over the string it will give character present at index without using indexing statement
for i in "Kailash":
    print(i) # this will print each character of the "Kailash"