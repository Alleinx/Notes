import matplotlib.pyplot as plt
from random_walk import RandomWalk

def scar():
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x, rw.y, s=3, c=rw.x, cmap=plt.cm.Blues, edgecolors='none')

    # # highlight start point and end point
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x[-1], rw.y[-1], c='red', edgecolors='none', s = 100)
    plt.show()

def cont():
    rw = RandomWalk()
    rw.fill_walk()

    plt.plot(rw.x ,rw.y, c = (0.3, 0.6, 0.6))
    plt.show()

if __name__ == "__main__":
    # set window size
    plt.figure(figsize=(10, 6))

    # hide the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    scar()
    cont()