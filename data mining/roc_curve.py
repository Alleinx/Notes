import matplotlib.pyplot as plt

x_fpr = [0, 0.2 ,0.2, 0.2, 0.4, 0.4, 0.6, 0.8, 1, 1]
y_tpr = [0.2, 0.2, 0.4, 0.6, 0.6, 0.8, 0.8, 0.8, 0.8, 1]

plt.scatter(x_fpr, y_tpr, c='green', alpha=0.2)
plt.plot([0, 1], [0, 1], c='red', alpha = 0.4)
plt.plot([0, 0.2, 0.4, 1.0], [0.2, 0.6, 0.8, 1.0], c='blue')
plt.xlabel('FPR')
plt.ylabel('TPR')

plt.ylim(ymin = 0)
plt.ylim(ymax = 1)
plt.xlim(xmin = 0)
plt.xlim(xmax = 1)
plt.show()