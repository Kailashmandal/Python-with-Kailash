#user input
# input function
# input function always takes input as string 
# convert input to number if required

# syntax is :    variable_to_store_the_input= input("message for user")

name=input("What is your name ?")
print("type is name is ",type(name))
print(name)


# int() function used to convert values to integer
# float() function used to convert values to string

num1= int(
    input("enter first number")
)

num2= int(
    input("enter second number")
)

total=num1+num2
print("Total of num1 and num2 is ",total)


float1= float(
    input("enter first decimal number")
)

float2 =float(
    input("enter sceond decimal numebr")
)

FloatSum=float1+float2
print(FloatSum)