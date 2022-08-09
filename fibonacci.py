# fibonacci series - 0,1,1,2,3,5,8,13,21,34...

#take the input from user how many number we want ?
#use print( vaue , end=" ") for format printing with end

def fibonacci(num):
    if num==1:
        print("0")
    elif num==2:
        print("0 , 1")
    else:
        f1=0
        f2=1
        print(f1)
        print(f2)
        for i in range(1,num-1):
            f3=f1+f2
            print(f3)
            f1=f2
            f2=f3

fibonacci(
    int(
        input("enter the fibonacci range ")
    )
)
