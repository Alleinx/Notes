from scipy.interpolate import interp1d
import numpy as np
import random

avg_cubic = 0.0
avg_linear = 0.0
num_iter = 2000
x = [0, 0.01, 0.03, 0.08, 0.2, 0.4, 0.67, 0.85, 0.93, 0.97, 1]
q = [1000, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 2000]

# interpolation to get f(p)
f_linear = interp1d(x, q)
f_cubic = interp1d(x, q, kind='cubic')

for i in range(num_iter):
    I_linear = 0.0   #Current inventory in gallons
    I_cubic = 0.0
    C_linear = 0.0   #Total running cost
    C_cubic = 0.0
    c_linear = 0.0   #average daily cost
    c_cubic = 0.0
    Flag = 0    #An indicator used to terminate the algorithm

    T = 2   #Time between deliveries in days
    Q = 2500   #Deliver quantity of gasoline in gallons
    N = 100   #Number of days to run the simulation

    d = 20 #Deliver cost
    s = 50  #Storage cost

    #Initialize:
    K = N
    Flag = 0

    while True:
        #Begin the next inventory cycle with a delivery:
        I_linear +=  Q
        I_cubic += Q

        C_linear += d
        C_cubic += d

        #Determine if the simulation will terminate during this cycle:
        if T >= K:
            T = K
            Flag = 1

        for i in range(T):
            x_i = random.random()

            qi_linear = f_linear(x_i)
            qi_cubic = f_cubic(x_i)

            I_linear = I_linear - qi_linear 
            I_cubic = I_cubic - qi_cubic

            if I_linear <= 0:
                I_linear = 0
            else:
                C_linear = C_linear + I_linear * s
            
            if I_cubic <= 0:
                I_cubic = 0
            else:
                C_cubic = C_cubic + I_cubic * s

            K = K - 1

        if Flag == 0:
            continue
        
        c_linear = C_linear / N
        c_cubic = C_cubic / N
        
        break
    avg_cubic += c_cubic
    avg_linear += c_linear

print('average result with linear spline model:', avg_linear / num_iter, 
    '\naverage result with cubic spline model:', avg_cubic / num_iter)

