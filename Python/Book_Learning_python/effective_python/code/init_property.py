# @property can also be added to constructor args.

class Register(object):
    def __init__(self, arg):
        self.arg = arg

class BoundedResistance(Register):
    def __init__(self, arg):
        super().__init__(arg)
        # or self.arg = arg
        # will also execute @arg.setter() from BoundedResistance cls

    @property
    def arg(self):
        return self._arg

    @arg.setter
    def arg(self, new):
        if new <= 0:
            raise ValueError('{} must be greater than 0'.format(new))
        self._arg = new


r1 = BoundedResistance(10)

print(r1.__dict__)
print(hasattr(r1, 'arg'))
print(r1.arg, r1._arg, r1.arg == r1._arg)

r3 = BoundedResistance(-5)
