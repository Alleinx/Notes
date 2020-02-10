# This program demonstrate the private field in python
# Use protected field instead of private field.

# Subclass can't directly access parent's private field.

class MyClass(object):
    def __init__(self, value):
        self.__value = value

    def get(self):
        return self.__value


obj = MyClass(10)
print(obj.__dict__)
print(obj.get())

obj._MyClass__value = 100
print(obj.get())
