from random import randrange
from numpy import exp, array

class ANNNeuron():
    ### Class Artificial Neural Network Neuron

    # Initializing
    def __init__(self, number_of_inputs):
        self.incoming_weights = [randrange(20)-10 for _ in range(number_of_inputs)]

    # Method for getting output value
    def get_output(self, inputs):
        return self.sigmoid(sum(self.incoming_weights*array(inputs)))

    # Method for normalization values
    def sigmoid(self, x):
        return 1/(1+exp(-x))