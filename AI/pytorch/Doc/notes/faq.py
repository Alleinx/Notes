#### Cuda error (2): run out of memory.
# 1. Don't accumulate history.
# By 
total_loss = 0
for i in range(iter):
    optimizer.zero_grad()
    output = model(input)
    loss = criterion(output)
    loss.backward()
    optimizer.step()

    # History will accumulate using following semantics.
    total_loss += loss
    # Instead, use:
    total_loss += float(loss)
