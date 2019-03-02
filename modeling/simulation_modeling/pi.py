# THIS program simulate the value of pi
import random as rd
count = 0
SIMU = 100000
for i in range(SIMU):
    x = pow(rd.random(),2)
    y = pow(rd.random(),2)
    if x + y <= 1:
        count += 1

print('pi = ' + str(4 * count / SIMU))

