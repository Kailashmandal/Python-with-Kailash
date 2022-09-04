## returning two values for the functions

# any function returning two or more value will
#  return a tuple not two different values
def func(num1,num2):
    add=num1+num2
    mul=num1*num2
    sub=num1-num2
    return add,sub,mul

print( func(20,5))

# we can unpack this tuple into three different variables
sum,sub,mul= func(20,5)

print(sum,sub,mul)
