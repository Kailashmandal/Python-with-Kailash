# scope of variables

x=5 # global variable

def fun():
    x=7 # local variable
    return x


# print( fun() ) # this will return x=7
# print( x ) this will print x=5

# but if we want to use the global variable then
# we have to use the global variable in the function

def func():
    global x # for using the global variable
    x=7 # now this is global variable modification 
    return x


print( func()) # this will print 7
print( x ) # this will print 7
