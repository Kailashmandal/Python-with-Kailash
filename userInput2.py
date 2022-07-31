#how to get two inputs using only one input function

#using split() function we can split the input on the bases of comma(,) and space (default)

#taking name and age as input
name , age = input("enter your age and name ").split()
print("name is " +name +" and age is "+age)