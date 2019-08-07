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

m2 = MyClass()
print(m2.car_inventory)