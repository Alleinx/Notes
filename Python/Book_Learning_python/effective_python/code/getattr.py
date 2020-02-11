# This program demonstrate:
# 1. The dynamic property of __getattr__(obj, name)
# 2. The usage of __getattribute__(obj, name)
# 3. The usage of __setattr__(obj, name, value)
# Note: Use super().__getattribute__(), super().__setattr__() in __getattribute__(), __setattr__() definition.

class LazyDB(object):
    def __init__(self):
        '''
        __getattr__() will be called if "name" is not in instance.__dict__
        '''

        self.exists = 5

    def __getattr__(self, name):
        if name == 'bad_name':
            raise AttributeError('Bad attribute name {}'.format(name))

        value = 'Value for {name}'.format(name=name)
        setattr(self, name, value)
        return value

class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        '''
        __getattribute__(name) will be called everytime we try to access some attributes, no matter whether they exist or not.
        '''

        print('Called __getattribute__({name})'.format(name=name))
        try:
            # Use super().__getattribute__() to avoid infinite recurrsion, since use getattr(self, name) or other way will also call __getattribute__.
            return super().__getattribute__(name)
        except AttributeError:
            if name == 'bad_name':
                raise AttributeError('Bad attribute name {}'.format(name))

            value = 'Value for {}'.format(name)
            setattr(self, name, value)
            return value

class SavingDB(object):
    def __setattr__(self, name, value):
        print('Called __setattr__({},{})'.format(name, value))

        # Use super().__setattr__() to avoid infinite recurrsion, since use setattr(self, name, value) or other way will also call __setattr__.
        super().__setattr__(name, value)

if __name__ == '__main__':
    print('-'*30)
    data = LazyDB()
    print('Before:', data.__dict__)
    print('foo:', data.foo)
    print('After:', data.__dict__)

    print('-'*30)
    data = ValidatingDB()
    print('exists:', data.exists)
    print('foo:'.ljust(10), data.foo)
    print('foo:'.ljust(10), data.foo)

    print('-'*30)
    data = SavingDB()
    print('Before:', data.__dict__)
    data.foo = 5
    print('After:', data.__dict__)
    data.foo = 7
    print('Finally:', data.__dict__)
