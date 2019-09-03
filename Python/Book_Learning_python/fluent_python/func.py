# functions in python are first-class object.
# 1. A first-class object is created during execution
# 2. A first-class object could be assigned to other object
# 3. A first-class object could be passed to a function as a parameter
# 4. A first-class object could be the return value of a functino.
def factorial(n):
    """
    Return n!
    """
    return 1 if n < 2 else n * factorial(n-1)

# demonstrate feature #2
fact = factorial
print(fact.__doc__)
print(type(factorial))
print(fact(5))

# demonstrate feature #3
maped_list = list(map(fact, range(10)))
print(maped_list)

# higher order function: A fucntion that takes other functions as parameter or returns function as its result.
fruits = [str(i) for i in range(3, 1000, 25)]
result = sorted(fruits, key=len)
# sorted() is a higher order function.
print(result)

# -------------------------
# Callable Object
# All object of python could be callable if it defines the __call__ method.
import random

class BingoCage:
    """
    This class demonstrate how to define a callable class instance
    """
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty Bingo Cage')
    
    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))
# Normal invokation of class method:
print(bingo.pick())
# Directly invoke the class instance, and python will call __call__() method of BingoCage
print(bingo())