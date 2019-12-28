import imageio
import torch
import numpy as np
import matplotlib.pyplot as plt

# Original Image:
cat_arr = torch.from_numpy(imageio.imread('./cat.jpg')).short()

# Mean Image:
# cat_arr = cat_arr.mean(-1, dtype=torch.float)

# Std Image:
# cat_arr = cat_arr.std(-1)

# Variance Image:
# cat_arr = cat_arr.float().var(-1)

print(cat_arr.shape)

plt.imshow(cat_arr)
plt.show()

# Random Image:
rand_img = torch.randint(256, (1024,2048,3))
plt.imshow(rand_img)
plt.show()