from ANNNeuron import *

class ANNLayer():
    ### Artificial Neural Network Layer ###

    # Initializing
    # number_of_inputs - amount inputs for each neuron in layer to generic weights
    # number_of_neurons - amount neurons in layer
    #
    def __init__(self, number_of_inputs = None, number_of_neurons = 1, parent_layer = None):
        if parent_layer == None:
            self.neurons = [ANNNeuron(number_of_inputs) for _ in range(number_of_neurons)]
        else:
            self.neurons = [ANNNeuron(len(parent_layer.neurons)) for _ in range(number_of_neurons)]

    def get_outputs(self, inputs):
        return [neuron.get_outputs(inputs) for neuron in self.neurons]

