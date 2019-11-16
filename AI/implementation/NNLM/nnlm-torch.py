import numpy as numpy
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable

dtype = torch.FloatTensor

sentences = ['I like dog', 'I love coffee', 'I hate milk']

word_list = ' '.join(sentences)
word_list = word_list.split()
word_list = list(set(word_list))

word_dict = {element: index for index,element in enumerate(word_list)}
number_dict = {index: element for index, element in enumerate(word_list)}

# number of Vocabulary
n_class = len(word_dict) 

# NNLM parameter
n_step = 2
n_hidden = 2
m = 2
