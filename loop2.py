# n = int(
#     input("enter the value of n ")
# )
# sum =0
# i=1
# sum of first n natural numbers
# while i<=n :
#     sum += i
#     i +=1

# print("Sum is ", sum)

# n= input("enter the value of n ")

# len = len(n)
# sum=0
# i=0 
# while i < len :
#     sum += int(
#         n[i]
#     )
#     i+=1

# print(sum)

###############################################
# program to count the frequency of each character in string
name = input("enter your name ")

temp="" # create a temp var to store the unique characters
i=0 
while i < len(name):
    if name[i] not in temp: # caheck whether ith char is present in temp or not
        temp = temp + name[i] # if not present then add it in temp and print count
        print(
            #printing the count of the character
        f"count of {name[i]} is {name.count(name[i])}"
        )
    i+=1 # increase the value of i

################################
# break is used to break the loop when a condition is met

for i in range(11):
    if i==5:
        break # this will beak the loop
    print(i)

for i in range(11):
    if i==5:
        continue # means nothing will be executed
    print(i) # 5 will not be printed
    


    
