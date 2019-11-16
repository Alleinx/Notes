import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import norm
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.mlab as mlab
import scipy
import math
import matplotlib.image as mpimg

# 1-D random numbers with visualization
rand_1d = np.random.rand(1000, 1)
plt.scatter(rand_1d[:,0], [0 for _ in range(1000)])
plt.show()

# Q1-1.1, Q1-1.2
# 2-D random numbers with visualization
rand_2d = np.random.rand(1000, 2)
plt.scatter(rand_2d[:,0], rand_2d[:,1])
plt.show()

# Q1-1.1, Q1-1.2
# 3-D random numbers with visualization
from mpl_toolkits.mplot3d import Axes3D

rand_3d = np.random.rand(1000,3)
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(rand_3d[:,0], rand_3d[:,1], rand_3d[:,2], marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

# Q1-1.3 
# pdf of 1-d
sns.distplot(rand_1d)
plt.show()

# Q1-1.3 
# pdf of 2-d
df = pd.DataFrame(rand_2d, columns=["x", "y"])
sns.jointplot(x="x", y="y", data=df, kind='regress')
plt.show()

# Q1-1.3 
# pdf of 3-d

sns.distplot(rand_3d[:,0], norm_hist=True, axlabel='X')
plt.show()
sns.distplot(rand_3d[:,1], norm_hist=True, axlabel = 'Y', color="y")
plt.show()
sns.distplot(rand_3d[:,2], norm_hist=True, axlabel = 'Z', color='g')
plt.show()

sns.distplot(rand_3d[:,0], norm_hist=True)
sns.distplot(rand_3d[:,1], norm_hist=True)
sns.distplot(rand_3d[:,2], norm_hist=True)
plt.show()

image = mpimg.imread('lenna.jpeg')
plt.imshow(image, cmap='gray')
plt.show()

# display image shape here:
print('image shape:', image.shape)

# flatten:
flat = image.reshape(1, -1)
print('After flat:', flat.shape)

mean = np.mean(flat)
median = np.median(flat)
min_value = np.min(flat)
max_value = np.max(flat)
mode = scipy.stats.mode(flat, axis=None)

print('mean:', mean)
print('median:', median)
print('min:', min_value)
print('max:', max_value)
print('mode:', *mode[0], 'count:', *mode[-1])

fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='3d')

# Change the angle here:
ax.view_init(90, 10)

x = np.repeat(np.array([i for i in range(512)]), 512)
y = np.array([i for i in range(512)])
y = np.tile(y, 512)

ax.scatter(x, y, flat, marker='o', c = flat[0], cmap='gray')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

# Perform min-max normalization
min_max_norm_flat = (flat - np.min(flat)) / (np.max(flat) - np.min(flat))

fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='3d')

# Change the view angle here:
ax.view_init(90, 10)

x = np.repeat(np.array([i for i in range(512)]), 512)
y = np.array([i for i in range(512)])
y = np.tile(y, 512)

ax.scatter(x, y, min_max_norm_flat, marker='o', c = min_max_norm_flat[0], cmap='gray')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

def plot_bin_image(bins_num):
    print('Number of bins:', bins_num)
    min_max_norm_flat = (flat - np.min(flat)) / (np.max(flat) - np.min(flat))

    bins = [i / bins_num for i in range(bins_num)]
    result = (np.histogram(min_max_norm_flat, bins, weights=min_max_norm_flat)[0] /
                 np.histogram(min_max_norm_flat, bins)[0])

    for i in range(1, len(min_max_norm_flat[-1])):
        for j in range(len(bins)):
            if min_max_norm_flat[0][i] >= bins[j-1] and min_max_norm_flat[0][i] < bins[j]:
                min_max_norm_flat[0][i] = bins[j-1]
            else:
                continue

    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111, projection='3d')

    # Change the view angle here:
    ax.view_init(90, 10)

    x = np.repeat(np.array([i for i in range(512)]), 512)
    y = np.array([i for i in range(512)])
    y = np.tile(y, 512)

    ax.scatter(x, y, min_max_norm_flat, marker='o', c = min_max_norm_flat[0], cmap='gray')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

plot_bin_image(2)
# plot 3, 4, 5, 6, 7bins:
plot_bin_image(3)
plot_bin_image(4)
plot_bin_image(5)
plot_bin_image(6)
plot_bin_image(7)

import warnings
# Ignore system warnings
warnings.filterwarnings('ignore')

plot_bin_image(255)
# As we can see, as the number of bins increase, the image will become more and more clear.