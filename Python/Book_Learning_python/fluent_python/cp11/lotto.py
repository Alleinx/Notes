import random

from tombola import Tombola

class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)
        # duck typing here.

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            result = self._balls.pop()
        except IndexError:
            raise LookupError('pick from empty LotteryBlower')
        
        return result

    # override super's methods
    def loaded(self):
        return bool(self._balls)
        # return False if list is empty, otherwise, return True.
    
    def inspect(self):
        return tuple(sorted(self._balls))
    
    
    