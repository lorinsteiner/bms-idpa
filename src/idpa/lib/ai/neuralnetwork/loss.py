from enum import StrEnum
from torch import nn

class Loss(StrEnum):
    CROSS_ENTROPY = "Cross-entropy"

def loss_module(loss: Loss) -> nn.Module:
    match loss:
        case Loss.CROSS_ENTROPY:
            return nn.CrossEntropyLoss()
