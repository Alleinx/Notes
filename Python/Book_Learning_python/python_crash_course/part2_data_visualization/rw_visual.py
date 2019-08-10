import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x, rw.y, s=3, c=rw.y, cmap=plt.cm.Blues, edgecolors='none')
    plt.show()

    keep_running = input('Make another walk? (y/n)')
    if keep_running == 'n':
        break