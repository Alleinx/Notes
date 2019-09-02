needles = {1, 2, 3, 4}
haystack = {5, 6, 2, 4}
print(needles ^ haystack)
print(len(needles & haystack))

list_comprehension = {i for i in range(100)}
print(type(list_comprehension), list_comprehension)

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

dict_comprehension = {k:v for k, v in codes}
print(dict_comprehension)