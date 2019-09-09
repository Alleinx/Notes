from array import array
import reprlib
import numbers
import math
import functools
import operator
import itertools

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)
        # Check what's inside self.
        for x in self:
            print(x)

        print(self, self._components)
    
    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        componets = reprlib.repr(self._components)
        componets = componets[componets.find('['):-1]
        return 'Vector({})'.format(componets)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                    bytes(self._components))

    def __eq__(self, other):
        return (len(self) == len(other) and
                    all(a == b for a, b in zip(self, other)))
    
    def __hash__(self):
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))
    
    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{.__name__} indices must be integers.'
            raise TypeError(msg.format(cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos and pos < len(self._components):
                return self._components[pos]
        
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1 and (self[-1] < 0)):
            return math.pi * 2 - a
        else:
            return a
        
    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[: -1]
            coords = itertools.chain([abs(self), self.angles()])
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'

        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
    
