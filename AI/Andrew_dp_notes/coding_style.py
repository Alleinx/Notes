# Python numpy vector notes.
import numpy as np

a = np.random.randn(5)

print(a)
print(a.shape) #neither col vector nor row vector
print(a.T)
print(np.dot(a, a.T))

a = np.random.randn(5, 1) # (5,1) col vector

print(a)
print(a.shape)
# assert(a.shape == (5,1))
print(a.T)
print(np.dot(a, a.T))