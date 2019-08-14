import operator
# Cartesian Product
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
                            for size in sizes]
# or 
# tshirts = [(color, size) for size in sizes
#                               for color in colors]
# print(tshirts)

# For other sequence, better use generator expression, for saving memory
t = tuple(str(i) for i in range(100))
# Don't use t = tuple([str(i) for i in range(100)])
print(t)

#------------------------
# To perform Cartesian Product on large amount of element, use generator expression
# for savign memory.
x_set = [i for i in range(100)]
y_set = [i for i in range(500, 600)]
# Use Generator Expression!
# for point in ((x, y) for x in x_set for y in y_set):
#     print(point)

#------------------------
# Use Tuple for records
traveler_ids = [
    ('USA', '31195855'),
    ('BRA', '1E342567'),
    ('ESP', '2DA205856'),
]

for passport in sorted(traveler_ids, key=operator.itemgetter(1)):
    print('%s:%s' % passport)

for country, _ in traveler_ids:
    print(country)

#------------------------
# Slice
l = [i for i in range(10)]
print(l)
# slice assignment, RHS should be an iterable obj.
l[2:5] = [20, 30]
# deletion
print(l)
del l[5:7]
print(l)
#------------------------
# +, * Operator on sequence obj

board = [[None] * 3 for i in range(3)]
board[-1][-1] = 100

# Notice the difference: 
# The following code is equivlant to
# row = [None] * 3
# wierd_board = []
# for i in range(3):
#    wierd_board.append(row)

wierd_board = [[None] * 3] * 3
wierd_board[-1][-1] = 123

print(board)
print(wierd_board)

# The Correct one should be 
# board = []
# for i in range(3):
#   row = [None] * 3
#   board.append(row)

#------------------------
# tuple Inplace addition
# Also mentioned in python official document.
try:
    t = (1,2, [30, 40])
    t[2] += [50, 60]
except TypeError as e:
    print('TypeError: \'tuple\' object does not support item assignment.')

print(t)
#------------------------
# Array
from array import array
from random import random
floats = array('d', (random() for i in range(10**5)))
fp = open('float.bin', 'wb') 

floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('float.bin', 'rb')
floats2.fromfile(fp, 10**5)
fp.close()

assert floats == floats2
# array.tofile & array.fromfile is way more faster than normal file read operation
# because all data need to be converted to float when use normal file read operation.

#------------------------
# deque
from collections import deque
dq = deque(range(10), maxlen=10)
dq.rotate(-1)
# will remove the rightmost element, and add -1 to the begining of the queue.
dq.appendleft(-1)
# will remove the 3 elements at the begining of the queue and add 3 new elements to the end.
dq.extend([11,22,33])

print(dq)
left = dq.popleft()
print(dq)
right = dq.pop()
print(dq)

