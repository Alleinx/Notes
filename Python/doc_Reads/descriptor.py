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
        self.val = val

class MyClass():
    # This is a class attribute(shard accross all instance of the class).
    car_inventory = Car(100)

    # Note: Different from
        # def __init__(self):
        #     self.car_inventory = Car(100)


m1 = MyClass()
print(m1.car_inventory)

m1.car_inventory = 20
print(m1.car_inventory)

m2 = MyClass()
print(m2.car_inventory)