
# str = input(
#     "enter your string "
# )

# if len(str)== 3:
#     pass
# else:
#   if str[-3:]=="ing":
#     str=str +"ly"
#   else:
#     str=str+"ing"

# print(str)


# str1= "abc" 
# str2="xyz"

# str1char=str1[0]
# str2char=str2[0]

# temp1= str1.replace(str1[0],str2[0],1)
# temp2=str2.replace(str2[0],str1[0],1)

# str=temp1+" "+temp2
# print(f"the required string is : {str}")

str1 = 'The lyrics is not that poor!'

pos_of_not= str1.find("not")
pos_of_poor= str1.find("poor")

# if pos_of_not < pos_of_poor:
#     print(str1[:pos_of_not]+"good"+str1[pos_of_poor+4:])
# else:
#     print(str1)
                    # OR

# if  pos_of_not<pos_of_poor:
#     print(
#         str1.replace(
#             str1[pos_of_not:pos_of_poor+4] ,"good"
#         )
#     )
# else:
#     print(str1)

# nth_char=int(
#     input("enter the character position ")
# )

# str2 = 'The lyrics is poor!'

# print(
#     str2.replace(
#         str2[nth_char-1] , "",1
#     )
# )

str2 = 'The lyrics is poor!'
str2 = str2[len(str2)-1]+str2[1:-1]+str2[0]

print(f"string is : {str2}")

## program to remove all the odd number character
str2 = 'The lyrics is poor!'
result = ""
for i in range(len(str2)):
       if i % 2==0 :
        result=result+str2[i]
print(result)
