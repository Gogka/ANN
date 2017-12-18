from ANNNeuron import *

class ANNLayer():
    def __init__(self, inputs, number_of_neurons):
        self.inputs = inputs
        self.neurons = [ANNNeuron(len(inputs)) for _ in range(number_of_neurons)]

    def get_outputs(self):
        return [neuron.get_outputs(self.inputs) for neuron in self.neurons]

