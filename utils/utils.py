import logging
import os

import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable


def numpy_to_tvar(x):
    return Variable(torch.from_numpy(x).type(torch.FloatTensor).to(torch.device("cuda:0")))


def get_norm(file_path):
    normalize_data = np.float32(np.loadtxt(file_path))
    mean = normalize_data[0]
    std = normalize_data[1]
    for i in range(std.size):
        if std[i] == 0:
            std[i] = 1
    return mean, std

