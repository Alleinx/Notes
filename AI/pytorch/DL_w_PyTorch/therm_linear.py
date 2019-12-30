import torch 
import torch.optim as optim
import torch.nn as nn

t_c = [0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0]
t_u = [35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4]

# Get Data:
t_c = torch.tensor(t_c, dtype=torch.float).view(-1, 1)
t_u = torch.tensor(t_u, dtype=torch.float).view(-1, 1)

# Build model:
linear_model = nn.Linear(1, 1, bias=True)
optimizer = optim.Adam(linear_model.parameters(), lr=1e-2)

# Training:
n_epochs = 10000
for epoch in range(1, n_epochs + 1):
    predicted = linear_model(t_u)

    # We use MSE loss here
    loss_fn = nn.MSELoss()

    loss = loss_fn(predicted, t_c)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 500 == 0:
        print('Epoch:', epoch, 'Loss:', float(loss))
    
print('Weight:', float(linear_model.weight))
print('Bias:', float(linear_model.bias))

# Predict:
data = torch.tensor([1.0])
print(float(linear_model(data)))