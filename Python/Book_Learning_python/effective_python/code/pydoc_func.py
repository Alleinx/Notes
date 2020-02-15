# This program demonstrate one of the ways to overload a function
# or implementation functions in python-doc format.
# like dict(), dict(Mapping, **kws), dict(Iterable, **kws)

import collections.abc


def user_dict(*args, **kw):
    '''
    user_dict() -> {}
    user_dict(Mapping, **kw) -> {k: v}
    user_dict(arg1, *args) -> {v:default}
    '''
    total_args = len(args)

    if total_args == 0:
        return {}

    result = {}

    if isinstance(args[0], collections.abc.Mapping):
        print('Mapping')
        if total_args > 1:
            raise TypeError(
                'user_dict() takes 1 positional argsument, but got {}.'.format(total_args))
        for k, v in args[0].items():
            result[k] = v
        for k, v in kw.items():
            result[k] = v
        return result
    else:
        for item in args:
            result.setdefault(item, 'null')
        return result


if __name__ == '__main__':
    a = {'a': 1, 'c': 4}
    print('a isinstance of collections.abc.Mapping:',
          isinstance(a, collections.abc.Mapping))

    b = user_dict(a, c=2, d=10)
    print('Testing user_dict(Mapping, **kw):', b)

    c = user_dict()
    print('Testing user_dict():', c)

    d = user_dict(3, 2, 4, 5)
    print('Testing user_dict(arg1, **args):', d)

    # Should Raise a TypeError
    # e = user_dict(3,2,[])

    # Test mix using Mapping and arg.
    # Should raise a TypeError.
    # c = user_dict(a, 1)
