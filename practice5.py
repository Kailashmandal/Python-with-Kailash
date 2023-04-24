# function to check the given string is palindrome

def is_palindrome( str):
    rev=str[::-1]
    if rev in str:
        print("palindrome")
    else:
        print("not palindrome")

is_palindrome(
    input("enter the string ")
)