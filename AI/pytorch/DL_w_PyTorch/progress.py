import torch
def main(n_epochs, learning_rate, params, x, y):
    for epoch in range(1, n_epochs + 1):
        if params.grad is not None:
            params.zero_()

        y_predict = model(x, *params)
        loss = loss_fn(y_predict, y)
        loss.backward()

        params = (params - learning_rate * params.grad).detach().requires_grad_()

        if epoch % 1000 = 0:
            print('Epoch', epoch, 'Loss', loss)
    
    return params