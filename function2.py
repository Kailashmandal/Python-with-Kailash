def Odd_Even(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

print(
    Odd_Even(
     int(
        input("enter your number ")
     )
    )
)