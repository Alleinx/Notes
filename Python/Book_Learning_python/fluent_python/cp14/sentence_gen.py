# This program implements a generator.
import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()
        # return (match.group() for match in RE_WORD.finditer(self.text))
        
        # Generator registor(Factory method) won't raise StopIteration Exception.
        # Using Lazy Implementation:
        # Unlike re.findall() (will return a list), re.finditer() will return a generator
        # which will save a lot of memory.

if __name__ == "__main__":
    def gen_AB():
        print('start')
        yield 'A'
        print('continue')
        yield 'B'
        print('end')

    for c in gen_AB():
        print('-->', c)
    
       
    s = Sentence('"The time has come," the Walrus said,')

    for word in s:
        print(word)