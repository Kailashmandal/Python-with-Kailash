# any all function

number1=[2,4,6,8]
number2=[1,3,5,4,6]

# all function return the true if all element of iteraor is true

list1=[ num%2==0 for num in number1]

print(
    all(list1 )
)

# any function return true if any one element is true

list2=[ num%2==0 for num in number2]

print(
    any(list2)
)


## checking input type before start adding in a sun function

def add(*args):
    if all((type(arg)==int or type(arg)== float) for arg in args):
        return sum(args)
    else:
        return "wrong input"

print(
    add(1,2,4.5,6.7,'some string')
)