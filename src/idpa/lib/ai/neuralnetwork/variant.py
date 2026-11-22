from idpa.lib.ai.neuralnetwork.loss import Loss
from idpa.lib.ai.neuralnetwork.optimization import Optimization
from idpa.lib.ai.neuralnetwork.initialization import Initialization
from idpa.lib.ai.neuralnetwork.activations import Activation
from dataclasses import dataclass

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


