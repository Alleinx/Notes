# The Wine Quality data set is available at:
# https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv
# keys: Tensor operation(mean, var), one-hot eoncoding conversion(tensor.discrete())

import csv
import torch
import numpy as np

# Load Data:
# Could use csv/numpy/pandas to load data from a csv file.
file_path = './data/winequality-white.csv'
data = np.loadtxt(file_path, dtype=np.float, delimiter=';', skiprows=1)
print(data.shape, data[0])

# convert numpy array to PyTorch Tensor:
data = torch.from_numpy(data)
print(data.dtype)
input_x = data[:, :-1]
input_y = data[:, -1].to(dtype=torch.long)
print(input_y[:10])

# convert y to one-hot vectors:
# Since we have 10 rank levels, 10 elements are required in each vector
y = torch.zeros(input_y.shape[0], 10)

# Use scatter to achieve one-hot encoding:
y.scatter_(-1, input_y.unsqueeze(1), 1)
# Parameters:
# 1st: dim, along which attribute.
# 2nd: the column tensor indicating the indices of the elements to scatter.
# - the tensor should have the same # of dimensions as the y_onehot, which is 2, so 
# we use unsqueeze to adds an extra dimension. (from (4898) to (4898,1)).
# 3rd: tensor containing the elements to scatter.
print(y[:10])

# Normalize the input data (Using z-norm/standardization):
x_mean = torch.mean(input_x, dim=0)
x_variance = torch.var(input_x, dim=0)
x = (input_x - x_mean) / torch.sqrt(x_variance)
print(x[:10])

# Determine which types of wine are bad:
# wines with rank < 3 is bad:
bad_index = torch.le(input_y, 3)
print(bad_index.shape, bad_index[:10], bad_index.sum())

bad_data = data[torch.le(input_y, 3)]
mid_data = data[torch.lt(input_y, 7) & torch.gt(input_y, 3)]
good_data = data[torch.ge(input_y, 7)]

bad_mean = torch.mean(bad_data, dim=0)
mid_mean = torch.mean(mid_data, dim=0)
good_mean = torch.mean(good_data, dim=0)

for i, args in enumerate(zip(next(csv.reader(open(file_path), delimiter=';')), bad_mean, mid_mean, good_mean)):
    print('{:2} {:20} {:6.2f} {:6.2f} {:6.2f}'.format(i, *args))
