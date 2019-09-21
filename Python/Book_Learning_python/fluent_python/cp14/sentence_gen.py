# This program implements a generator.
import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for word in self.words
            yield word

        # Generator won't raise StopIteration Excetpin,
        # but exit after generating all elements in the given list.
    
    