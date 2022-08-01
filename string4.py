#indexing in string
language ="Python"

#P -> 0
#y -> 1
# and so on (indexing of characters starts with 0 from start)

print(language[1])


# indexing start with -1 from end 
# for example n -> -1 , o-> -2 end so on

print(language[-1])
#by using this we can print the last character of any string
#without knowing the string lenght.


#####################################################

# String Slicing : is used when we want to get a specific part of string

# Syntax :  var_name[start index : end index + 1] last character is inclusive
print(language[0:2]) # Py
print(language[0:]) # Python
print(language[:3]) # Pyt


#######################################################


# Step argument in Slicing of String
# Syntax :  var_name[start index : end index + 1 : position jump] last character is inclusive
print(
    "Kailash"[0::2] # here jump step is 2 Output : Kiah
)

print(
    "Kailash"[::-1] # here jump is 1 from the back: hsaliaK
)

print(
    "kailash"[-1::-1]
)



