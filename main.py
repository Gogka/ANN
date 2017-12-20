
from ANNLayer import *
from ANN import *

if __name__ == "__main__":
    inputs = [1,2,3]
    layer = ANNLayer(number_of_inputs = len(inputs), number_of_neurons = 3)
    layer2 = ANNLayer(number_of_neurons = 3, parent_layer = layer)
    layer3 = ANNLayer(parent_layer = layer2)
    #ayer2 = ANNLayer(number_of_inputs = len(layer.get_outputs(inputs)), number_of_neurons = 3)
    #layer3 = ANNLayer(number_of_inputs = len(layer2.get_outputs(layer.get_outputs(inputs))))
    network = ANN([layer, layer2, layer3])
    print network.think(inputs)