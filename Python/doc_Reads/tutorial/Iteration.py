class Reverse:
    """Iterator for looping over a sequence backwards"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        
        self.index -= 1
        return self.data[self.index]

if __name__ == "__main__":
    rev = Reverse('spam')
    
    # Iterator.
    # for will invoke the __iter__() of Reverse which will return a iterable object.
    # Then __next__() will be invoked until reach the end of the container(which is notified by a StopIteration Exception)
    for char in rev:
        print(char, end=' ')

    print() #EOF