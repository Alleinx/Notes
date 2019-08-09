# This program test the order of name look up.
# 1. instance.attribute
# 2. instance.super.attribute
# 3. class attribute

class C():
    def __init__(self, i):
        self.i = i

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        else:
            return self.i

    def __set__(self, obj, value):
        self.i = value

class A():
    def __init__(self, i):
        self.i = i

class B(A):
    # Third
    i = C('test')

    def __init__(self, i):
        # Second
        super().__init__(i)
        # First
        self.i = 100

if __name__ == "__main__":
    b = B(10)
    print(b.i)