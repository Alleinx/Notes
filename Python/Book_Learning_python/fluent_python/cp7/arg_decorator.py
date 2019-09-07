# This program demonstrate how to pass other parameters to the decorator
# Create a factory method, pass the parameters to the factory method, and let 
# the factory method returns a new decorator.
# factory method is not a decorator, but is used to return a decorator.

registry = set()
# This is a factory method
def register_func(active=True):
    # This is the real decorator
    def decorate(func):
        print('running register(active=%s) -> decorate(%s)'
                % (active, func))
        if active:
            registry.add(func)
            print(func, 'is successfully registered.')
        else:
            registry.discard(func)
            print(func, 'is not registered.')
            
        return func
    
    return decorate

@register_func(active=False)
# Must use as a function
# So the order of execution is:
# 1st call register_funct(active=False), which will return decorate
# 2nd @decorate -> f1 = decorate(f1), which will print msg "xxx is not registered"
# 3rd f1() -> func(), which is f1(), which will print msg "running f1()"
def f1():
    print('running f1()')

@register_func()
def f2():
    print('runing f2()')

def f3():
    print('running f3()')

print('running main()')
print('registry ->', registry)

f1()
f2()
#------------------------------------------------------------------
# The following function test the property of 'free variable'
print('\n\n\n\n')

def test(other_args=False):
    print('running test()')
    
    def decorator(func):
        print('running decorator()', other_args)
        def operation_function(*args):
            print('Running operation function', other_args)
            print('args passed to operation_function(): ', args)
            func(*args)
            # Need to use *args to pass variable positional parameters to other function.

        return operation_function

    return decorator

@test()
def d1(*args):
    print('running f1()')
    print(args)
d1(123, 321, 123123123, 5235234)
# d1(123, 321, 123123, 123123, ...) will also works if d1() doesn't take any variable positional parameters.
print(test().__code__.co_freevars)
print(d1.__code__.co_freevars)