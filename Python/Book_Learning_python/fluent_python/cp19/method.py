class A:
    def foo(self, x):
        print('Executing foo(%s, %s)' % (self, x))
    
    @classmethod
    # func signature: class_method(cls, arg1, arg2, ...)
    # the first arg is class.
    def class_foo(cls, x):
        print('Executing class_foo(%s, %s)' % (cls, x))

    @staticmethod
    def static_foo(x):
        print('Executing static_foo(%s)' % x)

class B(A):

    @classmethod
    def class_foo(cls, x):
        print('Executing B\'s class_foo')

        
    @staticmethod
    def static_foo(x):
        print('B static_foo(%s)' % x)


a = A()
a.foo(10)
A.class_foo(10)
A.static_foo(10)
B.class_foo(10)
B.static_foo(10)