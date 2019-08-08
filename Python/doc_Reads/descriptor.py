class Car():
    def __init__(self, val):
        self.val = val

    def __get__(self, obj, type=None):
        print('Retrieving var')
        return self.val

    def __set__(self, obj, val):
        # Define Read-Only descriptor by raising AttributeError()
        # raise AttributeError('Read-Only Attribute')
        print('Updating var')
        if isinstance(val, int):
            self.val = val
        else:
            print('Error: val should be a integer.')
        

class MyClass():
    # This is a class attribute(shard accross all instance of the class).
    car_inventory = Car(100)
    
    def __init__(self):
        self.car_inventory = 'abc'

    # Note: Different from
        # def __init__(self):
        #     self.car_inventory = Car(100)


# The look-up priority of attribute changes for *data descriptor* and *non-data descriptor*

# delete the __set__() method to see the difference.
# for non-data D: self.attribute has higher priority.
# for data D: D obj has higher priority.

m1 = MyClass()
print(m1.car_inventory)

m1.car_inventory = 20
print(m1.car_inventory)
m1.car_inventory = 'test'

m2 = MyClass()
print(m2.car_inventory)

class C():
    def getx(self):
        return self.__x
    
    def setx(self, value):
        self.__x = value

    def delx(self):
        del self.__x

    x = property(getx, setx, delx, "'x' property.")

class Property():
    """Emulate PyProperty_Type() in Objects/descrobject.c"""

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

        if doc is None and fget is not None:
            doc = fget.__doc__
        self.doc = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        if self.fget is None:
            raise AttributeError("Unreadable Attribute")

        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("Can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribtue")
        self.fdel(obj)

    def getter(self, fget)
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__
    
    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


# The property() builtin helps whenever a user interface has granted attribute access 
# and then subsequent changes require the intervention of a method.
# E.g. Don't want to modify the existing code but want to add some extra
# behavior before/during accessing the attribute.

class Cell():
    def getvalue(self):
        """recalculate the cell before returning value"""
        self.recalc()
        return self._value

    value = property(getvalue)