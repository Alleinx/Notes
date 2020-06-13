import torch
import torch.nn as nn
import torch.nn.functional as F
import config
import train_util
import numpy as np
from numpy import random
import logging
import copy

random.seed(123)
torch.manual_seed(123)

class ResNet(nn.Module):
    
    def __init__(self, n=7, res_option='A', use_dropout=False):
        super(ResNet, self).__init__()
        self.res_option = res_option
        self.use_dropout = use_dropout
        # used for CCU:
        self.layer_counter = n
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.norm1 = nn.BatchNorm2d(16)
        self.relu1 = nn.ReLU(inplace=True)
        self.layers1 = self._make_layer(n, 16, 16, 1)
        self.layers2 = self._make_layer(2, 32, 16, 2)
        self.layers3 = self._make_layer(2, 64, 32, 2)
        self.avgpool = nn.AvgPool2d(8)
        self.linear = nn.Linear(64, 10)
    
    def _make_layer(self, layer_count, channels, channels_in, stride):
        return nn.Sequential(
            ResBlock(channels, channels_in, stride, res_option=self.res_option, use_dropout=self.use_dropout),
            *[ResBlock(channels) for _ in range(layer_count-1)])
    
    def add_res_block(self, channels=16, channels_in=16, stride=1):
        """
        Only implement layer1 add/remove/unchanged operation
        """
        extra_block = copy.deepcopy(self.layers1[-1])

        # extra_block = ResBlock(channels, channels_in, stride, res_option=self.res_option, use_dropout=self.use_dropout)
        extra_block = extra_block.type(torch.cuda.FloatTensor)
        self.layers1.add_module(str(self.layer_counter), extra_block)
        self.layer_counter += 1
        logging.info('Added Extra Layer, total layer:{}'.format(self.layer_counter))

    def remove_res_block(self):
        """
        Only implement layer1 add/remove/unchanged operation
        """
        if self.layer_counter > 1:
            del self.layers1[-1]
            self.layer_counter -= 1
            logging.info('Remove one Layer, total layer:{}'.format(self.layer_counter))
        else:
            logging.error('Only 1 layer left, can not remove anymore!')
    
    
    def forward(self, x):
        x = train_util.get_cuda(x)
        out = self.conv1(x)
        out = self.norm1(out)
        out = self.relu1(out)
        out = self.layers1(out)
        out = self.layers2(out)
        out = self.layers3(out)
        out = self.avgpool(out)
        out = out.view(out.size(0), -1)
        out = self.linear(out)
        return out


