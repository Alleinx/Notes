import time
import functools

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    
    return clocked

@clock
# snooze will be stored in global scope of the program.
# clock(snooze)
def snooze(second):
    time.sleep(second)

@functools.lru_cache()
# lru_cache is a decorator that implements optimization mechanism.
# Execution Order for @decorator1 @decorator2 def func()
# func = decorator1(decorator2(func))
@clock
# factorial will be stored in global scope of the program.
# clock(factorial)
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == "__main__":
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(10)')
    factorial(10)