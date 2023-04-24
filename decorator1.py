# pass function as arguments

#defining normal function 
def sq(a):
    return a*a

# a list
l=[1,2,3,4,5]

## defining a function that can take function as argument
def my_map(func, it):
    return [func(item) for item in it]

print(
my_map(sq,l)
)

# we can also use lmbda exp
print(
    my_map(
        lambda a:a**2,l
    )
)

# we can also use default map function
print(
    list( map(lambda a:a**2,l) )
)



## inner function and outer functions
## Closure or First class function
## Returning a function from a function

def outer_function():
    def inner_function():
        print('inside inner function')

    return inner_function

# getting inner function into the var_func variable
var_func= outer_function() 

#using var_func as function
var_func()


def outer_func(list):
    def inner_func():
        print(f'the list is {list}')
    
    return inner_func

var_inn=outer_func(l)
var_inn()


