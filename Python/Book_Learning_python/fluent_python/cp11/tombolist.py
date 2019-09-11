# This program demonstrates how to regist a class as the virtual subclass of abc.
# virtual subclass will not extend any method/attribute from abc.
from random import randrange

from tombola import Tombola

@Tombola.register
class Tombolist(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('Pop from empty TomboList.')
    
    # Tombolist.load = list.extend
    load = list.extend

    def loaded(self):
        return bool(self)
    
    def inspect(self):
        return tuple(sorted(self))
    
if __name__ == "__main__":
    print(issubclass(Tombolist, Tombola))
    t = Tombolist(i for i in range(10))
    print(isinstance(t, Tombola))