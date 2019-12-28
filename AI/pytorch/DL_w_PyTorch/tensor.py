import torch as T
import numpy as np
# Create Tensor:
# 1.random:
a = T.rand(3)
print(a)
print(a[0])

b = T.rand(3,3)
print(b)
print(b[0][1], b[1][2])

c = T.rand(3,3,3)
print(c)
print(c[0][1][2], c[1][0][2])

# 2. from a list/tuple
d = T.tensor([
    [1.0, 2.0],
    [3.0, 4.0],
    [5.0, 6.0],
    (7.0, 8.0)
])
print(d.shape, d[0])

# 3. from numpy
e = np.ones((1,2))
print(type(e))
e = T.from_numpy(e)
print(type(e), e.shape, e)

# 4. Ones/Zeros
a = T.ones(1,2)
b = T.zeros(1, 2)
print(a, b)

# 5. FLoatTensor:
a = T.FloatTensor([[1,2], [3,4]])
print(a)

# Values are stored in Storage instance, which is a flat array.
# Tensors are just views on corresponding Storage instance.
print(a.storage())

# Change sub-tensor has side-effect on the original tensor:
a[0][1] = 10
print(a)

# Clone the tensor 
b = a.clone()
b[-1][-1] = 5
print(b)
print(a)

print(id(a.storage()))
print(id(a.storage()) == id(b.storage()))
print(a.storage())
print(b.storage())

# Transposing:
a = T.rand(3,10)
print(a.shape)
print(a.t().shape)
print(a.view(10, -1).shape, a.size())

# dtype:
print(a.dtype)
a = a.to(T.long)
print(a.dtype)
a = a.double()
print(a.dtype)
a = a.type(T.float)
print(a.dtype)

# Accessing elements:
a = T.rand(3,5)
print(a)
# In genearl: tensor[a:b:v, j:k:h]
# (a,b,v) denotes the (start, end, stride) for row accessing.
# (j,k,h) denotes the (start, end, stride) for column accessing.
print(a[::1, :3:1].diagonal())