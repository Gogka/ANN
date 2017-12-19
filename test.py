
from ANNLayer import *

if __name__ == "__main__":
    layer = ANNLayer(number_of_inputs = len([1,2,3]), number_of_neurons = 3)
    for outputs in layer.get_outputs([1, 2, 3]):
        print outputs