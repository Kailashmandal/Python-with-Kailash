def decorator_function( any_function ):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    
    return wrapper_function # new wrapper function with ehanced functionality is returned

@decorator_function
def func():
    print('this is func')

func() # this will works fine

# but function with argument func(a) will give error

# for that use *args and **kwargs and return the original function inside of wrapper function

def decorator_function_x( any_function ):
    def wrapper_function(*args , **kwargs):
        print('this is awesome function')
        return any_function(*args,**kwargs)
    
    return wrapper_function # new wrapper function with ehanced functionality is returned


@decorator_function_x
def func_add(a,b):
    return a+b

# now if we call the func_add()
print(
    func_add(88,12)
)
