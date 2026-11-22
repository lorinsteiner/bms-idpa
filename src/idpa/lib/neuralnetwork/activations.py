from enum import StrEnum
from torch import nn

class Activation(StrEnum):
    RELU = "ReLU"
    SIGMOID = "Sigmoid"
    TANH = "Tanh"

def activation_module(activation: Activation):
    match activation:
        case Activation.RELU:
            return nn.ReLU()
        case Activation.SIGMOID:
            return nn.Sigmoid()
        case Activation.TANH:
            return nn.Tanh()
