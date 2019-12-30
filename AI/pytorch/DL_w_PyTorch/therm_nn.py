import torch 
import torch.optim as optim
import torch.nn as nn

t_c = [0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0]
t_u = [35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4]

# Get Data:
t_c = torch.tensor(t_c, dtype=torch.float).view(-1, 1)
t_u = torch.tensor(t_u, dtype=torch.float).view(-1, 1)

# Build model:
# Hidden layer: Linear(1, dim) + Tanh -> (n, dim)
# Output layer: Linear(dim, 1) -> (1)
dim = 15
model = nn.Sequential(
    nn.Linear(1, dim),
    nn.Tanh(),
    nn.Linear(dim, 1)
)

print(model)

optimizer = optim.Adam(model.parameters(), lr=1e-3)

# Training:
n_epochs = 10000
for epoch in range(1, n_epochs + 1):
    predicted = model(t_u)

    # We use MSE loss here
    loss_fn = nn.MSELoss()

    loss = loss_fn(predicted, t_c)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 500 == 0:
        print('Epoch:', epoch, 'Loss:', float(loss))

# Display parameters:
# 1st Linear layer: weight + bias (hidden)
# 2nd Linear layer: weight + bias (output)
for name, param in model.named_parameters():
    print(name, param.shape)

# Predict:
data = torch.tensor([1.0])
print(float(model(data)))


# Plot figure:
import matplotlib.pyplot as plt

t_range = torch.arange(20.0, 90.0).unsqueeze(1)
plt.xlabel("Fahrenheit")
plt.ylabel("Celsius")
plt.plot(t_u.numpy(), t_c.numpy(), 'o')
plt.plot(t_range.numpy(), model(t_range).detach().numpy(), 'c--')
plt.plot(t_u.numpy(), model(t_u).detach().numpy(), 'kx')
plt.show()