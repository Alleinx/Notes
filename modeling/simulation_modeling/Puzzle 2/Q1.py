import random
import math

iter = 100
avg_result = 0.0

for i in range(iter):
    
    limit = 100
    
    first_octant = 0

    for i in range(limit):
        x = random.uniform(-1, 1)   
        y = random.uniform(-1 * math.sqrt(1 - pow(x, 2)), math.sqrt(1 - pow(x, 2)))   
        z = random.uniform(-1 * math.sqrt(1 - pow(x, 2) - pow(y, 2)), math.sqrt(1 - pow(x, 2) - pow(y,2)))
            
        if x > 0 and y > 0 and z > 0:
            first_octant += 1

    avg_result += (first_octant / limit)

print(avg_result / iter)

