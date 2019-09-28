import itertools
import functools
import operator

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

print(list(itertools.accumulate(sample)))
print(list(itertools.accumulate(sample, max)))
print(list(itertools.accumulate(sample, operator.mul)))


# Concatenate all the result and form a generator.
print(list(
    itertools.chain(itertools.accumulate(sample),
                    itertools.accumulate(sample, operator.mul))
        )
    )


print(list(
        itertools.zip_longest(sample,
                            [i for i in range(5)],
                            fillvalue='-1')
        )
    )

for i, v in enumerate(range(7, 20), start=1):
    print(str(i) + ' : ' + str(v))


cartesian_product = itertools.product(sample, 'abc', repeat=1)
print(list(cartesian_product))

print(list(itertools.combinations(range(5), 2)))

print(list(itertools.permutations(range(5),)))

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)

for length, group in itertools.groupby(animals, key=len):
    print(length, '->', list(group))

# In reverse way:
animals.sort(key=len, reverse=True)

for length, group in itertools.groupby(animals, key=len):
    print(length, '->', list(group))

def test_yield_from(*iterables):
    for iter_obj in iterables:
        yield from iter_obj

s = 'ABC'
t = tuple(range(3))
print(list(test_yield_from(s,t)))

# calculate 6!:
print(functools.reduce(operator.mul, range(1,7)))