import random

from tombola import Tombola

class BingoCage(Tombola):

    def __init__(self, items):
        # self._randomizer = random.SystemRandom()
        self._item = []
        self.load(items)

    def load(self, items):
        self._item.extend(items)
        # self._randomizer.shuffle(self._item)
        random.shuffle(self._item)

    def pick(self):
        try:
            return self._items.pop()
        except:
            raise LookupError('pick from empty BingoCage.')
    
    def __call__(self):
        self.pick()

