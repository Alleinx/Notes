import itertools
import functools

# Inorder traverse of a tree.
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x
        
        yield t.lable

        for x in inorder(t.right):
            yield x

def upper(s):
    return s.upper()

print(list(map(upper, ['sentense', 'fragment'])))


def is_even(x):
    return (x % 2) == 0

print(list(filter(is_even, range(10))))


# usually used to mark the index of required elements
for item in enumerate(['subject', 'verb', 'object']):
    print(item)

try:
    with open('some_file') as f_obj:
        for i, line in enumerate(f_obj):
            if line.strip() == '':
                print('Blank line at line #{number}'.format(number = i))

except FileNotFoundError as e:
    print('No such file.')

for i in zip([1,2,3], (4,5,6,7)):
    print(i)
#---------------------------------------
# Usage of itertools module:

print('Permutation:')
for i in itertools.permutations((1,2,3), 2):
    print(i)

print('Combination:')
for i in itertools.combinations((3,4,5),2):
    print(i)

#---------------------------------------
# Usage of functools module:
def log(message, subsystem):
    """Write the contents of 'message' to the specified subsystem."""
    print('{0}: {1}'.format(subsystem, message))
    
server_log = functools.partial(log, subsystem='server')
server_log('Unable to open socket.')