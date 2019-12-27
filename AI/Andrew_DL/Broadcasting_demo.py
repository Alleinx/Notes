# This program demonstrate Broadcasting in python.

# Input: (m,n) matrix; (1,n) matrix; (m,1) matrix;
# Operator: + - * /...
# Broadcasting (by copying): 
#   1. (m,n) op (1,n) -> (m,n) op (m,n)
#   2. (m,n) op (m,1) -> (m,n) op (m,n)

import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0],
    [1.2, 104.0, 52.0, 8.0],
    [1.8, 135.0, 99.0, 0.9]])

cal = A.sum(axis = 0) #0: sum vertically; 1: sum horizontally.

percentage = 100 * (A / cal) 
# Broadcast here, convert cal (1,4) matrix to a (3,4) matrix.

print(percentage) 