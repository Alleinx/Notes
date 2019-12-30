import torch

def main(n_epochs, learning_rate, params, x, y):
    for epoch in range(1, n_epochs + 1):
        if params.grad is not None:
            params.zero_()

        y_predict = model(x, *params)
        loss = loss_fn(y_predict, y)
        loss.backward()

        params = (params - learning_rate * params.grad).detach().requires_grad_()

        if epoch % 1000 == 0:
            print('Epoch', epoch, 'Loss', loss)
    
    return params


def main_w_optim(n_epochs, optimizer, params, x, y):
    '''
    Training progress with optimizer
    1. Get predicted value with model
    2. Calculate loss
    3. Update Gradient
      3.1 zero_grad() first.
      3.2 call loss.backward().
    4. Update Parameters with optimizer.step().
    '''
    for epoch in range(1, n_epochs + 1):
        predicted = model(x, params)
        loss = loss_fn(predicted, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 1000 == 0:
            print('Epoch', epoch, 'Loss', loss)
    
    return params

if __name__ == "__main__":
    import torch.optim as optim
    print(dir(optim))

    # The usage of optimizer:
    params = torch.tensor([1, 1], dtype=torch.float, requires_grad=True)
    learning_rate = 1e-3
    
    # optimizer will store all of the input parameters and update the 
    # parameters with optimizer.step()
    optimizer = optim.Adam(params, lr=learning_rate)

    # LOOP:
    predicted = model(x, *params)

    # remember to zero out all gradients:
    # zero_grad() method should be invoked before the .backwrad() method.
    optimizer.zero_grad()

    # calculate loss 
    loss = loss_fn(predicted, y)

    # calculate and update grad attributes:
    loss.backward()

    # update parameters:
    optimizer.step()
    # END LOOP