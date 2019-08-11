def lazy_import(*some_arg):
    import sys
    print('Avoid "cicular import" problem, delay the import process',
    'of the lower level module. However, it\'s better to rearrange the module level.')
    print(sys.version)

# func obj feature: memory/cache
def expensive(arg1, arg2, *, _cache={}):
    """Callers can only provide two parameters and optionally pass _cache by keyword"""
    if (arg1, arg2) in _cache:
        return _cache[(arg1, arg2)]

    # calculate the value
    # result = expensive computation...
    # and store result in the cache
    #_cache[(arg1, arg2)] = result
    # return result

# passing optional parameter and keyword parameter from 1 func to another.
def f(*args, **kwargs):
    # passing to another function
    print(type(args))
    g(*args, **kwargs)
    
def g(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == "__main__":
    # lazy_import()
    f((1,2,3,4),5,6,7, key='map')
    
    