# Closure is different from anonymous function
# take avg() as an example: 
# avg(number): takes a number and return the average value from all historical input.

# Class implementation
class Averager():
    def __init__(self):
        self._series = []
    
    def __call__(self, new_value):
        self._series.append(new_value)
        total = sum(self._series)
        return total / len(self._series)

# usage:
avg = Averager()
print('first invoke:', avg(10), 'second invoke:', avg(12))

# ------------------------------------------
# Functional implementation(Closure)
def make_averager():
    series = []

    def averager(new_value):
        # series variable is a 'free variable', it will be stored in the co_freevars of __code__
        # of function averager.
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager

# Usage:
avg = make_averager()
print('first invoke:', avg(10), 'second invoke:', avg(12))
print('varables inside free varable scope:', avg.__code__.co_freevars,
        ';normal variables of function averager():', avg.__code__.co_varnames)
print('variables inside make_averager():', make_averager.__code__.co_varnames)