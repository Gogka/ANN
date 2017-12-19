from ANNLayer import *

class ANN():
    def __init__(self, layers):
        self.layers = layers
        self.last_layer = ANNLayer(layers[-1])

    def think(self, inputs):


