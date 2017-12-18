from random import randrange
from numpy import exp, array

class ANNNeuron():
    def __init__(self, number_of_inputs):
        self.incoming_weights = [randrange(20)-10 for _ in range(number_of_inputs)]

    def get_outputs(self, inputs):
        return self.sigmoid(sum(self.incoming_weights*array(inputs)).T)

    def sigmoid(self, x):
        return 1/(1+exp(-x))