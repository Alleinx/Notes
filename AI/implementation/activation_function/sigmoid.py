#Activation Function: sigmoid
#cons: 
#   1. Computational expensive(Comparing to ReLU)
#   2. Vanishing Gradient when x >> 0 or  x << 0.


import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

print(sigmoid(0.3), sigmoid(-0.3))
