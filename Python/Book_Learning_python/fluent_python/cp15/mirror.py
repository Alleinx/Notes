# This program demonstrate how the Context Manager works in python.
# The Context Manager collaborates with 'with' code block.
# __enter__() method will be invoked by 'with' when 'with' begin to run.
# __exit__() method will be invoked by 'with' when 'with' finishs executing.
# so the object after 'with' need to implements both __enter__, and __exit__ method.

class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'
    
    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please do not divide by zero!')
            return True
    

if __name__ == "__main__":
    with LookingGlass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)
    
    print(what)
    print('Back to Normal')

    # Which is equivlant to:
    context_manager = LookingGlass()
    temp = context_manager.__enter__()
    what = temp

    print('Alice, Kitty and Snowdrop')
    print(what)

    context_manager.__exit__(None, None, None)

    print(what)
    print('Back to normal.')
