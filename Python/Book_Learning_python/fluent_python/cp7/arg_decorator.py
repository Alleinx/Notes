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