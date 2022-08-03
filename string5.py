
from turtle import st


name = "      OpenCV    "
dots ='..................'

print(name+dots)

# lstrip : clears the left space of the string

print(name.lstrip()+dots)


# rstrip : clears the right spaces of the string

print(name.rstrip()+dots)


##### strip() : clears the both sides spaces
print(name.strip()+dots)

str= "O P     EN     CV    "
##### replace("what we wnat to replace" , "replacement value" , how many replacement we want in numbers eg-1-2-3) method
print(str.replace(" " , ""))

str="she is beautiful and she is good dancer"
print(str.replace(" ","_"))

# find("string we want to find" , start poistion , end position) method is used to find the chacters and substring  starting position

print(str.find("is"))

is_pos1 = str.find("is")

is_pos2 = str.find("is" , is_pos1+1) 
print(is_pos2)

