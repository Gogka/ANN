from ANNLayer import *

class ANN():
    ### Class Artificial Neural network  ###

    # Initializing
    def __init__(self, layers):
        self.layers = layers

    # Method for getting result from network
    def think(self, inputs, layer_index = 0):
        current_layer = self.layers[layer_index]
        if layer_index == (len(self.layers) - 1):
            return current_layer.get_outputs(inputs)
        return self.think(current_layer.get_outputs(inputs), layer_index + 1)