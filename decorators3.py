from functools import wraps

def decorator_function_x( any_function ):

    @wraps(any_function)
    def wrapper_function(*args , **kwargs):
        """This is wrapper fucntion"""
        print('this is awesome function')
        return any_function(*args,**kwargs)
    
    return wrapper_function # new wrapper function with ehanced functionality is returned


@decorator_function_x
def func_add(a,b):
    """This is add function"""
    return a+b

# now if we call the func_add()
print(
    func_add(88,12)
)


print(func_add.__doc__)
print(func_add.__name__)