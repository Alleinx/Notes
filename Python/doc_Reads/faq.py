def lazy_import(*some_arg):
    import sys
    print('Avoid "cicular import" problem, delay the import process',
    'of the lower level module. However, it\'s better to rearrange the module level.')
    print(sys.version)

if __name__ == "__main__":
    lazy_import()


def expensive(arg1, arg2, *, _cache={}):
    """Callers can only provide two parameters and optionally pass _cache by keyword"""
    if (arg1, arg2) in _cache:
        return _cache[(arg1, arg2)]

    # calculate the value
    # result = expensive computation...
    # and store result in the cache
    #_cache[(arg1, arg2)] = result
    # return result