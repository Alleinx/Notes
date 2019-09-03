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