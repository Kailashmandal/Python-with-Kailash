# Write a Python program to calculate 
# the sum and average of n integer numbers
#  (input from the user). Input 0 to finish. 

# n= int(
#     input("enter the number ")
# )
# sum=0
# avg=0
# for i in range(0,n+1 ):
#      sum+= i

# avg = sum / n 
# print(f"sum is {sum} and avg is {avg}")

################# Write a Python program to reverse a string

def reverse_str( str ):
    str = str[::-1]
    return str

str = input("enter the string : ")
str= reverse_str(str)
print("reverse string is : "+str)