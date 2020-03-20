# This program is a demonstration of how to use builtin decorators
# Should use functools.wraps(func) to customize your own decorators, since use
# self-defined wrapper could cause problems when use debuggers and object serializers.
import functools

def demo_decorator(func):
    @functools.wraps(func)
    def wrapper(*arg, **kws):
        print('Currently in wrapper()')
        print('Decorating func name:', func.__name__)
        print('Decorating func arguments:', arg, kws)
        # you can add extra behavior before calling the function.
        result = func(*arg, **kws)
        # you can add extra behavior after calling the function.
        return result

    return wrapper

@demo_decorator
def test(arg1, arg2, *, name=None):
    print('Currently in calling function test()')
    print(f'Args in test(): {arg1}, {arg2}, {name}')

if __name__ == '__main__':
    test(10, 20, name='Y')
