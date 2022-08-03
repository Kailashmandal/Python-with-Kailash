# Write a Python program to calculate the length of a string.

str = input("enter your string :")

str_len = len(str)

print("lenght of string is ",str_len)


# Write a Python program to count the number of 
# characters (character frequency) in a string

char = input('enter the char ')

count = str.count(char)
print(f"The occurence of {char} is {count}")


# Write a Python program to get a string made of 
# the first 2 and the last 2 chars from a given 
# a string. If the string length is less than 2,
# return instead of the empty string.

str1= "W3resource"

start = str1[:2]
end=str1[-2:]
req_str =start+end

print(req_str)


# Write a Python program to get a string from a given string where all occurrences of its first char 
# have been changed to '$', except the first char itself.

str2 = "restartrrrr"

char=str2[0] # store the first char

str2 =str2.replace(char,"$" ,len(str2)) # replace all char present in str2 with '$'

print(
    # now replace first '$' with char and print
    str2.replace("$" ,char, 1)
)
