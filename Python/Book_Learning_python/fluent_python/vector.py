from math import hypot

class Vector:
    """
    This class simulate the behavior of vector

    Operation:
    
    1. Addition:
        Vector(a, b) + Vector(c, d) = Vector(a+c, b+d).
    2. Multiplication:
        Vector(a, b) * scalar = Vector(a*scalar, b*scalar)
    3. Abs:
        abs(Vector(a, b)) = sqrt(a**2 + b**2)
    4. Description:
        User friendly vector representation.
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({x}, {y})'.format(x=self.x, y=self.y)

    # def __str__(self):
    #     return 'test'

    def __abs__(self):
        # hypot(x, y):
        # Return the Euclidean distance, sqrt(x*x + y*y).
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        try:
            x = self.x + other.x
            y = self.y + other.y
        except TypeError:
            print('Error: Inconsistant Type.')
        except Exception:
            print('An Error Occurs.')
        else:
            return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__ == "__main__":
    vecA = Vector(3, 4)
    vecB = Vector(5, 6)
    
    print(vecA)

    print(vecA + vecB)

    print(vecA * 10)

    print(abs(vecA))
