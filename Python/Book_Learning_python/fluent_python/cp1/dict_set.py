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