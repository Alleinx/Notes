import re
import reprlib

RE_WAORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WAORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    

if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said,')

    print(s)

    for word in s:
        print(word)
    
    print(list(s))
