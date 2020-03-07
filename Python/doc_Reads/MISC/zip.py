# Implementation of zip functions in python

def zip(*iterables):
    sentinel = object()
    iterators = [iter(it) for it in iterables]

    while iterators:
        result = []
        for it in iterators:
            item = next(it, sentinel)
            if item is sentinel:
            # if one of the iterator is exhausted.
                return
            result.append(item)
        yield tuple(result)
