import torch
import torchvision.models
import torch.optim as optim

# Tensor.requires_grad:
# 2 ways to change the requries_gard:
x = torch.rand(3, 1, dtype=torch.float, requires_grad=False)

print('Before requires_grad()_:', x.requires_grad)

# 1st: requires_grad_([Bool]) 
x.requires_grad_()
print('After requires_grad()_:', x.requires_grad)
x.requires_grad_(False)
print('After requires_grad(False)_:', x.requires_grad)

# 2nd: 
print('Manually set requires_grad:')
x.requires_grad = True
print('After requires_grad = True:', x.requires_grad)


# Application:
# 1.Freeze pre-trained model:
model = torchvision.models.resnet18(pretrained=True)

for param in model.parameters():
    param.requires_grad_(False)
    # or param.requires_grad = False

# Replace the layer you want:
model.fc = nn.Linear(512, 100)

# Optimize only the finetune layer:
optimizer = optim.SGD(model.fc.parameters(), lr=1e-3)
