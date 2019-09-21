import re
import reprlib

RE_WAORD = re.compile(r'\w+')

class Sentence:
    """
    This class is a classic iterable object
    which implements at least one of __iter__ and __getitem__(index).
    """

    def __init__(self, text):
        self.text = text
        self.words = RE_WAORD.findall(text)

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        """In a Iterable obj, __iter__ needs to return a new iterator"""

        return SentenceIterator(self.words)

class SentenceIterator:
    """
    This class is a classic Iterator:
    which need to implement __iter__ and __next__
    """
    def __init__(self, words):
        self.words = words
        self.index = 0
    
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()

        self.index += 1
        return word
    
    def __iter__(self):
        """
        In an Iterator, __iter__ needs to return a iterator, which is self.
        """
        return self

if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said,')
    print(s)


    for word in s:
        print(word)
    
    print(list(s))

    # Iterator must be reconstructed every time it's fully consumed
    a = iter(s)
    print('Iterator hasn\'t reach the end:')
    for word in a:
        print(word)
    
    # Nothing will happens here, cause Iterator has reached the end.
    print('Iterator has reach the end.')
    for word in a:
        print(word)
    
    # iter(s) will call s.__iter__, which will return a new iterator, so
    # these code will always works.
    print('New Iterator constructed:')
    for word in s:
        print(word)