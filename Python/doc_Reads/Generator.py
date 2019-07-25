# Will automatically implement __iter__() and __next__()
# Will automatically raise StopIteration Exception and store index information.
# Return data using 'yield' statement.

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

if __name__ == "__main__":
    for char in reverse('golf'):
        print(char, end = ' ')
    
    print()