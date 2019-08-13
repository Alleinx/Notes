import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs herts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                            for rank in self.ranks]

    # Invoked by interpreter when execute len(obj)
    def __len__(self):
        return len(self._cards)

    # Invoked by interpreter when execute obj[position]
    def __getitem__(self, position):
        return self._cards[position]

    # Invoked by interpreter when execute print(obj), if doesn't override __str__()
    # Otherwise, __str__() will be invoked.
    def __repr__(self):
        return str(self._cards)

    # Invoked by interpreter when execute iterator
    def __iter__(self):
        return iter(self._cards)
        # Or self._cards.__iter__()

if __name__ == "__main__":
    deck = FrenchDeck()
    print(deck)
    print(len(deck))
    
    for card in deck:
        print(card)