class ResBlock(nn.Module):
    
    def __init__(self, num_filters, channels_in=None, stride=1, res_option='A', use_dropout=False):
        super(ResBlock, self).__init__()
        
        # uses 1x1 convolutions for downsampling
        if not channels_in or channels_in == num_filters:
            channels_in = num_filters
            self.projection = None
        else:
            if res_option == 'A':
                self.projection = IdentityPadding(num_filters, channels_in, stride)
            elif res_option == 'B':
                self.projection = ConvProjection(num_filters, channels_in, stride)
            elif res_option == 'C':
                self.projection = AvgPoolPadding(num_filters, channels_in, stride)
        self.use_dropout = use_dropout

        self.conv1 = nn.Conv2d(channels_in, num_filters, kernel_size=3, stride=stride, padding=1)
        self.bn1 = nn.BatchNorm2d(num_filters)
        self.relu1 = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(num_filters, num_filters, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(num_filters)

        if self.use_dropout:
            self.dropout = nn.Dropout(p=config.drop_out, inplace=True)
        self.relu2 = nn.ReLU(inplace=True)

    def forward(self, x):
        residual = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu1(out)
        out = self.conv2(out)
        out = self.bn2(out)

        if self.use_dropout:
            out = self.dropout(out)
        if self.projection:
            residual = self.projection(x)
        out += residual
        out = self.relu2(out)
        return out


# various projection options to change number of filters in residual connection
# option A from paper
class IdentityPadding(nn.Module):
    def __init__(self, num_filters, channels_in, stride):
        super(IdentityPadding, self).__init__()
        # with kernel_size=1, max pooling is equivalent to identity mapping with stride
        self.identity = nn.MaxPool2d(1, stride=stride)
        self.num_zeros = num_filters - channels_in
    
    def forward(self, x):
        out = F.pad(x, (0, 0, 0, 0, 0, self.num_zeros))
        out = self.identity(out)
        return out

# option B from paper
class ConvProjection(nn.Module):

    def __init__(self, num_filters, channels_in, stride):
        super(ResA, self).__init__()
        self.conv = nn.Conv2d(channels_in, num_filters, kernel_size=1, stride=stride)
    
    def forward(self, x):
        out = self.conv(x)
        return out

# experimental option C
class AvgPoolPadding(nn.Module):

    def __init__(self, num_filters, channels_in, stride):
        super(AvgPoolPadding, self).__init__()
        self.identity = nn.AvgPool2d(stride, stride=stride)
        self.num_zeros = num_filters - channels_in
    
    def forward(self, x):
        out = F.pad(x, (0, 0, 0, 0, 0, self.num_zeros))
        out = self.identity(out)
        return out

class CCU_Atten(nn.Module):
    def __init__(self):
        super(CCU_Atten, self).__init__()
        self.W_A = nn.Linear(config.CCU_Atten_features, config.CCU_Atten_features)

    def forward(self, CCU_features):
        x = self.W_A(CCU_features)
        et = F.relu(x)
        at = F.softmax(x, dim=0).view(1, -1)
        CCU_features = CCU_features.view(1, -1)

        # For DEBUG:
        # print('Inside CCU_Atten: at:', at)
        # print('Inside CCU_Atten: features:', CCU_features)

        ct_CCU = at * CCU_features
        ct_CCU = torch.sum(ct_CCU)

        return ct_CCU


class CCU(nn.Module):
    def __init__(self):
        super(CCU, self).__init__()

        # number of iterations before self-evolution:
        self.CCU_S = config.CCU_gap

        # Feature 1
        self.CCU_loss_sampeles = nn.Linear(self.CCU_S, config.hidden_unit)
        self.CCU_loss_sampeles_2 = nn.Linear(config.hidden_unit, config.hidden_unit)
        # Feature 2
        self.CCU_loss_begining = nn.Linear(1, config.hidden_unit)
        self.CCU_loss_begining_2 = nn.Linear(config.hidden_unit, config.hidden_unit)
        # Feature 3
        self.CCU_loss_end = nn.Linear(1, config.hidden_unit)
        self.CCU_loss_end_2 = nn.Linear(config.hidden_unit, config.hidden_unit)
        # Feature 4
        self.CCU_loss_diff_begin_end = nn.Linear(1, config.hidden_unit)
        self.CCU_loss_diff_begin_end_2 = nn.Linear(config.hidden_unit, config.hidden_unit)
        # Feature 5
        self.CCU_loss_remain_train_steps = nn.Linear(1, config.hidden_unit)
        self.CCU_loss_remain_train_steps_2 = nn.Linear(config.hidden_unit, config.hidden_unit)
        # Feature 6
        self.CCU_loss_avg_changing_rate = nn.Linear(1, config.hidden_unit)
        self.CCU_loss_avg_changing_rate_2 = nn.Linear(config.hidden_unit, config.hidden_unit)

        # CCU_Attention_unit:
        self.CCU_Atten = CCU_Atten()

        # Final layer:
        self.CCU_final = nn.Linear(1, config.hidden_unit)
        self.CCU_final_2 = nn.Linear(config.hidden_unit, config.CCU_number_of_choices)
    
    def forward(self, loss_samples, loss_begining, loss_ending, remaining_training_steps, model):

        # f1 feature:
        f1 = F.relu(self.CCU_loss_sampeles(loss_samples))
        f1 = torch.tanh(self.CCU_loss_sampeles_2(f1).squeeze(0)).view(-1, 1)

        # f2 feature
        f2 = F.relu(self.CCU_loss_begining(loss_begining))
        f2 = torch.tanh(self.CCU_loss_begining_2(f2)).view(-1, 1)

        # f3 feature
        f3 = F.relu(self.CCU_loss_end(loss_ending))
        f3 = torch.tanh(self.CCU_loss_end_2(f3)).view(-1, 1)

        # calculate delta loss from (beginging_step - ending_step):
        delta = loss_begining - loss_ending

        # f4 feature:
        f4 = F.relu(self.CCU_loss_diff_begin_end(delta))
        f4 = torch.tanh(self.CCU_loss_diff_begin_end_2(f4)).view(-1, 1)

        # f5 feature:
        remaining_ratio = (remaining_training_steps/config.training_step).view(-1, 1)
        f5 = F.relu(self.CCU_loss_remain_train_steps(remaining_ratio).squeeze(0))
        f5 = torch.tanh(self.CCU_loss_remain_train_steps_2(f5)).view(-1, 1)

        # f6 feature:
        f6 = F.relu(self.CCU_loss_avg_changing_rate(delta/self.CCU_S))
        f6 = torch.tanh(self.CCU_loss_avg_changing_rate_2(f6)).view(-1, 1)

        # concatenate features together:
        features = torch.cat([f1, f2, f3, f4, f5, f6], dim=1)

        # Go into CCU attention:
        ct_CCU = self.CCU_Atten(features)
        ct_CCU = ct_CCU.view(-1, 1)

        # Used to choose operation:
        et = F.relu(self.CCU_final(ct_CCU))
        et = F.relu(self.CCU_final_2(et))

        final_operation_p = F.softmax(et, dim=1)
        final_operation_p = final_operation_p.squeeze(0)
        # TODO: add learn here

        operation_index = self.choose_operation(final_operation_p, model)

        return ct_CCU, final_operation_p
    
    def choose_operation(self, p, model):
        # TODO: change to dynamicall calculation:
        choice = np.random.rand(1)[0]

        if choice < config.threshold:
            max_p = max(p)
            for i in range(len(p)):
                if p[i] == max_p:
                    final_choice = i
                    break
        else:
            rand_operation = np.random.rand(1)[0]
            threshold1 = p[0]
            threshold2 = p[0] + p[1]
            threshold3 = 1

            # For debug
            # print(p)
            # print(rand_operation)
            # logging.info('Threshold: ({}, {}, {})'.format(threshold1, threshold2, threshold3))

            if rand_operation < threshold1:
                # first case: add layer
                final_choice = 0
            elif threshold1 < rand_operation < threshold2:
                # second case: remove layer
                final_choice = 1
            elif rand_operation > threshold2:
                # third case: unchange
                final_choice = 2

        if final_choice == 0:
            model.add_layer()
        elif final_choice == 1:
            model.remove_layer()
        elif final_choice == 2:
            model.unchange()




class Model(nn.Module):
    """
    Complete model structure.
    Model consists of 3 parts:
    1. NetBlock (Conv layer with res connection).
    2. CCU(Central Controlling Unit): used to control wheter to:
        2.1 Add another layer
        2.2 Remove the last-added layer
        2.3 Retain unchanged.
    3. Historical Attention (HA) mechanism:
        - Store all history every $S$ steps and attend on them.
    """

    def __init__(self):
        super(Model, self).__init__()

        self.ResNet = ResNet(n=config.init_layers, use_dropout=True)
 
        if config.use_CCU:
            self.CCU = CCU()
            self.w_ccu = nn.Linear(1, config.hidden_unit)
            self.w_ccu_2 = nn.Linear(config.hidden_unit, 10)            # bs, output size
            self.w_p = nn.Linear(3, config.hidden_unit)
            self.w_p2 = nn.Linear(config.hidden_unit, 10)

        # TODO: add HA block.
        # self.HA = HA()
    
    def forward(self, x, use_ccu=False, loss_samples=None, remaining_step=None, training_step=None):
        x = train_util.get_cuda(x)
        x = self.ResNet(x)

        if use_ccu == True:
            if training_step and training_step >= config.warm_up:

                loss_begin = loss_samples[0]
                loss_end = loss_samples[-1]
                loss_samples = loss_samples.view(1, -1)

                c_ccu, final_p = self.CCU(loss_samples, loss_begin, loss_end, remaining_step, self)
                p = F.relu(self.w_p(final_p))
                p = F.relu(self.w_p2(p))
                c_ccu = F.relu(self.w_ccu(c_ccu))
                c_ccu = F.relu(self.w_ccu_2(c_ccu))

                # Add c_ccu to enable learning for CCU parameters:
                x = x + c_ccu + p

        return x

    def add_layer(self):
        self.ResNet.add_res_block()
    
    def remove_layer(self):
        self.ResNet.remove_res_block()

    def unchange(self):
        logging.info('Unchanged.')
