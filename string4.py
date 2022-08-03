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