# Decorators - enhance the functionality of the other functions

def func1():
    print('this is function 1')


def func2():
    print('this is function 2')


# we want to print extra line ' this is awesome function' when func2() is called


func1() , func2()

# defining the decorator( that decorates the functionality of other function)
# @  use for decorators

def decorator_function( any_function ):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    
    return wrapper_function # new wrapper function with ehanced functionality is returned


# we can asigning the decorators functionality to same fucntion
func2= decorator_function( func2 )

func1() , func2()

# OR we can use syntax suger '@' symbol
# use '@' symbol for enhacement of functionality while defining the function using decorators
@decorator_function
def func3():
    print('this is function 3')

# now if func3() is called it will act accordily decorator function
func3()
