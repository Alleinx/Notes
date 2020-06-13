import os
import logging
os.environ["CUDA_VISIBLE_DEVICES"] = "0"    #Set cuda device

import torch.optim as optim
import torch
import torchvision
import torchvision.transforms as transforms
from model import *
from config import *
from train_util import get_cuda
import argparse
from tqdm import tqdm


def train(trainloader):
    # Init data loader:
    dataloader = iter(trainloader)

    # Init model:
    model = Model()
    model = model.type(torch.cuda.FloatTensor)

    # Init Optimization scheme
    criterion = nn.CrossEntropyLoss().cuda()
    optimizer = optim.Adam(model.parameters())

    # Used in CCU:
    loss_samples = get_cuda(torch.zeros(CCU_gap, 1))
    loss_counter = 0

    # Main loop:
    for i in tqdm(range(training_step)):  # loop over the dataset multiple times
    
        running_loss = 0.0

        # get data here
        try:
            inputs, labels = dataloader.next()
        except StopIteration:
            dataloader = iter(trainloader)
            inputs, labels = dataloader.next()
        labels = get_cuda(labels)

        # zero the parameter gradients
        optimizer.zero_grad()

        # Choose CCU or not:
        if loss_counter < CCU_gap:
            outputs = model(inputs)

        elif loss_counter == CCU_gap and use_CCU:
            # print('use CCU:')
            remain_step = get_cuda(torch.tensor(training_step - i, dtype=torch.float))
            outputs = model(inputs, use_ccu=True, loss_samples=loss_samples, remaining_step=remain_step, training_step=i)

            # reset CCU loss counter and samples.
            loss_counter = 0
            loss_samples = get_cuda(torch.zeros(CCU_gap, 1))

        elif loss_counter == CCU_gap and not use_CCU:
            outputs = model(inputs)

            # TODO: remove redundancy
            loss_counter = 0
            loss_samples = get_cuda(torch.zeros(CCU_gap, 1))
        else:
            # Should not get into here
            raise RuntimeError('There may be bugs in loss_counter')

        # calculate loss 
        loss = criterion(outputs, labels)
        running_loss += loss.item()

        # Update ccu_loss_samples and loss_counter
        loss_samples[loss_counter] = loss.item()
        loss_counter += 1

        # 1 step BP
        loss.backward()
        optimizer.step()

        # print statistics
        if i % showstep == 0:   
            print('Training step: {} loss: {}'.format
                (i, running_loss / showstep))

            running_loss = 0.0

    print('Finished Training')
    return model

def test(testloader, model):

    """
    Test unit
    # TODO: Move to eval.py later
    """

    correct = 0
    total = 0

    with torch.no_grad():
        for data in testloader:
            images, labels = data
            labels = get_cuda(labels)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)

            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('Accuracy of the network on the 10000 test images: {}%'.format(
        100 * correct / total))

def main(opt):
    # Transform data
    transform = transforms.Compose(
        [transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    # Load data:
    trainset = torchvision.datasets.CIFAR10(root='data', train=True,
                                            download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                            shuffle=True, num_workers=2)

    testset = torchvision.datasets.CIFAR10(root='data', train=False,
                                        download=True, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                            shuffle=False, num_workers=2)

    # Define classes:
    classes = ('plane', 'car', 'bird', 'cat',
            'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
    
# if opt.train:
    model = train(trainloader)
# elif opt.test:
    test(testloader, model)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', type=str, default="yes")
    parser.add_argument('--test', type=str, default="No")
    
    logging.basicConfig(format='[%(asctime)s:\t %(message)s]', level=logging.INFO)
    opt = parser.parse_args()
    main(opt)