# This program demonstrates how to override Unary operator:
import math

class Vector2d:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __abs__(self):
        return math.sqrt(sum((self.x ** 2, self.y ** 2)))

    def __neg__(self):
        """
        Override Unary '-'
        """
        return Vector2d(-self.x, -self.y)
    
    def __pos__(self):
        """
        Override Unary '+'
        """
        return Vector2d(self.x, self.y)

    def __repr__(self):
        return 'Vector (%.2f, %.2f)' % (self.x, self.y)

if __name__ == "__main__":
    a = Vector2d(4, 3)
    print(a)
    print(abs(a))
    
    b = -a
    print(b)
    print(abs(b))

    c = +b
    print(c)
    print(abs(c))