#  row strings can be defined using r"our string"

str= r"hey kailash" 
# and no escape sequence will work in row string
print(str)

str=r"kailash \n hey" # with \n and r

print(str)

str1 = r"kailash \" hey'" # row string
print(str1)


str ="hye \n kailash" #without r not a row string 
print(str)

