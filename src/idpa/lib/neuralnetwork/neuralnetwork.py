from idpa.lib.neuralnetwork.initialization import init_parameters
from idpa.lib.neuralnetwork.activations import activation_module
from torch import nn
from torch.utils.data import DataLoader

from idpa.lib.neuralnetwork.variant import Variant

class NeuralNetwork(nn.Module):

    def __init__(self, variant: Variant):
        super().__init__()

        super().to(variant.device)

        # layer initialization
        self.layers = nn.Sequential()
        self.layers.append(nn.Flatten())

        allLayers = variant.allLayers()
        lastHiddenIndex = len(allLayers) - 1
        prevLayer: int | None = None

        for index, layer in enumerate(allLayers):
            if prevLayer is None:
                prevLayer = layer
                continue
            if index == lastHiddenIndex:
                continue

            self.layers.append(nn.Linear(prevLayer, layer))
            if index != lastHiddenIndex - 1:
                self.layers.append(activation_module(variant.activation))

            prevLayer = layer

        # nn.CrossEntropyLoss internally applies softmax, so no additional nn.Softmax is necessary

        # parameter initialization
        self.apply(lambda module : init_parameters(variant.initialization, variant.activation, module))

    def forward(self, x):
        return self.layers(x)
    


