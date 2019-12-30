import torch
import torch.nn as nn

# x: (batch_size, #feature_dim)
x = torch.rand(3,2, dtype=torch.float)

# Linear(input_size, output_size)
# input_size = #feature_dim.
linear_layer = nn.Linear(2,1, bias=True)
print(x)

# Calling an instance of nn.Module ends up calling the 'forward()' method.
# The forward() method executes the forward computation;
# __call__() does sth else before and after calling forward().
# Thus, DO NOT DIRECTLY CALL forward() in user code;
print(linear_layer(x))
print(linear_layer.weight)
print(linear_layer.bias)

# Briefly demonstrate the implementation of Module.call:
# Lots of hooks won't get called properly if directly use .forward() in user code.
def __call__(self, *input, **kwargs):
    for hook in self._forward_pre_hooks.values():
        hook(self, input)
    
    result = self.forward(*input, **kwargs)

    for hook in self._forward_hooks.values():
        hook_result = hook(self, input, result)
        # ...
    
    for hook in self._backward_hooks.values():
        pass
        # ...
    #...
    return result