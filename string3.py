name = "kailash"
age =22
print("hello "+name+" your age is",age)
#this is regular printing

#we can {} as placeholder and format the string intoduced in python 3

print("hello {} your age is {}".format(name,age))
# {}--> name , {}-->age
#both {} will be replaced by the name and age variable.


#we can also format the string like this after python 3.6
print(f"hello {name} your age is {age}")
#this is like string literal in javascript


#we can manipulate also inside the print formate syntax
print(f"your age is {age + 2}")