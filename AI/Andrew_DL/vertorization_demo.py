# Demonstrate difference between vertorization calculation and for loop calculation.

import numpy as np
import time

x = np.random.rand(1000000)
w = np.random.rand(1000000)

tic = time.time()
c1 = np.dot(w,x)
toc = time.time()

print(c1)
print("vertorization version:" + str(1000*(toc-tic)) + "ms")

tic = time.time()
c2 = 0

for i in range(1000000):
    c2 += w[i]*x[i]
toc = time.time()

print(c2)
print("for loop version:" + str(1000*(toc-tic)) + "ms")

