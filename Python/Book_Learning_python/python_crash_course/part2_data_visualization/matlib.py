import matplotlib.pyplot as plt

x = [i for i in range(1, 6)]
y = [i**2 for i in range(1, 6)]

plt.plot(x ,y, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(labelsize=5)

plt.show()