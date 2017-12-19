from ANNNeuron import *

class ANNLayer():
    def __init__(self, number_of_inputs, number_of_neurons = 1):
        self.neurons = [ANNNeuron(number_of_inputs) for _ in range(number_of_neurons)]

    def get_outputs(self, inputs):
        return [neuron.get_outputs(inputs) for neuron in self.neurons]

