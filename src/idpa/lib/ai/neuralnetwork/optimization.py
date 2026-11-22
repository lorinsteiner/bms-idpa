from collections.abc import Iterable
from enum import StrEnum
import torch
from torch import nn

class Optimization:
    type: OptimizationType
    learning_rate: float
    momentum: float = 0

class OptimizationType(StrEnum):
    ADAM = "Adam"
    SGD = "SGD"

def optimizer(optimization: Optimization, params: Iterable[nn.Parameter]) -> torch.optim.Optimizer:
    match optimization.type:
        case OptimizationType.ADAM:
            return torch.optim.Adam(params, lr=optimization.learning_rate)
        case OptimizationType.SGD:
            return torch.optim.SGD(params, lr=optimization.learning_rate, momentum=optimization.momentum)
