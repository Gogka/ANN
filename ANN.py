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

    # Method for training network
    def train(self, set_inputs, set_training_values, number_of_training_iterations = 100):
        for _ in range(0, number_of_training_iterations):
            for training_value in set_training_values:
                network_result = self.think(training_value)
                self.set_delta_for_last_layer(training_value, network_result)
                self.set_deltas(self.layers[-1].deltas)
                print "\n"



    # Method for getting derivative sigmoid
    def get_derivative(self, point):
        return (array(1)-array(point))*point


    def set_delta_for_last_layer(self, training_value, result):
        self.layers[-1].deltas = (array(training_value) - array(self.layers[-1].outputs)) * self.get_derivative(result)

    def set_deltas(self, previous_deltas, layer_index = -2):
        if len(self.layers) == 1 or layer_index == (len(self.layers) * (-1)) - 1:
            return
        layer = self.layers[layer_index]
        ##
        print layer.neurons[0].incoming_weights
        print previous_deltas
        print "\n"
        ##
        layer.deltas = self.get_derivative(layer.outputs) * [sum(neuron.incoming_weights * previous_deltas) for neuron in self.layers[layer_index+1].neurons]
        self.set_deltas(layer.deltas, layer_index-1)







