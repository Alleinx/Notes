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
        for word in self.words:
            yield word
        # Generator registor(Factory method) won't raise StopIteration Exception.

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