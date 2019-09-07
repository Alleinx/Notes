# This program demonstrate the difference between shallow copy and deep copy
import copy

class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
            # Defensive programming style, won't modify the original object if it's mutable.
    
    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        if name in self.passengers:
            self.passengers.remove(name)
        else:
            print(name, 'is not in the passenger list of the bus.')

bus1 = Bus(['A', 'B', 'C'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))

bus1.drop('B')
print(bus2.passengers, ',', bus3.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))

bus1.drop('D')