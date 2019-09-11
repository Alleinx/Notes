# This program demonstrates some problem of extend builtin classes

class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


# If we want to extend some of the builtin classes, should extend classes in collections module.
import collections

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

if __name__ == "__main__":
    dd = DoppelDict(one = 1)
    # __init__ method of dict ignores our __setitem__ method.
    print(dd)

    dd['two'] = 1
    print(dd)
    
    dd.update(three = 3)
    # update method also ignores our __setitem__ method.
    print(dd)

# ---------------------------------
# DoppelDict2 Won't have the same problem as DoppelDict.
    dd2 = DoppelDict2(one=1)
    print(dd2)

    dd2['two'] = 1
    print(dd2)

    dd2.update(three = 3)
    print(dd2)