# function takes two numbers returns greater number

def greater_number(a,b):
    return a if a>b else b


print(
    greater_number(
        int(
            input("enter first number ")
        )
        ,
        int(
            input("enter second number ")
        )
    )
)

def graeter_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

print(
    graeter_of_three(
        int(
            input("enter the 1st number ")
        ),
        int(
            input("enter the 2nd number ")
        ),
        int(
            input("enter the 3rd number ")
        )
    )
)



print(
    greater_number(
        greater_number(
            int(
                input("enter first number ")
            ),
            int(
                input("enter second number ")
            )
        )
        ,
        int(
            input("enter third number ")
        )
    )
)
