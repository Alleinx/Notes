# To let some class to behave like sequence, we don't need to let the class
# be the subclass of any specific class(like java), but only need to implement
# some necessary method
# For example, to let a class behave like a sequence, the class need to implement
# __len__ and __getitem__ methods. After that, it could be used as a sequence.
# Actually, it's the same as java.
import collections 

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.__cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, position):
        return self.__cards[position]

if __name__ == "__main__":
    deck = FrenchDeck()
    for i in range(len(deck)):
        print(deck[i])
        
    for card in deck[::2]:
        print(card)