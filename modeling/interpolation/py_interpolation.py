#python code for interpolation

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

x = [0, 0.01, 0.03, 0.08, 0.2, 0.4, 0.67, 0.85, 0.93, 0.97, 1]
q = [1000, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 2000]

f = interp1d(x, q)
f2 = interp1d(x, q, kind='cubic')

x_new = np.linspace(0, 1, num = 50, endpoint = True)
plt.plot(x, q, 'o', x_new, f(x_new), '-', x_new, f2(x_new), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()
