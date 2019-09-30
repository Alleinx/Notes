import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
    
    sys.stdout.write = reverse_write
    # code above will be executed when __enter__ is called, or
    # at the begining of the with code block.
    msg = ''
    try:
        yield 'JABBERWOCKY'
    # code after yeild will be executed when __exit__ is called, or
    # at the end of the with code block.
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)

if __name__ == "__main__":
    with looking_glass() as what:
        print('Alice, Kitty and snowdrop')
        print(what)
    
    print(what)