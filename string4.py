name ="MacHine lEaRning"

#len(string_variable) function is used to get the length of the string
print('Length of the name : ', len(name))

# lower() method is used to convert  a string into lower alphabets string

name_in_lower_characters = name.lower()

print(name_in_lower_characters)

# upper() method is used to get the dtring in capital alphabets
name_in_capital_characters= name.upper()

print(name_in_capital_characters)

# title() method convert any string to title : first letter capital and others small
title = name.title() # MacHine lEaRning --> Machine Learning

print(title) 

# count() method is used to count the occurence of  character that we want to count
print("occurence of 'a' is : " ,name.count("a"))
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



