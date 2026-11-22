from idpa.lib.neuralnetwork.loss import Loss
from idpa.lib.neuralnetwork.optimization import Optimization
from idpa.lib.neuralnetwork.initialization import Initialization
from idpa.lib.neuralnetwork.activations import Activation
from dataclasses import dataclass
from enum import StrEnum

@dataclass(frozen=True)
class Variant:
    inputLayer: int
    hiddenLayers: list[int]
    outputLayer: int
    activation: Activation
    initialization: Initialization
    optimization: Optimization
    lossFunction: Loss
    device: str = "cpu"
    
    def allLayers(self):
        return [self.inputLayer] + self.hiddenLayers + [self.outputLayer]


