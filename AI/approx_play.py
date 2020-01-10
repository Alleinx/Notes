# This program tends to learn why NN can approximate any function:
# 1.Compare linear & non-linear activation function.
# 2.Use different non-linear activation function.

import matplotlib.pyplot as plt
import numpy as np  
import torch
import torch.nn as nn
import torch.optim as optim
import tqdm

def generate_target(x):
    '''
    This function generate ground truth label according to given input x, and the function need to be approximated.
    '''
    return np.sin(x) + 2 * np.tanh(x) - np.cos(x)

class LinearModel(nn.Module):

    def __init__(self):
        super().__init__()
        # When dim is set to a small number, the training procedure is unstable using ReLu activation function,
        # Meaning if the weight is initialized bad, then the "Dead gradient" issue will occur.
        self.first_layer = nn.Linear(1, 100)
        self.second_layer = nn.Linear(100, 50)
        self.third_l = nn.Linear(50, 1)
    
    def forward(self, x):
        # first layer:
        y = self.first_layer(x)
        # using tanh:
        y = torch.tanh(y)
        # using relu:
        # y = torch.relu(y)

        # second layer:
        y = self.second_layer(y)
        y = torch.tanh(y)
        # y = torch.relu(y)

        # output layer:
        y = self.third_l(y)

        return y

# Training data:
train_x = np.arange(-10.0, 10.0, 0.3)
train_y = generate_target(train_x)

train_x = torch.from_numpy(train_x).to(dtype=torch.float32).view(-1, 1)
train_y = torch.from_numpy(train_y).to(dtype=torch.float32).view(-1, 1)

# Init model:
model = LinearModel()
# Init optimizer
optimizer = optim.Adam(model.parameters(), lr=1e-2)
# Init loss function
loss_fn = nn.MSELoss()

iter = 20000

for i in tqdm.tqdm(range(1, iter+1)):
    predict = model(train_x)
    loss = loss_fn(predict, train_y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if i % 1000 == 0:
        print('Iteration:', i, 'Loss:', float(loss))

# CV:
cv_x = np.arange(-10.0, 10.0, 0.1)
cv_y = generate_target(cv_x)

# Plot:
with torch.no_grad():
    predicted = model(torch.from_numpy(cv_x).to(dtype=torch.float32).view(-1, 1))
    plt.plot(cv_x, cv_y, 'r--', cv_x, predicted.detach().numpy(), 'x', alpha=0.4)
    plt.show()
