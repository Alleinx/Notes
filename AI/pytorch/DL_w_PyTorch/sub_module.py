# This program demonstrate how to build your own model, instead of using nn.Sequential()
# The Subclass need to extend nn.Module and implement at least forward() method.
import torch
import torch.nn as nn

class SubclassModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden_layer = nn.Linear(1, 13)
        self.output_layer = nn.Linear(13, 1)

    def forward(self, input):
        '''
        Need to implement this method at least
        '''
        h_t = self.hidden_layer(input)
        # You could customize the computational progress as you wish:
        # This is benefit from the dynamic graph-building property of PyTorch
        if torch.rand() > 0.5:
            h_t = torch.tanh(h_t)
        else:
            print('Unchanged here')
        y_t = self.output_layer(h_t)

        return y_t

if __name__ == "__main__":
    model = SubclassModel()
    print(model)