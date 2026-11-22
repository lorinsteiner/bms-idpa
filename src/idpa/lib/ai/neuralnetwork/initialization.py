import math
from torch.nn.init import _NonlinearityType
from idpa.lib.ai.neuralnetwork.activations import Activation
from torch import nn
from enum import StrEnum

class Initialization(StrEnum):
    HE = "He"
    XAVIER = "Xavier"
    NAIVE = "Naive"

def init_parameters(initialization: Initialization, activation: Activation, module: nn.Module):
    if isinstance(module, nn.Linear):
        match initialization:
            case Initialization.HE:
                nn.init.kaiming_normal_(module.weight, nonlinearity=_map(activation))
            case Initialization.XAVIER:
                # U[-sqrt(6/(n_in+n_out)), +sqrt(6/(n_in+n_out))]
                nn.init.xavier_uniform_(module.weight)
            case Initialization.NAIVE:
                # U[-1/sqrt(n_in), +1/sqrt(n_in)]
                limit = 1 / math.sqrt(module.in_features)
                nn.init.uniform_(module.weight, -limit, limit)
        nn.init.zeros_(module.bias)

def _map(activation: Activation) -> _NonlinearityType:
    match activation:
        case Activation.RELU:
            return 'relu'
        case Activation.SIGMOID:
            return 'sigmoid'
        case Activation.TANH:
            return 'tanh'
