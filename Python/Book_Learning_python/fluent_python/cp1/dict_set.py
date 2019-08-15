a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
assert a == b == c

# Dictcomp
codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'US'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
]

country_code = {country: code for country, code in codes}
print(country_code)
reversed_country_code = {code: country for country, code in country_code.items()}
print(reversed_country_code)

# Missing keys
dd = {1: 'test'}
print(dd.get(2, 'No such key exists in the dict.'))
print(dd)

print(dd.setdefault(1, 'Added by setdefault'))
dd.setdefault(3, 'Added by setdefault')
print(dd)

class StrKeyDict(dict):
    """
    A dict with str key, and could get/set value using str/int key.
    """

    def __missing__(self, key):
        """
        __missing__ will be invoked when __getitem__ doesn't find given key.

        """
        if isinstance(key, str):
            raise KeyError(key)
        
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
            # Pass the duty to __getitem__ so that __missing__ could be invoked.
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict({'2': 'two', '4': 'four'})
print(d['2'], d[4])

# print(d[1]): KeyError Exception

print(d.get('2'), d.get(4), d.get(1, 'N/A'), sep=', ')

a, b = (2 in d, 1 in d)
print(a, b, sep=', ')