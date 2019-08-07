class Car():
    def __init__(self, val):
        self.val = val

    def __get__(self, obj, type=None):
        print('Retrieving var')
        return self.val

    def __set__(self, obj, val):
        # Define Read-Only descriptor by raising AttributeError()
        print('Updating var')
        raise AttributeError('Read-only object.')

class MyClass():
    car_inventory = Car(100)


m = MyClass()
m.car_inventory
m.car_inventory = 20